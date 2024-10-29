import serial.tools.list_ports

def list_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Port: {port.device}")
        print(f"Description: {port.description}")
        print(f"Hardware ID: {port.hwid}")
        print(f"PID: {port.pid}, VID: {port.vid}")
        print(f"locationID: {port.location}")
        print(f"interfaceId: {port.interface}")
        print("-" * 40)

if __name__ == "__main__":
    list_ports()
