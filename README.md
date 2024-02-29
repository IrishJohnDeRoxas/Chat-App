Flask Chat App
==============
    Socket.IO integration for Flask applications.

Installation
------------

You can install this package as usual with pip:

    pip install requirement.txt

Example
-------

```py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.event
def handle_message(message):
    emit('response', {'data': 'got it!'})

if __name__ == '__main__':
    socketio.run(app)
```
