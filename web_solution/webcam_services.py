import os
import cv2
from time import sleep
import threading


class WebCam:
    """Class to get frames from webcam"""

    def __init__(self):
        self.frames = []
        self.thread = None
        # Here will be 0 in webcam case
        self.camera = cv2.VideoCapture("small.mp4")
        if not self.camera.isOpened():
            raise RuntimeError('Could not start camera')
        self.thread = threading.Thread(target=self.emualate, args=())
        self.thread.daemon = True
        self.thread.start()  # start emulate() method in background thread

    def emualate(self):
        """Get frames from webcam or from file an countinously put them in frames list"""
        # TODO Add some exceptions to make this more stable
        while True:
            _, frame = self.camera.read()
            sleep(0.3)  # comment this in case of using webcam
            self.frames.append(cv2.imencode('.jpg', frame)[1].tobytes())
            print(len(self.frames))

    def get_frame(self):
        print(len(self.frames[-1]))
        return self.frames[-1]
