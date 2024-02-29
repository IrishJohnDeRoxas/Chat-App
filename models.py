from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()

class UserModel(db.Model, UserMixin):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(255), nullable=False)
    hashed_password = db.Column(db.TEXT(), nullable=False)
    first_name = db.Column(db.TEXT(), nullable=False)
    last_name = db.Column(db.TEXT(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    @property
    def password(self):
        raise AttributeError('Password is not readable')

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hashed_password, password)
class RoomModel(db.Model):
    __tablename__ = 'room' 
    room_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_name = db.Column(db.VARCHAR(255), nullable=False)
    owner = db.Column(db.TEXT(), nullable=False)
    messages = db.relationship("RoomMsgModel", backref="room")  # One-to-Many

class RoomMsgModel(db.Model):
    __tablename__ = 'room_messages'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey("room.room_id"))
    sender = db.Column(db.TEXT(), nullable=False)
    message = db.Column(db.TEXT(), nullable=False)