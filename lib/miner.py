from subprocess import *



class Miner:
    _port = 0
    _command = []
    

    def __init__(self):
        self._command = shlex.split("aa")

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

    def is_running(self):
        return True