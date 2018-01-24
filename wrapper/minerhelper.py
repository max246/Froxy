import ConfigParser
from model.pool import *
from wrapper.miner.cpuminer import *



class MinerHelper():


    def __init__(self, miner_config, pool_type):
        self._config_pool = ConfigParser.ConfigParser()
        self._config_pool.read("config/pool.conf")
        self._config_miner = ConfigParser.ConfigParser()
        self._config_miner.read(miner_config)

        self._pool_type = pool_type


    def init(self):
        # Populate the miner
        if self.find_pool(self._pool_type):
            return self.find_miner(self._pool.get_miner_name())
        else:
            return None


    def find_pool(self, type):
        data = {}
        if self._config_pool.has_section(type):
            options = self._config_pool.options(type)
            for option in options:
                data[option] = self._config_pool.get(type,option)

            self._pool = Pool(data)
            return True
        else:
            return None

    def get_pool(self):
        return self._pool

    def get_pool_type(self):
        return self._pool_type


    def find_miner(self,name):
        data = {}
        if self._config_miner.has_section(name):
            options = self._config_miner.options(name)
            for option in options:
                data[option] = self._config_miner.get(name,option)

            if name == "CPUMinerOPT-4WAY":
                self._miner = CPUMiner(data,self._pool)
            else:
                return None

            return True
        else:
            return None


    def get_miner(self):
        return self._miner




