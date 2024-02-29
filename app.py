from flask import Flask, request
from flask_login import LoginManager,current_user
from flask_socketio import SocketIO, disconnect, send
from dotenv import load_dotenv
from models import db, migrate, UserModel, RoomMsgModel
from routes import main, cache
import os, functools


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.app_context().push()
db.init_app(app)
migrate.init_app(app,db)
socketio = SocketIO(app, cors_allowed_origin='*')
cache.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))

app.register_blueprint(main)

if __name__ == '__main__':
    socketio.run(app, host='localhost')

def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

@socketio.on('message')
@authenticated_only
def handle_message(msg):
    id = cache.get('cached_id')
    if msg != 'User Connected!s':
        new_msg = RoomMsgModel(room_id = id, sender = current_user.username, message = msg)
        db.session.add(new_msg)
        db.session.commit()
        send({'user': current_user.username,
              'msg': msg,
              "room_id": id
            }, broadcast=True)
