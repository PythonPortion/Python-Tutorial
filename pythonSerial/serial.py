import serial

# 创建虚拟串口
ser = serial.serial_for_url('loop://', timeout=1)

# 打开虚拟串口
ser.open()

try:
    # 向虚拟串口写入数据
    ser.write(b'Hello, serial port!\n')

    # 从虚拟串口读取数据
    response = ser.readline()
    print("Received:", response.decode())
finally:
    # 关闭串口
    ser.close()
