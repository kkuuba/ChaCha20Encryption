from flask import Flask, render_template, Response
from web_solution.webcam_client import WebCamClient

app = Flask(__name__)
camera = WebCamClient()
# TODO add some REST methods to save secret key
@app.route('/')
def index():
    """Video streaming home page."""
    
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
