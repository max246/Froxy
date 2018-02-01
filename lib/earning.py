import requests


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
    MONTH = DAY * 30

    def __init__(self):
        self._coins = {}
        self._url = "https://whattomine.com/coins.json"
        self.update_coins()


    def update_coins(self):
        r = requests.get(self._url)
        if r.status_code == 200:
            coins = r.json()["coins"]
            for coin in coins:
                self._coins[coin] = {}
                for value in coins[coin]:
                    self._coins[coin][value] = coins[coin][value]

    def get_coins(self):
        coins = []
        for coin in self._coins:
            coins.append(coin)
        return coins

    def select_coin(self,coin):
        if coin in self._coins:
            self.pull_coin(coin)
            return True
        else:
            return False

    def pull_coin(self,coin):
        self.update_coins()
        data = self._coins[coin]

        self._difficulty = data["difficulty24"]
        self._block_time = float(data["block_time"])
        self._network_hash = self._difficulty / self._block_time
        self._block_reward = data["block_reward"]
        self._block_per_minute = 60.0 / self._block_time
        self._coin_per_minute = self._block_per_minute * self._block_reward

    def calculate(self,hashrate, time=HOUR):
        user_ratio = hashrate / self._network_hash
        return user_ratio * self._coin_per_minute * time




#a = Earning()
#print a.select_coin("Electroneum")
#print a.calculate(55, Earning.DAY)
#print a.get_coins()
