#!/usr/bin/python3
from libFunction.map import map
from libFunction.reduce import reduce
#reduce(map("'foo foo quux labs foo bar quux"))
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 9999
s.connect((host, port))   

str_send = "Hello, the world!\n"
s.send(bytes(str_send, 'utf-8'))

# str_recv = s.recv(1024)
# print(str(str_recv))