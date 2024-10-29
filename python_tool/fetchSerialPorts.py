# import serial.tools.list_ports

# def list_serial_ports():
#     ports = serial.tools.list_ports.comports()
#     for port in ports:
#         print(f"Device: {port.device}")
#         print(f"Name: {port.name}")
#         print(f"Description: {port.description}")
#         print(f"HWID: {port.hwid}")
#         print(f"Location: {port.location}")
#         print(f"Manufacturer: {port.manufacturer}")
#         print(f"Product: {port.product}")
#         print(f"Interface: {port.interface}")
#         print("")

# if __name__ == "__main__":
#     list_serial_ports()


import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Device: {port.device}")
    print(f"Name: {port.name}")
    print(f"Description: {port.description}")
    print(f"HWID: {port.hwid}")
    print(f"Location: {port.location}")
    print(f"Manufacturer: {port.manufacturer}")
    print(f"Product: {port.product}")
    print(f"Interface: {port.interface}")
    print("")
