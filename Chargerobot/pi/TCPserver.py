
import socket

# 建立 socket 物件
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 綁定伺服器地址和端口
server_address = ('localhost', 8888)
server_socket.bind(server_address)

# 開始監聽連線
server_socket.listen(1)

print("等待客戶端連線...")

# 接受連線
client_socket, client_address = server_socket.accept()

# 接收客戶端訊息
data = client_socket.recv(1024)
print(f"接收到來自 {client_address} 的訊息：{data.decode('utf-8')}")

# 關閉連線
client_socket.close()
server_socket.close()
