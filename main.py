import ConfigParser
import time
import liblo
import json
import sys

from wrapper.miner.cpuminer import *
from wrapper.minerhelper import *

miners = []

try:
    server = liblo.Server(12345)
except liblo.ServerError, err:
    print str(err)
    sys.exit()

try:
    target = liblo.Address(12346)
except liblo.AddressError, err:
    print str(err)
    sys.exit()

def cb_failure(miner):
    print "miner failed"

config = ConfigParser.ConfigParser()
config.read("froxy.conf")

filename_miner = ( "config/miner_linux.conf" if config.get("main","os") == "linux" else "config/miner_win.conf" )
doBenchmark = config.getboolean("main","benchamrk")

m = MinerHelper(filename_miner,"CPU")
if m.init():
    print "found miner ",m.get_pool().get_miner_name()
    miner = m.get_miner()
    miners.append(miner)
    miner.start(benchmark=doBenchmark)

    thread_m = MinerThread(miner,cb_failure)
    thread_m.setDaemon(True)
    thread_m.start()

    '''
    for i in range(4400000):
        if miner.get_status_api():
            miner.print_summary()
        else:
            print "failed connecto to api"
        time.sleep(0.4)
    time.sleep(2)
    '''
else:
    print "* Couldnt find miner ", m.get_pool_type()
'''
config = ConfigParser.ConfigParser()
config.read("miner_linux.conf")
#print config.sections()

bin =  config.get("CPUMinerOPT-4WAY","bin")
args =  config.get("CPUMinerOPT-4WAY","args")
api_host = config.get("CPUMinerOPT-4WAY","api_host")
api_port = config.getint("CPUMinerOPT-4WAY","api_port")
folder = config.get("CPUMinerOPT-4WAY","path")
bin = config.get("CPUMinerOPT-4WAY","bin")
args = config.get("CPUMinerOPT-4WAY","args")
username = config.get("CPUMinerOPT-4WAY","username")
password = config.get("CPUMinerOPT-4WAY","password")
pool = config.get("CPUMinerOPT-4WAY","pool")
scheme = config.get("CPUMinerOPT-4WAY","scheme")

algo = "scrypt"


miner = CPUMiner(config,"CPUMinerOPT-4WAY")
miner = CPUMiner(api_host,api_port, folder, bin, args, algo, username, password,  scheme,pool)
miner.start()
time.sleep(5)
miner.get_status_api()
miner.print_summary()
time.sleep(5)
miner.stop()
'''

def list_miner(path,args):
    output = {}
    output["miner"] = []
    i = 0
    print output
    for miner in miners:
        output["miner"].append({"type" : miner.get_name() , "id" : i})
        i += 1
    print output
    liblo.send(target,"/web/miner/list",json.dumps(output))

def get_status(path,args):
    print path, args
    output = ""
    if miner.get_status_api():
        output = miner.get_summary()
    liblo.send(target,"/web/miner/status",output)

def stop_miner(path,args):
    print "stop"

def start_miner(path,args):
    print "start"



server.add_method("/miner/list", '', list_miner)
server.add_method("/miner/status", 'i', get_status)
server.add_method("/miner/stop", 'i', stop_miner)
server.add_method("/miner/start", 'i', start_miner)


while True:
    server.recv(100)

thread_m.stop()
miner.stop()