#!/usr/bin/python3
import socket          
import threading
import re
import time
import base64
from datetime import datetime

stringLine = []
indif = []
listMap = []
listReduce = []
addressl = []

def loadingData():
    filepath = 'data/data.txt'
    with open(filepath) as file_in:
        for line in file_in:
            strL = line.rstrip()
            if len(strL) > 0:
                strL = re.sub('[^A-Za-z ]+', '', strL)
                stringLine.append(strL)

class ThreadedServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self, maxClient):
        self.sock.listen(maxClient)
        while True:
            client, address = self.sock.accept()
            print(address,"-","ket noi!",client)
            indif.append(client)
            addressl.append(address)
            if len(indif) >1 :
                threading.Thread(target=self.listenToWorker,args=(indif[0], addressl[0],"map")).start()
                threading.Thread(target=self.sendMsgToWorker,args=(indif[0],"map")).start()
                threading.Thread(target=self.sendMsgToWorker,args=(indif[1],"reduce")).start()
                threading.Thread(target=self.listenToWorker,args=(indif[1], addressl[1],"reduce")).start()

    def listenToWorker(self, client, address, typeW):
        if typeW == "map":
            while True:
                data = client.recv(1024)
                if data != b'':
                    now = datetime.now()
                    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
                    data = str(data,"utf-8")
                    listMap.append(data)
                    print(typeW,"-",date_time,"-",address,"-",str(base64.b64decode(data),"utf-8"))
        else:
            while True:
                data = client.recv(1024)
                if data != b'':
                    now = datetime.now()
                    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
                    data = str(data,"utf-8")
                    str_decode64 = base64.b64decode(data)
                    print(typeW,"-",date_time,"-",address,"-",str(str_decode64,"utf-8"))
        
    def sendMsgToWorker(self,client,typeW):
        if typeW == "map":
            for strl in stringLine :
                encodSender = base64.b64encode(bytes(strl, "utf-8"))
                client.send(bytes(str(encodSender,"utf-8"), 'utf-8'))
                time.sleep(1)
        else:
            while True:
                if len(listMap) > 0:
                    encodSender = listMap.pop()
                    client.send(bytes(encodSender, 'utf-8'))
                time.sleep(1)

if __name__ == "__main__":
    loadingData()
    ThreadedServer(socket.gethostname(), 9999).listen(3)
