import socket
import threading


class WebCamClient:
    """Class to get frames from webcam server"""

    def __init__(self):
        self.frame = None
        self.thread = None
        self.thread = threading.Thread(
            target=self.get_frames_from_server, args=())
        self.thread.daemon = True
        self.thread.start()  # start get_frames_from_server() method in background thread

    def get_frames_from_server(self):
        # TODO Add some exceptions to make this more stable
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect(("127.0.0.1", 4444))
        while True:
            self.frame = s.recv()
            print(self.frame)

    def get_frame(self):
        return self.frame
