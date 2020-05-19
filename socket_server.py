import pickle
import socket
import struct
import cv2


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
        self.data = b''
        self.payload_size = struct.calcsize("L")

    def __del__(self):
        self.close_connection()

    def rcv_frame(self):
        """
        Receive data via socket connection.

        :return: output data in dictionary format
        """

        # Retrieve message size
        while len(self.data) < self.payload_size:
            self.data += self.connection.recv(4096)

        packed_msg_size = self.data[:self.payload_size]
        self.data = self.data[self.payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        # Retrieve all data based on message size
        while len(self.data) < msg_size:
            self.data += self.connection.recv(4096)

        frame_data = self.data[:msg_size]
        self.data = self.data[msg_size:]

        # Extract frame
        return pickle.loads(frame_data)

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
    while True:
        frame = server.rcv_frame()
        # Here should be implemented decryption of frame
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
