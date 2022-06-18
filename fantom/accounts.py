import logging
import pickle
from getpass import getpass
from typing import Type

import cryptocode
from eth_account import Account
from web3 import middleware, Web3
from web3.middleware import construct_sign_and_send_raw_middleware

from common.constants import KEYS_FOLDER
from common.rpc_networks import RpcNetworks
from fantom.fantom_config import FantomW3Config

logger = logging.getLogger(__name__)


def get_and_assign_account(w3, private_key, fantom_config: FantomW3Config):
    account = Account.from_key(private_key)
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    assign_account(w3, account.address, fantom_config)


def assign_account(w3, public_address, fantom_config: FantomW3Config):
    _public_address = Web3.toChecksumAddress(public_address)
    w3.eth.default_account = _public_address
    w3.middleware_onion.add(middleware.latest_block_based_cache_middleware)
    w3.middleware_onion.add(middleware.simple_cache_middleware)
    setattr(w3, "config", fantom_config)


class AbstractFantomAccount:
    def __init__(self, fantom_config: Type[FantomW3Config] = None):
        if fantom_config is None:
            self.config = FantomW3Config()
        else:
            self.config = fantom_config()
        self.key_file = KEYS_FOLDER / f"{self.__class__.__name__}.pickle"

    def _get_private_key(self):
        logger.info(f"THIS IS PRODUCTION FOR {self.__class__.__name__}")
        password = getpass(prompt='Enter your password: ')
        with self.key_file.open("rb") as fl:
            encrypted_key = pickle.load(fl)
        private_key = cryptocode.decrypt(encrypted_key, password)
        return private_key

    def store_private_key(self):
        private_key = getpass(prompt='Enter your private key: ')
        logger.info(f"{len(private_key)=}")
        password = getpass(prompt='Enter your password: ')
        encrypted_key = cryptocode.encrypt(private_key, password)
        self.key_file.parent.mkdir(exist_ok=True, parents=True)
        with self.key_file.open("wb") as fl:
            pickle.dump(encrypted_key, fl)

    def get_w3(self):
        raise NotImplementedError


class ReadOnlyAccount(AbstractFantomAccount):
    def get_w3(self, address=None):
        w3 = RpcNetworks.fantom()
        assign_account(w3, address, self.config)
        return w3


class LocalAccount(AbstractFantomAccount):
    def get_w3(self, address=None):
        w3 = RpcNetworks.local()
        assign_account(w3, address, self.config)
        return w3


class TarotBorrowAccount(AbstractFantomAccount):
    def get_w3(self):
        w3 = RpcNetworks.fantom_websocket()
        private_key = self._get_private_key()
        get_and_assign_account(w3, private_key, self.config)
        return w3


def store_key():
    account = TarotBorrowAccount()
    account.store_private_key()


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stdout, format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)
    store_key()
