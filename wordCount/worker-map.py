#!/usr/bin/python3
from libFunction.map import map
import socket
import time
import base64
from datetime import datetime
status = False 
dataProcess = ""
class WorkerMap:
	global status
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.host ,self.port))

	def workerSendMsgToMaster(self,str_send):
		self.sock.send(bytes(str_send, 'utf-8'))

	def listenMaster(self):
		data = self.sock.recv(1024)
		if data != b'':
			now = datetime.now()
			date_time = now.strftime("%m/%d/%Y %H:%M:%S")
			data = str(data,"utf-8")
			dataProcess = data
			str_decode64 = base64.b64decode(dataProcess)
			str_decode64 = str(str_decode64,"utf-8")
			self.workerSendMsgToMaster(map(str_decode64))
			print(date_time,"-",str_decode64)

	def getStatus(self):
		return status
if __name__ == "__main__":
	node = WorkerMap(socket.gethostname(), 9999)
	while True:
		node.listenMaster()
		