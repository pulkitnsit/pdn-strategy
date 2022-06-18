from web3 import Web3
from web3.middleware import geth_poa_middleware


class RpcNetworks:
    def __init__(self):
        self.index = 0

    @staticmethod
    def local(default_account=None):
        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545/"))
        if default_account is not None:
            w3.eth.default_account = default_account
        return w3

    @staticmethod
    def fantom():
        return Web3(Web3.HTTPProvider("https://rpc.ftm.tools/"))
        # return Web3(Web3.HTTPProvider("https://rpcapi.fantom.network/"))
        # return Web3(Web3.HTTPProvider("https://ftmrpc.ultimatenodes.io/"))

    def switch_fantom(self):
        urls = ["https://rpc.ftm.tools/", "https://rpcapi.fantom.network/", "https://ftmrpc.ultimatenodes.io/"]
        url = urls[self.index]
        self.index = (self.index + 1) % len(urls)
        print(url)
        return Web3(Web3.HTTPProvider(url))

    @staticmethod
    def fantom_websocket():
        return Web3(Web3.WebsocketProvider("wss://wsapi.fantom.network/"))

    @staticmethod
    def fantom_test():
        return Web3(Web3.HTTPProvider("https://rpc.testnet.fantom.network/"))

    @staticmethod
    def polygon():
        return Web3(Web3.HTTPProvider("https://rpc-mainnet.matic.quiknode.pro"))

    @staticmethod
    def avax():
        return Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))

    @staticmethod
    def bsc():
        w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        return w3
