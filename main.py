import ConfigParser
import time
import liblo
import json
import sys


from codes.froxy import *


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




config = ConfigParser.ConfigParser()
config.read("froxy.conf")

filename_miner = ( "config/miner_linux.conf" if config.get("main","os") == "linux" else "config/miner_win.conf" )

froxy = Froxy(config, filename_miner)
froxy.prepare_miners()


def list_miner(path,args):

    output = froxy.get_miners()

    print output
    liblo.send(target,"/web/miner/list",json.dumps(output))

def get_status(path,args):
    print path, args
    output = ""
    #if miner.get_status_api():
    #    output = miner.get_summary()
    #liblo.send(target,"/web/miner/status",output)

def stop_miner(path,args):
    print "stop"

def start_miner(path,args):
    print "start"



server.add_method("/miner/list", '', list_miner)
server.add_method("/miner/status", 'i', get_status)
server.add_method("/miner/stop", 'i', stop_miner)
server.add_method("/miner/start", 'i', start_miner)

froxy.start_miner()


while True:
    server.recv(100)

