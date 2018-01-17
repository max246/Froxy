import ConfigParser
import time
import liblo
from wrapper.miner.cpuminer import *

config = ConfigParser.ConfigParser()
config.read("miner_linux.conf")
#print config.sections()

bin =  config.get("CPUMinerOPT-4WAY","bin")
args =  config.get("CPUMinerOPT-4WAY","args")
api_host = config.get("CPUMinerOPT-4WAY","api_host")
api_port = config.getint("CPUMinerOPT-4WAY","api_port")
folder = config.get("CPUMinerOPT-4WAY","path")
bin = config.get("CPUMinerOPT-4WAY","bin")
args = config.get("CPUMinerOPT-4WAY","args")
username = config.get("CPUMinerOPT-4WAY","username")
password = config.get("CPUMinerOPT-4WAY","password")
pool = config.get("CPUMinerOPT-4WAY","pool")
scheme = config.get("CPUMinerOPT-4WAY","scheme")

algo = "scrypt"

miner = CPUMiner(api_host,api_port, folder, bin, args, algo, username, password,  scheme,pool)
miner.start()
time.sleep(5)
miner.get_status_api()
miner.print_summary()
time.sleep(5)
miner.stop()