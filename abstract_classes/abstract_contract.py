from web3 import Web3


class AbstractContract:
    ADDRESS: str

    def __init__(self, w3: Web3, abi: str):
        self.w3 = w3
        self.contract = w3.eth.contract(Web3.toChecksumAddress(self.ADDRESS), abi=abi)

    def decode_tx_data(self, tx_data):
        tx_func = self.contract.decode_function_input(tx_data)
        print(tx_func)
        breakpoint()
