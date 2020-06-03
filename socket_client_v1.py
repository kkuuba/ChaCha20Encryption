import cv2
import socket
import pickle
import struct
import chacha_ciphering
import base64
import numpy as np

key = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
nonce = '000000000000004a00000000'
counter = 1
cipher = chacha_ciphering.ChaCha20(key, nonce, counter)


# Here could be class SocketClient with all proper methods
def send_frame(socket_object, frame_to_send):
    """
    Send frame over socket client connection.

    :param socket_object: object of socket class
    :param frame_to_send: frame from VideoCapture
    :return: None
    """
    data_to_send = pickle.dumps(frame_to_send)
    message_size = struct.pack("L", len(data_to_send))
    socket_object.sendall(message_size + data_to_send)


ip_address = "127.0.0.1"
port = 4444
# Here could be 0 instead of "small.mp4" if using your webcam
cap = cv2.VideoCapture("big.mp4")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, port))
while True:
    ret, frame = cap.read()
    frame = cv2.imencode('.jpg', frame)[1]
    data = pickle.dumps(frame)
    plaintext = str(data)
    print("Encryption")
    frame = cipher.encryption(plaintext)
    send_frame(client_socket, frame)
