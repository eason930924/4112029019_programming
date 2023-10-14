import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.137.1",3000))
outdata = input("傳送訊息至伺服器:")
s.send(outdata.encode())
indata = s.recv(1024)
print("由伺服器接收:",indata.decode())
s.close()
