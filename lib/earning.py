

class Earning:

    _network_hash = 0
    _block_per_minute = 0
    _block_reward = 0
    _difficulty = 0
    _block_time = 0
    _coin_per_minute = 0
    _block_per_minute = 0

    HOUR = 60
    DAY = 60 * 24
    WEEK = 60 * 24 * 7

    def __init__(self,difficulty,block_time,block_reward):
        self._network_hash = difficulty/block_time
        self._difficulty = difficulty
        self._block_time = block_time
        self._block_reward = block_reward
        self._block_per_minute = 60.0/block_time
        self._coin_per_minute = self._block_per_minute * block_reward

    def calculate(self,hashrate, time=HOUR):
        user_ratio = hashrate / self._network_hash
        return user_ratio * self._coin_per_minute * time



#a = Earning(17240277307812.700,14.0,10.0)
#print a.calculate(20000000)