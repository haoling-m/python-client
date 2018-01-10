# Echo client program
import socket

HOST = '192.168.66.187'
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#s.send(bytes("*idn?", 'UTF-8'))
s.send(bytes("hellooo", 'UTF-8'))
data = s.recv(1024)
s.close()
print(data.decode('utf-8'))
