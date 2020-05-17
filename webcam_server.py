import socket
import json
from time import sleep
from webcam_services import WebCam


class SocketServer:
    """Socket server class with symmetric ciphering"""

    def __init__(self, port, ip_address=""):
        """
        Create object which represent server instance with all default parameters. Also it bind local IP address of
        device and start listening to defined port.

        :param port: listening port of device
        :param ip_address: interface ip address which will be bind to socket
        """
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ip_address = ip_address
        self.port = int(port)
        self.connection = None
        self.remote_con_params = ""
        self.sock.bind((self.ip_address, self.port))
        self.sock.listen(3)

    def __del__(self):
        self.close_connection()

    def send_data(self, byte_data):
        """
        Send via socket connection.

        :param dictionary: input data to send through connection
        :return: None
        """
        self.connection.send(byte_data)

    def rcv_data(self):
        """
        Receive data via socket connection.

        :return: output data in dictionary format
        """
        return self.connection.recv(4096)

    def accept_remote_handshake(self):
        """
        Accept remote connection on socket side.

        :return: None
        """
        if self.connection:
            self.close_connection()
        self.connection, self.remote_con_params = self.sock.accept()
        print("Connection from %s on port %d \n" %
              (self.remote_con_params[0], self.remote_con_params[1]))

    def close_connection(self):
        """
        Close connection with checking if client is actually connected.

        :return:
        """
        if self.connection:
            self.connection.close()
        elif self.sock:
            self.sock.close()


server = SocketServer(4444)
while True:
    print("Waiting for connection ... \n")
    server.accept_remote_handshake()
    webcam = WebCam()
    sleep(2)
    frame = webcam.get_frame()
    while True:
        frame_to_send = webcam.get_frame()
        # TODO here should be code to encrypt this frame with chacha20 encryption class
        server.send_data(frame_to_send)
        # it will be throwing frames to connection until we Ctrl-C script
