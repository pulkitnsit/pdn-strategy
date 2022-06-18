import json
from abc import ABC
from typing import Type, Union

from web3 import Web3

from common.constants import DEFAULT_ADDRESS
from common.utils import check_and_get_default_address


class AbstractCurrency(ABC):
    ADDRESS: str
    DECIMAL = 10 ** 18

    def __init__(self, w3: Web3, abi=None):
        self.w3 = w3
        if abi is None:
            abi = json.loads("""[
            {
                "constant": true,
                "inputs": [],
                "name": "name",
                "outputs": [
                    {
                        "name": "",
                        "type": "string"
                    }
                ],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": false,
                "inputs": [
                    {
                        "name": "guy",
                        "type": "address"
                    },
                    {
                        "name": "wad",
                        "type": "uint256"
                    }
                ],
                "name": "approve",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": false,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [],
                "name": "totalSupply",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": false,
                "inputs": [
                    {
                        "name": "src",
                        "type": "address"
                    },
                    {
                        "name": "dst",
                        "type": "address"
                    },
                    {
                        "name": "wad",
                        "type": "uint256"
                    }
                ],
                "name": "transferFrom",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": false,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": false,
                "inputs": [
                    {
                        "name": "wad",
                        "type": "uint256"
                    }
                ],
                "name": "withdraw",
                "outputs": [],
                "payable": false,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [],
                "name": "decimals",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint8"
                    }
                ],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [
                    {
                        "name": "",
                        "type": "address"
                    }
                ],
                "name": "balanceOf",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [],
                "name": "symbol",
                "outputs": [
                    {
                        "name": "",
                        "type": "string"
                    }
                ],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": false,
                "inputs": [
                    {
                        "name": "dst",
                        "type": "address"
                    },
                    {
                        "name": "wad",
                        "type": "uint256"
                    }
                ],
                "name": "transfer",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": false,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": false,
                "inputs": [],
                "name": "deposit",
                "outputs": [],
                "payable": true,
                "stateMutability": "payable",
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [
                    {
                        "name": "",
                        "type": "address"
                    },
                    {
                        "name": "",
                        "type": "address"
                    }
                ],
                "name": "allowance",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "payable": true,
                "stateMutability": "payable",
                "type": "fallback"
            },
            {
                "anonymous": false,
                "inputs": [
                    {
                        "indexed": true,
                        "name": "src",
                        "type": "address"
                    },
                    {
                        "indexed": true,
                        "name": "guy",
                        "type": "address"
                    },
                    {
                        "indexed": false,
                        "name": "wad",
                        "type": "uint256"
                    }
                ],
                "name": "Approval",
                "type": "event"
            },
            {
                "anonymous": false,
                "inputs": [
                    {
                        "indexed": true,
                        "name": "src",
                        "type": "address"
                    },
                    {
                        "indexed": true,
                        "name": "dst",
                        "type": "address"
                    },
                    {
                        "indexed": false,
                        "name": "wad",
                        "type": "uint256"
                    }
                ],
                "name": "Transfer",
                "type": "event"
            },
            {
                "anonymous": false,
                "inputs": [
                    {
                        "indexed": true,
                        "name": "dst",
                        "type": "address"
                    },
                    {
                        "indexed": false,
                        "name": "wad",
                        "type": "uint256"
                    }
                ],
                "name": "Deposit",
                "type": "event"
            },
            {
                "anonymous": false,
                "inputs": [
                    {
                        "indexed": true,
                        "name": "src",
                        "type": "address"
                    },
                    {
                        "indexed": false,
                        "name": "wad",
                        "type": "uint256"
                    }
                ],
                "name": "Withdrawal",
                "type": "event"
            }
        ]""")
        self.contract = self.w3.eth.contract(address=Web3.toChecksumAddress(self.ADDRESS), abi=abi)

    def get_balance_of_in_eth(self, address=DEFAULT_ADDRESS, block_identifier='latest'):
        balance = self.get_balance_of(address, block_identifier)
        conv_balance = balance / self.DECIMAL
        return conv_balance

    def get_balance_of(self, address=DEFAULT_ADDRESS, block_identifier='latest'):
        _address = check_and_get_default_address(self.w3, address)
        balance = self.contract.functions.balanceOf(Web3.toChecksumAddress(_address)).call(block_identifier=block_identifier)
        return balance

    def get_total_supply(self):
        return self.contract.functions.totalSupply().call()

    def approve(self, address: str, amount=None):
        if amount is None:
            conv_curr1_amount = int(2**255)
        else:
            conv_curr1_amount = int(amount * self.DECIMAL)
        # breakpoint()
        tx_hash = self.contract.functions.approve(
            Web3.toChecksumAddress(address), conv_curr1_amount).transact()
        return tx_hash

    def transfer(self, to_address, amount):
        conv_amount = amount * self.DECIMAL
        tx_hash = self.contract.functions.transfer(to_address, conv_amount).transact()
        return tx_hash


class Currency(AbstractCurrency):
    def __init__(self, w3: Web3, address, abi=None):
        self.ADDRESS = address
        super().__init__(w3, abi)
        decimal = self.contract.functions.decimals().call()
        self.DECIMAL = 10**decimal


CurrencyType = Union[AbstractCurrency, Type[AbstractCurrency]]
