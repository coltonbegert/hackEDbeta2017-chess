from flask import *
import threading
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'nucle benis'
socketio = SocketIO(app)

class Web(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        app.run()
    def update_board(self, fen):
        send_fen(fen)

@app.route('/')
def index():
    print("hit index")
    return current_app.send_static_file('index.html')

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

def send_fen(fen):
    print(fen)
    socketio.emit('fen', {'data': fen}, broadcast=True)

def flaskthread():
    app.run(host="0.0.0.0")


if __name__ == '__main__':
    app.run()
