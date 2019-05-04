from Config import Config
import socket
import sys
import numpy as np
import cv2
import json
from threading import Thread

def receive():
    config = Config()
    # 初始化连接信息
    host = config.get("server", "host")
    port = config.get("server", "img_port")
    address = (host, int(port))


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)

    bfsize = 46080
    chuncksize = 46081
    frame = np.zeros(bfsize * 20, dtype=np.uint8)
    cnt = 0

    while True:
        #print("server\n")
        # start = time.time()#用于计算帧率信息
        cnt += 1
        data, addr = sock.recvfrom(chuncksize)
        frame_array = np.frombuffer(data, dtype=np.uint8)
        img = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)
        #print(img)
        #cv2.imshow("receive_frame", img)
        # i = int.from_bytes(data[-1:], byteorder='big')
        # line_data = numpy.frombuffer(data[:-1], dtype=numpy.uint8)
        # frame[i * 46080:(i + 1) * 46080] = line_data
        # if cnt == 20:
        #     cv2.imshow("frame", frame.reshape(480, 640, 3))
        #     cnt = 0
        #
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

def receive2():
    config = Config()
    # 初始化连接信息
    host = config.get("server", "host")
    port = config.get("server", "res_port")
    address = (host, int(port))


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(address)
    sock.listen(2)
    conn, addr = sock.accept()

    bfsize = 46080
    chuncksize = 46081
    frame = np.zeros(bfsize * 20, dtype=np.uint8)
    cnt = 0

    while True:
        #print("server\n")
        # start = time.time()#用于计算帧率信息
        b_data = conn.recv(bfsize)
        data = str(b_data,encoding="utf-8")
        res = json.loads(data)
        #print(res)
        #print("receive res : window_name :"+res['video_idx']+" time:"+res['time']+" result"+res['people_num']+"\n")

if __name__ == '__main__':
    th1 = Thread(target=receive)
    th2 = Thread(target=receive2)
    th1.start()
    th2.start()