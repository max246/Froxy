import threading
import liblo



class OSCThread(threading.Thread):

    def __init__(self, server, client, wsemit):
        super(OSCThread, self).__init__()

        self._doRun = True
        self._server = server
        self._client = client
        self._wsemit = wsemit

    def run(self):
        while self._doRun:
            self._server.recv(100)
            #self._wsemit("aaa","aa")
    def stop(self):
        self._doRun = False

    def add_request(self,topic):
        liblo.send(self._client,topic)

    def add_request_data(self,topic,data):
        liblo.send(self._client,topic,data)

    def emit(self,topic,data):
        print "Emit"#emit(topic,data)