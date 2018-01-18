# Echo client program
import socket

HOST = '192.168.2.108'    # The remote host
PORT = 13333              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('{"id":0,"jsonrpc":"2.0","method":"miner_getstat2"}')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
