from lib.miner import *
import re



class EthDcrMiner64(Miner):

    dcri = [20,30,40]

    def __init__(self, data, pool):
        print data
        super(EthDcrMiner64, self).__init__(data["api_host"], int(data["api_port"]))

        self._name = pool.get_miner_name()
        args_e = data["args_e"]
        args_e = args_e.replace("$EPOOL",pool.get_pool())
        args_e = args_e.replace("$EUSERNAME", pool.get_username())
        args_e = args_e.replace("$EPASSWORD", pool.get_password())

        args = data["args"]
        args = args.replace("$APIPORT",data["api_host"])
        args = args.replace("$ALLCOINS",data["api_port"])

        args = "{} {}".format(args, args_e)

        args_bm = data["args_benchmark"]
        #args_bm = args_bm.replace("$ALGO", pool.get_coin())
        args_bm = args_bm.replace("$APIPORT", str(data["api_port"]))
        args_bm = args_bm.replace("$APIHOST", data["api_host"])

        self._command = shlex.split("miner/{}/{} {}".format(data["path"], data["bin"], args))
        self._command_benchmark = shlex.split("miner/{}/{} {}".format(data["path"], data["bin"], args_bm))

    def get_status_api(self):

        data = self.do_socket_cmd('{"id":0,"jsonrpc":"2.0","method":"miner_getstat1"}')

        self.parse_summary(data)
        #{"id":0,"jsonrpc":"2.0","method":"miner_getstat2"}
        '''
          
The following commands are available (JSON format):


----------------
REQUEST:
{"id":0,"jsonrpc":"2.0","method":"miner_getstat1"}

RESPONSE:
{"result": ["9.3 - ETH", "21", "182724;51;0", "30502;30457;30297;30481;30479;30505", "0;0;0", "off;off;off;off;off;off", "53;71;57;67;61;72;55;70;59;71;61;70", "eth-eu1.nanopool.org:9999", "0;0;0;0"]}
"9.3 - ETH"				- miner version.
"21"					- running time, in minutes.
"182724"				- total ETH hashrate in MH/s, number of ETH shares, number of ETH rejected shares.
"30502;30457;30297;30481;30479;30505"	- detailed ETH hashrate for all GPUs.
"0;0;0"					- total DCR hashrate in MH/s, number of DCR shares, number of DCR rejected shares.
"off;off;off;off;off;off"		- detailed DCR hashrate for all GPUs.
"53;71;57;67;61;72;55;70;59;71;61;70"	- Temperature and Fan speed(%) pairs for all GPUs.
"eth-eu1.nanopool.org:9999"		- current mining pool. For dual mode, there will be two pools here.
"0;0;0;0"				- number of ETH invalid shares, number of ETH pool switches, number of DCR invalid shares, number of DCR pool switches.

COMMENTS:
Gets current statistics.



----------------
REQUEST:
{"id":0,"jsonrpc":"2.0","method":"miner_getstat2"}

RESPONSE:
Same as "miner_getstat1" but also appends additional information:

- ETH accepted shares for every GPU.
- ETH rejected shares for every GPU.
- ETH invalid shares for every GPU.
- DCR accepted shares for every GPU.
- DCR rejected shares for every GPU.
- DCR invalid shares for every GPU.



----------------
REQUEST:

{"id":0,"jsonrpc":"2.0","method":"miner_restart"}

RESPONSE:
none.

COMMENTS:
Restarts miner.



----------------
REQUEST:
{"id":0,"jsonrpc":"2.0","method":"miner_reboot"}

RESPONSE:
none.

COMMENTS:
Calls "reboot.bat" for Windows, or "reboot.bash" (or "reboot.sh") for Linux.



----------------
REQUEST:
{"id":0,"jsonrpc":"2.0","method":"control_gpu", "params":[0, 1]}

RESPONSE:
none.

COMMENTS:
first number - GPU index, or "-1" for all GPUs. Second number - new GPU state, 0 - disabled, 1 - ETH-only mode, 2 - dual mode.

        '''


    def parse_summary(self,data):
        print "parse"
