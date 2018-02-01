import ConfigParser
from wrapper.miner.cpuminer import *
from wrapper.minerhelper import *
from lib.earning import  *


class Froxy:
    AMD = "AMD"
    NVIDIA = "NVIDIA"
    CPU = "CPU"

    _miners = []

    def __init__(self, config, filename_miner):
        self._filename_miner = filename_miner
        self._doBenchmark = config.getboolean("main","benchamrk")
        self._enableAMD = config.getboolean("arch",self.AMD)
        self._enableNVIDIA = config.getboolean("arch", self.NVIDIA)
        self._enableCPU = config.getboolean("arch", self.CPU)

        self._earning = Earning()
        self._earning.select_coin("Electroneum")

    def cb_failure(self,miner):
        print "miner failed"

    def cb_benchmark(self, miner):
        self._earning.select_coin("Electroneum")
        coins = self._earning.calculate(miner.get_hashrate())
        print "** Benchmark over **"
        print "Miner: {}  Hashrate: {}".format(miner.get_name(), miner.get_hashrate())
        print "Earning over a day: {}".format(coins)

    def check_arch_enable(self, arch):
        if arch == self.AMD:
            return self._enableAMD
        elif arch == self.NVIDIA:
            return self._enableNVIDIA
        elif arch == self.CPU:
            return self._enableCPU
        else:
            return False

    def prepare_miners(self):
        config =ConfigParser.ConfigParser()
        config.read(self._filename_miner)
        for name in config.sections():
            if config.getboolean(name,"enable") and self.check_arch_enable(config.get(name, "type")):#Create miner only if set to enable
                self.create_miner(name)


    def create_miner(self, name):
        config = ConfigParser.ConfigParser()
        config.read("config/pool.conf")
        for pool in config.sections():
            if config.get(pool,"miner") == name:
                helper = MinerHelper(self._filename_miner, pool)
                if helper.init():
                    self._miners.append(helper.get_miner())


    def start_miner(self):
        miner = self._miners[0]
        miner.start(benchmark=self._doBenchmark )

        thread_m = MinerThread(miner, self.cb_failure, self.cb_benchmark)
        thread_m.setDaemon(True)
        thread_m.start()
        print "Benchmark started!"
        '''
        for i in range(4400000):
            if miner.get_status_api():
                miner.print_summary()
            else:
                print "failed connecto to api"
            time.sleep(0.4)
        time.sleep(2)
        '''

    def get_miners(self):
        output = {}
        output["miner"] = []
        i = 0
        for miner in self._miners:
            output["miner"].append({"type": miner.get_name(), "id": i})
            i += 1
