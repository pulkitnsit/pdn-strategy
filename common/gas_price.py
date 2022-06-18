import math
from enum import Enum

import requests


class GasPriceType(Enum):
    FAST = "fast"
    NORMAL = "normal"


class GasPrices:
    def __init__(self, normal: float, fast: int, decimal_mult=1):
        self.normal = int(normal * decimal_mult)
        self.fast = int(fast * decimal_mult)


def get_ftm_gas_prices():
    req = requests.get("https://gftm.blockscan.com/gasapi.ashx?apikey=key&method=gasoracle")
    json_resp = req.json()
    result = json_resp["result"]
    gas_prices = GasPrices(float(result["ProposeGasPrice"]),
                           get_round_up(result["FastGasPrice"], 100),
                           decimal_mult=10**9)
    return gas_prices


def get_round_up(number, place=100):
    decimal_number = float(number) / place
    round_up = math.ceil(decimal_number) * place
    return round_up
