import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.137.1',3000))
s.listen(5)
conn,addr = s.accept()
print("連線至",addr)
conn.send(conn.recv(1024))
conn.close()
s.close()
