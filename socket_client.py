import cv2
import socket
import pickle
import struct


# Here could be class SocketClient with all proper methods
def send_frame(socket_object, frame_to_send):
    """
    Send frame over socket client connection.

    :param socket_object: object of socket class
    :param frame_to_send: frame from VideoCapture
    :return: None
    """
    data = pickle.dumps(frame_to_send)
    message_size = struct.pack("L", len(data))
    socket_object.sendall(message_size + data)


ip_address = "127.0.0.1"
port = 4444
# Here could be 0 instead of "small.mp4" if using your webcam
cap = cv2.VideoCapture("small.mp4")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, port))

while True:
    ret, frame = cap.read()
    # Here should be implemented encryption of frame
    send_frame(client_socket, frame)
