from flask import Blueprint, render_template, redirect, url_for, flash
from forms import UserLoginForm, UserSignUpForm, SendMsgForm, CreateRoomForm
from models import db, UserModel, RoomModel, RoomMsgModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_caching import Cache

main = Blueprint('main', __name__)
cache = Cache(config={'CACHE_TYPE': 'simple'})

@main.route('/')
def index():
    return redirect('/login')
    
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        username_exist = UserModel.query.filter_by(username = username).first()
        if username_exist:
            hashed_password = username_exist.hashed_password
            
            if check_password_hash(hashed_password, password):
                login_user(username_exist)
                if cache.get('cached_id'):                        
                    return redirect(url_for('main.dashboard', id=cache.get('cached_id')))
                else:
                    return redirect(url_for('main.dashboard', id=0))
                    
            else:
                flash('Incorrect username or password', 'info')
        
    return render_template('login.html', 
                           form=form)

@main.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    form = UserSignUpForm()
    username_exist = UserModel.query.filter_by(username=form.username.data).first()
    
    if form.validate_on_submit():
        if not username_exist:
            hashed_password = generate_password_hash(form.password.data)            
            user_entry = UserModel(first_name = form.first_name.data,
                                last_name = form.last_name.data,
                                age = form.age.data,
                                username = form.username.data,
                                hashed_password = hashed_password)
            
            form.first_name.data = ''
            form.last_name.data = ''
            form.age.data = ''
            form.username.data = ''
            form.password.data = ''
            
            db.session.add(user_entry)
            db.session.commit()
            
            flash('Sign up successful','success')
            return redirect(url_for('login'))

    elif username_exist:
        username_error = {'warning' : 'Username Already Taken' }
        return render_template('sign_up.html', 
                                form=form, 
                                username_error=username_error)

    return render_template('sign_up.html', 
                           form=form)

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = SendMsgForm()
    return render_template('home.html', 
                           form=form,
                           username=current_user.username)
    
@main.route('/chat/<id>', methods=['GET', 'POST'])
@login_required
def dashboard(id):
    cache.set('cached_id', id)
    create_room_form = CreateRoomForm()
    send_msg_form = SendMsgForm()
    if create_room_form.validate_on_submit():
        new_room = RoomModel(room_name = create_room_form.room_name.data, 
                             owner = current_user.username)
        db.session.add(new_room)
        db.session.commit()
        create_room_form.room_name.data = ''
        flash('Created a room', 'success')
    rooms = RoomModel.query.all()
    room_msg = RoomMsgModel.query.filter_by(room_id=id)
    return render_template('dashboard.html',
                           create_room_form = create_room_form,
                           send_msg_form = send_msg_form,
                           rooms=rooms,
                           room_msg=room_msg)

@main.route("/logout")   
@login_required
def logout():
    # id = current_user.get_id()
    # print(id)
    logout_user()
    flash('Logged out', 'success')
    return redirect(url_for('main.index'))
