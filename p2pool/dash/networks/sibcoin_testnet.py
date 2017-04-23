import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'cee2caff'.decode('hex')
P2P_PORT = 11945
ADDRESS_VERSION = 125
SCRIPT_ADDRESS_VERSION = 100
RPC_PORT = 11944
RPC_CHECK = defer.inlineCallbacks(lambda dashd: defer.returnValue(
            'sibcoinaddress' in (yield dashd.rpc_help()) and
            (yield dashd.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('x11_gost_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('x11_gost_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'tSIB'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'DashCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/DashCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.dashcore'), 'dash.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://testchain.sibcoin.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://testchain.sibcoin.net/address/'
TX_EXPLORER_URL_PREFIX = 'https://testchain.sibcoin.net/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**20 - 1)
DUST_THRESHOLD = 0.001e8
