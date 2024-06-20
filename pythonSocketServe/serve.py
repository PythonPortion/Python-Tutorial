import socket

# 选择一个端口号
PORT = 12345

# 创建一个 TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定到本地地址和端口
server_socket.bind(('localhost', PORT))

# 开始监听连接
server_socket.listen(1)

print("等待连接...")

# 等待客户端连接
client_socket, client_address = server_socket.accept()
print(f"连接来自 {client_address}")

while True:
    # 接收客户端消息
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"收到消息: {data.decode('utf-8')}")

    # 将消息发回给客户端
    client_socket.sendall(data)

# 关闭连接
client_socket.close()
server_socket.close()
