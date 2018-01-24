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

@socketio.on('miners', namespace='/froxy')
def test_message():
    thread.add_request("/miner/list")
    print "event"

@socketio.on('status', namespace='/froxy')
def status(msg):
    thread.add_request_data("/miner/status",int(msg['data']))
    print "event"

@socketio.on('connect', namespace='/froxy')
def test_connect():
    #liblo.send(target, "/miner/list")
    print "connect"
    #emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/froxy')
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
    socketio.emit('miner_list',{'data': args[0]}, namespace='/froxy')


def get_status(path,args):
    print args
    socketio.emit('miner_status',{'data': args[0]}, namespace='/froxy')

server.add_method("/web/miner/list", 's', list_miner)
server.add_method("/web/miner/status", 's', get_status)

#liblo.send(target,"/miner/list")
#liblo.send(target,"/miner/status",0)


thread = OSCThread(server,target,emit)
thread.setDaemon(True)
thread.start()

if __name__ == '__main__':
    socketio.run(app)