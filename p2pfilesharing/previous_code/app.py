#!/usr/bin/python3


#imports
from flask import Flask, session, redirect, request, render_template
from flask_session import Session
from flask_socketio import SocketIO
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, initialise, add_user, check_username_password_hash

#initialise the flask module
app = Flask(__name__)

#nsure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOADED"] = True

#Ensure responses are not cached!
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-chache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#configure app session to use filesystem
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#initialising socketio
socketio = SocketIO(app)

#declaring routes
@app.route('/')
def index():
    initialise()
    return redirect('/register')
@app.route('/register', methods=['POST', 'GET'])

def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        add_user(Username=username, Hash=hashed_password)
        return f'<h1>Added user {username}<h1>'
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        hashed_password = check_username_password_hash(Username=username)
        plain_password = request.form['password']
        if hashed_password:
            for hash in hashed_password:
                if not check_password_hash(hash, plain_password):
                    continue
                else:
                    break
            return redirect('/message')
        else:
            return 'There aint no user with that password bro'

@app.route('/message', methods=['POST', 'GET'])
def message():
    if request.metod=='GET':
        return render_template('messaging.html')
    else:
        pass

if __name__ == '__main__':
    app.run()

