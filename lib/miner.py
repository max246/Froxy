from subprocess import *
import shlex
import socket
import requests
import threading
import datetime
import time


class Miner(object):
    _port = 0
    _command = []
    _command_benchmark = []
    _api_host = "127.0.0.1"
    _api_host = 4048


    def __init__(self,api_host,api_port):
        self._api_host = api_host
        self._api_port = api_port

    def start(self,benchmark=False):
        #if win:
        self._handle = Popen(self._command_benchmark if benchmark else self._command, stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=False)

    def read(self):
        return self._handle.stdout.readline()

    def stop(self):
        self._handle.pid #kill


    def download(self):
        print "downloading...s"

    def get_status_api(self):
        print "api"

    def do_socket_cmd(self,cmd):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self._api_host, self._api_port))
            s.send(cmd)
            data = s.recv(1024)
            s.close()
            return  data
        except:
            return None

    def do_request_cmd(self,cmd):
        try:
            r = requests.get("http://{}:{}/{}".format(self._api_host, self._api_port, cmd))
            return r.text
        except requests.exceptions.RequestException as e:
            if str(e).find("bye") > 0:
                return True
            else:
                return None


    def is_running(self):
        return True

    def get_name(self):
        return "miner class"



class MinerThread(threading.Thread):

    def __init__(self, miner):
        super(MinerThread, self).__init__()

        self._doRun = True
        self._miner = miner
        filename = datetime.datetime.now()

        self._log = open("log/miner_{}_{}.txt".format(self._miner.get_name(),filename),"w")

    def run(self):
        while self._doRun:
            output = self._miner.read()
            if len(output) > 0:
                self._log.write("{}".format(output))
                self._log.flush()
                time.sleep(0.1)

    def stop(self):
        self._doRun = False

