import socket, sys, time
class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))
        print("Connection made on {}:{}".format(host, port))

    def send(self, msg):
        sent = self.sock.send(bytes(str(msg), encoding="utf8"))
#            print("Message sent: {}".format(msg[totalsent:]))
        if sent == 0:
            raise RuntimeError("socket connection broken")

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
    
    def close(self):
        self.sock.close()


if __name__ == '__main__':
    s=MySocket()
    s.connect(host="192.168.192.31", port=1223)
    for j in range(10):
        s.send([i for i in range(10)])
        time.sleep(0.1)