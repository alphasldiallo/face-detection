import cv2
from threading import Thread
import socket
import sys, time


# def main():
#     target_host = '172.20.10.2'
#     target_port = 1223
#
#     try:
#         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     except socket.error:
#         print('Could not create a socket')
#         time.sleep(1)
#         sys.exit()
#
#     try:
#         client.connect((target_host, target_port))
#     except socket.error:
#         print('Could not connect to server')
#         time.sleep(1)
#         sys.exit()
#
#     online = True
#     while online:
#         for i in range(10):
#             client.sendall(str(i).encode())
#             time.sleep(1)
# # start client
# main()

class ThreadedCamera(object):
    def __init__(self, source = 0):

        self.capture = cv2.VideoCapture(source)

        self.thread = Thread(target = self.update, args = ())
        self.thread.daemon = True
        self.thread.start()

        self.status = False
        self.frame  = None

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def grab_frame(self):
        if self.status:
            return self.frame
        return None


if __name__ == '__main__':
    host = "172.20.10.2"
    port = 8090
    port2 = 1223
    stream_link = f"http://{host}:{port}"
    streamer = ThreadedCamera(stream_link)
    face_cascade = cv2.CascadeClassifier('haarcascade.xml')
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Could not create a socket')
        time.sleep(1)
        sys.exit()

    try:
        client.connect((host, port2))
    except socket.error:
        print('Could not connect to server')
        time.sleep(1)
        sys.exit()

    # start client
    while True:
        frame = streamer.grab_frame()
        if frame is not None:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                val = f"x={x} \t y={y} \t w={w} \t h={h}"
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                x_normalized = (((x/1280)*180)/2)*(-1)
                if x_normalized < -40 or x_normalized > -15:
                    client.sendall(str(x_normalized).encode())
                print(x_normalized)
                time.sleep(2)
            cv2.imshow("Context", frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    streamer.capture.release()
