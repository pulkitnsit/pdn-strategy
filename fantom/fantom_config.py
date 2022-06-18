from common.w3config import W3Config
from common.gas_price import get_ftm_gas_prices, GasPriceType


class FantomW3Config(W3Config):
    MAX_GAS = 5 * 10**5
    MAX_GAS_PRICE = 3500

    def get_gas_price(self, max_gas_price=None, gas_price_type=GasPriceType.FAST):
        """If max_gas_price=None, then use self.MAX_GAS_PRICE"""
        gas_prices = get_ftm_gas_prices()
        gas_price = self._get_gas_price_from_type(gas_prices, gas_price_type)
        _max_gas_price = max_gas_price or self.MAX_GAS_PRICE
        wei_max_gas_price = _max_gas_price * 10**9
        self._check_max_gas_price(gas_price, wei_max_gas_price)
        return gas_price


class FantomTestW3Config(FantomW3Config):
    def get_gas_price(self, max_gas_price=None, gas_price_type=GasPriceType.FAST):
        gas_price = super().get_gas_price(max_gas_price, gas_price_type)
        return gas_price * 3
