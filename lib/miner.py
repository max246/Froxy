from subprocess import *
import shlex
import socket



class Miner(object):
    _port = 0
    _command = []
    _api_host = "127.0.0.1"
    _api_host = 4048


    def __init__(self,api_host,api_port):
        self._command = shlex.split("aa")
        self._api_host = api_host
        self._api_port = api_port

    def start(self):
        #if win:
        self._handle = Popen(self._command, stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=False)
        print self._handle.stderr.readline()

    def stop(self):
        self._handle.pid #kill


    def download(self):
        print "downloading...s"

    def get_status_api(self):
        print "api"

    def do_socket_cmd(self,cmd):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self._api_host, self._api_port))
        s.send(cmd)
        data = s.recv(1024)
        s.close()
        return  data

    def do_request_cmd(self,cmd):
        r = request.get("http://{}:{}/{}".format(self._api_host, self._api_port, cmd))
        return r.text


    def is_running(self):
        return True