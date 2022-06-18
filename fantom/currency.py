import json

from abstract_classes.abstract_currency import AbstractCurrency
from abstract_classes.abstract_lp import AbstractLp


class USDC(AbstractCurrency):
    ADDRESS = "0x04068da6c83afcfa0e13ba15a6696662335d5b75"
    DECIMAL = 10 ** 6


class FUSDT(AbstractCurrency):
    ADDRESS = "0x049d68029688eabf473097a2fc38ef61633a3c7a"
    DECIMAL = 10 ** 6


class TOMB(AbstractCurrency):
    ADDRESS = "0x6c021ae822bea943b2e66552bde1d2696a53fbb7"


class WFTM(AbstractCurrency):
    ADDRESS = "0x21be370d5312f44cb42ce377bc9b8a0cef1a4c83"

    def __init__(self, w3):
        abi = json.loads("""[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"PauserAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"PauserRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"constant":true,"inputs":[],"name":"ERR_INVALID_ZERO_VALUE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"ERR_NO_ERROR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"addPauser","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isPauser","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renouncePauser","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]""")
        super().__init__(w3, abi)


class TSHARE(AbstractCurrency):
    ADDRESS = "0x4cdf39285d7ca8eb3f090fda0c069ba5f4145b37"


class TAROT(AbstractCurrency):
    ADDRESS = "0xc5e2b037d30a390e62180970b3aa4e91868764cd"


class OXD(AbstractCurrency):
    ADDRESS = "0xc165d941481e68696f43ee6e99bfb2b23e0e3114"


class MAI(AbstractCurrency):
    ADDRESS = "0xfB98B335551a418cD0737375a2ea0ded62Ea213b"


class MIM(AbstractCurrency):
    ADDRESS = "0x82f0B8B456c1A451378467398982d4834b6829c1"


class CRV(AbstractCurrency):
    ADDRESS = "0x1E4F97b9f9F913c46F1632781732927B9019C68b"


class DAI(AbstractCurrency):
    ADDRESS = "0x8d11ec38a3eb5e956b052f67da8bdc9bef8abf3e"


class TwoShare(AbstractCurrency):
    ADDRESS = "0xc54a1684fd1bef1f077a336e6be4bd9a3096a6ca"


class TwoOmb(AbstractCurrency):
    ADDRESS = "0x7a6e4e3cc2ac9924605dca4ba31d1831c84b44ae"


class ThreeOmb(AbstractCurrency):
    ADDRESS = "0x14def7584a6c52f470ca4f4b9671056b22f4ffde"


class Based(AbstractCurrency):
    ADDRESS = "0x8D7d3409881b51466B483B11Ea1B8A03cdEd89ae"


class Bshare(AbstractCurrency):
    ADDRESS = "0x49C290Ff692149A4E16611c694fdED42C954ab7a"


class Solid(AbstractCurrency):
    ADDRESS = "0x888ef71766ca594ded1f0fa3ae64ed2941740a20"


class Dei(AbstractCurrency):
    ADDRESS = "0xDE12c7959E1a72bbe8a5f7A1dc8f8EeF9Ab011B3"


class Deus(AbstractCurrency):
    ADDRESS = "0xDE5ed76E7c05eC5e4572CfC88d1ACEA165109E44"


class GRAIL(AbstractCurrency):
    ADDRESS = "0x255861B569D44Df3E113b6cA090a1122046E6F89"


# LPs

class TshareFtmLp(AbstractLp):
    ADDRESS = "0x4733bc45ef91cf7ccecaeedb794727075fb209f2"
    MAIN_CURR_ADDR = TSHARE.ADDRESS


class BasedTombLp(AbstractLp):
    ADDRESS = "0xaB2ddCBB346327bBDF97120b0dD5eE172a9c8f9E"
    MAIN_CURR_ADDR = Based.ADDRESS


def main():
    from common.rpc_networks import RpcNetworks
    w3 = RpcNetworks.fantom_websocket()
    lp = BasedTombLp(w3)


if __name__ == '__main__':
    main()

