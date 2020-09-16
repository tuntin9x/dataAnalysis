#!/usr/bin/python3
import socket          
import threading
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
            # print("Da co client ket noi!")
            # msg = 'Thank you for connecting'+ "\r\n"
            # client.send(msg.encode('ascii'))
            threading.Thread(target=self.listenToClient,args=(client, address)).start()

    def listenToClient(self, client, address):
        recvBuf = ''
        while True:
            data = self.recvLine(client, recvBuf)
            print (data)

    def recvLine(self, client, recvBuf):  # receive line from client
        while '\n' not in recvBuf:
            try:
                data = client.recv(1024)
                if data:
                    recvBuf += data
                # else:
                #     return [False, 'disconnected']
            except:
                client.close()
                return [False, 'error']
        lineEnd = recvBuf.index('\n')
        data = recvBuf[:lineEnd]
        recvBuf = recvBuf[lineEnd+1:]
        return data
if __name__ == "__main__":
    ThreadedServer(socket.gethostname(), 9999).listen(50)