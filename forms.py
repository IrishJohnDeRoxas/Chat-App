from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired, NumberRange, ValidationError

class UserSignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1,max=255)])
    password = PasswordField('Password', validators=[InputRequired(),
                                                     Length(min=8, max=100),
                                                     EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(18, message='Should be legal age')])
    submit = SubmitField('Submit')
    
class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')
    
    # def validate_username(self, username):
    #     username_exist = UserModel.query.filter_by(username=username).first()
    #     if username_exist:
    #         raise ValidationError('Username Already exist')
    
class SendMsgForm(FlaskForm):
    msg = StringField('Aa')
    send = SubmitField('Send')

class CreateRoomForm(FlaskForm):
    room_name = StringField('Room Name:', validators=[DataRequired(), Length(1,40)])
    submit = SubmitField('Create Room')
    