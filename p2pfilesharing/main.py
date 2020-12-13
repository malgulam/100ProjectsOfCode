#Source code from: https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d
#written by: https://medium.com/u/7e65fabdea53?source=post_page-----f98de4adfa5d--------------------------------
#and:https://medium.com/u/4ce24554e1d2?source=post_page-----f98de4adfa5d--------------------------------

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)