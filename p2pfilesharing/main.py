# Source code from: https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d
# written by: https://medium.com/u/7e65fabdea53?source=post_page-----f98de4adfa5d--------------------------------
# and:https://medium.com/u/4ce24554e1d2?source=post_page-----f98de4adfa5d--------------------------------
# modified by: github.com/malimba


import os
from pathlib import Path

from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__)
# configure secret key
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
# configure file to  work with uploaded files into UPLOAD_FOLDER
base_dir = str(Path.home())
UPLOAD_FOLDER = f'{base_dir}/Desktop'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
socketio = SocketIO(app)


# methods
def allowed_file(filename):
    # next time I'll use path.splitext
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def sessions():
    return render_template('session.html')


@app.route('/upload')
def upload():
    return render_template('uploader.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return 'file uploaded successfully'


@app.route('/all_files')
def all_files():
    pwd_contents = os.listdir(app.config['UPLOAD_FOLDER'])
    return f'Files on server: <p>{pwd_contents}</p><h1><b>To download the file ' \
           f'do:https://localhost:port/download/filename<b></h1> '


@app.route('/download/<path:path>')
def get_file(path):
    """Download the file"""
    return send_from_directory(UPLOAD_FOLDER, path, as_attachment=True)


def messageReceived(methods=None):
    if methods is None:
        pass
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=None):
    if methods is None:
        pass
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
