from flask import *
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'nucle benis'
socketio = SocketIO(app)

@app.route('/')
def index():
    print("hit index")
    return current_app.send_static_file('index.html')

def send_fen(fen):
    emit('fen', {'data': fen}, broadcast=True)