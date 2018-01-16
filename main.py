from wrapper.miner.cpuminer import *

miner = CPUMiner("127.0.0.1", 4048)
miner.get_status_api()
miner.print_summary()