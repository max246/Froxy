import liblo
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from lib.osc import  *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,async_mode='threading')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join', namespace='/test')
def test_message(sss):
    thread.add_request_data("/miner/status",0)
    print "event"

@socketio.on('connect', namespace='/test')
def test_connect():
    #liblo.send(target, "/miner/list")
    print "connect"
    #emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

try:
    server = liblo.Server(12346)
except liblo.ServerError, err:
    print str(err)
    sys.exit()

try:
    target = liblo.Address(12345)
except liblo.AddressError, err:
    print str(err)
    sys.exit()



def list_miner(path,args):
    print args
    socketio.emit('my_response',{'data': args[0]}, namespace='/test')


def get_status(path,args):
    print args
    socketio.emit('my_response',{'data': args[0]}, namespace='/test')

server.add_method("/web/miner/list", 's', list_miner)
server.add_method("/web/miner/status", 's', get_status)

#liblo.send(target,"/miner/list")
#liblo.send(target,"/miner/status",0)


thread = OSCThread(server,target,emit)
thread.setDaemon(True)
thread.start()

if __name__ == '__main__':
    socketio.run(app)