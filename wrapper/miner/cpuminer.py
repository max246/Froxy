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

    def __init__(self, data, pool):
        super(CPUMiner, self).__init__(data["api_host"], int(data["api_port"]))

        self._name = pool.get_miner_name()

        args = data["args"]
        args = args.replace("$USERNAME", pool.get_username())
        args = args.replace("$SCHEME", pool.get_scheme())
        args = args.replace("$POOL",  pool.get_pool())
        args = args.replace("$PASSWORD", pool.get_password())
        args = args.replace("$ALGO", pool.get_algorithm())
        args = args.replace("$APIPORT", str(data["api_port"]))
        args = args.replace("$APIHOST", data["api_host"])

        args_bm = data["args_benchmark"]
        args_bm = args_bm.replace("$ALGO", pool.get_algorithm())
        args_bm = args_bm.replace("$APIPORT", str(data["api_port"]))
        args_bm = args_bm.replace("$APIHOST", data["api_host"])

        self._command = shlex.split("miner/{}/{} {}".format(data["path"],data["bin"], args))
        self._command_benchmark = shlex.split("miner/{}/{} {}".format(data["path"],data["bin"], args_bm))

        print args



    def get_status_api(self):
        #summary  NAME=cpuminer-opt;VER=3.7.10;API=1.0;ALGO=scrypt;CPUS=4;KHS=0.00;ACC=0;REJ=0;ACCMN=0.000;DIFF=3564823.186406;TEMP=57.0;FAN=0;FREQ=0;UPTIME=8;TS=1516143339|
        #threads
        #seturl
        #quit
        #help
        data = self.do_socket_cmd("summary")
        if data:
            self.parse_summary(data)
            return True
        else:
            return None

    def stop(self):
        self.do_request_cmd("quit")
        #check PID that is killed

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

    def get_summary(self):
        return  "ALGO:{} VER:{} CPUS:{} KHS:{} TEMP:{}".format(self._algo,self._version,self._cpus,self._hashrate,self._temprature)

    def get_hashrate(self):
        return float(self._hashrate)*1000.0





