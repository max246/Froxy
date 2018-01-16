from lib.miner import *
import re


#./cpuminer  -a scrypt  -o stratum+tcp://litecoinpool.org:3333 -u max246.1 -p 1  --api-bind 127.0.0.1:4048 --api-remote

class CPUMiner(Miner):
    _algo = ""
    _version = "3.7.10"
    _cpus = 0
    _hashrate = 0
    _accept = 0
    _reject = 0
    _difficulty = 0
    _temprature = 0
    _fan_speed = 0
    _frequency = 0
    _uptime = 0

    def __init__(self, api_host, api_port):
        super(CPUMiner, self).__init__(api_host, api_port)

    def get_status_api(self):
        #/summary  NAME=cpuminer-opt;VER=3.7.10;API=1.0;ALGO=scrypt;CPUS=4;KHS=0.00;ACC=0;REJ=0;ACCMN=0.000;DIFF=3564823.186406;TEMP=57.0;FAN=0;FREQ=0;UPTIME=8;TS=1516143339|
        #/threads
        #/seturl
        #/quit
        #/help
        data = self.do_socket_cmd("summary")
        #print data
        self.parse_summary(data)

    def parse_summary(self,data):
        out = re.findall( r'(\w+)=(.*?)\;', data)
        for line in out:
            if line[0] == "ALGO":
                self._algo = line[1]
            elif line[0] == "VER":
                self._version = line[1]
            elif line[0] == "CPUS":
                self._cpus = line[1]
            elif line[0] == "KHS":
                self._hashrate = line[1]
            elif line[0] == "ACC":
                self._accept = line[1]
            elif line[0] == "REJ":
                self._reject = line[1]
            elif line[0] == "DIFF":
                self._difficulty = line[1]
            elif line[0] == "TEMP":
                self._temprature = line[1]
            elif line[0] == "FAN":
                self._fan_speed = line[1]
            elif line[0] == "FREQ":
                self._frequency = line[1]
            elif line[0] == "UPTIME":
                self._uptime = line[1]

    def print_summary(self):
        print "ALGO:{} VER:{} CPUS:{} KHS:{} TEMP:{}".format(self._algo,self._version,self._cpus,self._hashrate,self._temprature)



