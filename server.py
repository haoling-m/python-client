# SBC test server and interpreter program
import socket
HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print("Connected by {0}".format(addr))
while 1:
    data = conn.recv(1024)
    if data:
        print(data)
    if data==b'*IDN?' or data==b'*idn?':
        reply = b'I am beaglebone number 10'
        conn.send(reply)
        break
    if b'Hello' in data or b'hello' in data:
        reply = b'hello'
        conn.send(reply)
        #break
    if data==b'bye': 
        conn.send(data)
        break
conn.close()
