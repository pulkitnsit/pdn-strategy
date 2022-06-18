from datetime import timedelta, datetime

from web3 import Web3

from common.constants import DEFAULT_ADDRESS


def get_deadline(minutes=30):
    deadline = datetime.now() + timedelta(minutes=minutes)
    deadline = int(deadline.timestamp())
    return deadline


def check_and_get_default_address(w3: Web3, address):
    if address == DEFAULT_ADDRESS:
        address = w3.eth.default_account
        if address is None:
            raise ValueError("w3.eth.default_account is None")
    if address is None:
        raise ValueError("address provided is None")
    return address


def main():
    get_deadline()


if __name__ == '__main__':
    main()
