import socket

# 建立 socket 物件
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 連線到伺服器
server_address = ('localhost', 8888)
client_socket.connect(server_address)

# 傳送訊息給伺服器
message = "Hello, server!"
client_socket.sendall(message.encode('utf-8'))

# 關閉連線
client_socket.close()
