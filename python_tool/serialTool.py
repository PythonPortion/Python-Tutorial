# -*- coding: utf-8 -*- 
"""
@Project :LedTool
@File    :serial.py
@IDE     :PyCharm
@Author  :CXL
@Date    :2024/2/19  08:43
"""
import serial
import time
import sys
import plistlib


class SerialCommunication:
    def __init__(self, port, baudrate=115200, timeout=0.6, terminator=None):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.terminator = terminator
        self.serial_port = None

    def open_serial(self):
        self.serial_port = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        time.sleep(0.1)  # 等待一段时间以确保串口已完全打开

    def close_serial(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()

    def send_data(self, data):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.write(data.encode('utf-8'))

    def receive_data(self):
        if self.serial_port and self.serial_port.is_open:
            if self.terminator:
                return self.serial_port.read_until(self.terminator).strip()
            else:
                return self.serial_port.readline().strip()

    def send_data_until_response(self, data_to_send, expected_response, timeout=5):
        start_time = time.time()
        self.send_data(data_to_send)
        received_data = ''
        while True:
            received_data += self.receive_data().decode('utf-8', errors='ignore')
            if expected_response in received_data:
                return received_data
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                return received_data

if __name__ == "__main__":
    args = sys.argv
    command = args[1]
    # 使用示例
    try:
        plist_file_path = '/Users/lingxiao/Desktop/Ports.plist'
        # 读取 plist 文件
        with open(plist_file_path, 'rb') as fp:
            # 使用 load 方法加载 plist 文件内容
            plist_data = plistlib.load(fp)

        print(plist_data)

        port_name = plist_data['Ports'][0]

        print(f'==>port_name==:{port_name}<==')
        serial_comm = SerialCommunication(port_name, 115200)
        serial_comm.open_serial()
        result = serial_comm.send_data_until_response(f"{command}\r\n", "Apple-Watch:~ root#", 5)
        print(f'==>test_result:{result}<==')

    finally:
        if serial_comm:
            serial_comm.close_serial()



