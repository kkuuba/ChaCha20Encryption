import os
import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):

    def __init__(self):
        super(Camera, self).__init__()

    @staticmethod
    def frames():
        camera = cv2.VideoCapture("small.mp4") # Here will be 0 in webcam case
        if not camera.isOpened():
            raise RuntimeError('Could not start camera')

        while True:
            _, frame = camera.read()
            yield cv2.imencode('.jpg', frame)[1].tobytes()
