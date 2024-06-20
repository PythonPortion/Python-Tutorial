import socket

# 选择服务器地址和端口号
SERVER_ADDRESS = 'localhost'
PORT = 12345

# 创建一个 TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
client_socket.connect((SERVER_ADDRESS, PORT))

while True:
    # 发送消息给服务器
    message = input("请输入消息: ")
    client_socket.sendall(message.encode('utf-8'))

    # 接收服务器的响应
    data = client_socket.recv(1024)
    print(f"收到服务器响应: {data.decode('utf-8')}")

# 关闭连接
client_socket.close()
