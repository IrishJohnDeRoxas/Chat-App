Flask Chat App
==============
    Socket.IO integration for Flask applications.

Installation
------------

You can install this package as usual with pip:

    pip install requirements.txt

Set up the database by running the sql file in Mysql Workbench:

    Run the flask_chat_app.sql to create the database

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
