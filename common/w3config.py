from common.gas_price import GasPriceType


class W3Config:
    MAX_GAS: int

    def get_gas_price(self, max_gas_price: int, gas_price_type=GasPriceType.FAST):
        raise NotImplementedError

    @staticmethod
    def _get_gas_price_from_type(gas_prices, gas_price_type):
        if gas_price_type is GasPriceType.FAST:
            gas_price = gas_prices.fast
        else:
            gas_price = gas_prices.normal
        return gas_price

    @staticmethod
    def _check_max_gas_price(gas_price, max_gas_price):
        if gas_price > max_gas_price:
            raise ValueError(f"Gas price too high: {gas_price} > {max_gas_price}")
