from abstract_classes.abstract_currency import AbstractCurrency


class PolyUSDC(AbstractCurrency):
    ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
    DECIMAL = 10 ** 6


class MATIC(AbstractCurrency):
    ADDRESS = "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"


class ETH(AbstractCurrency):
    ADDRESS = "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619"


class PolyTOMB(AbstractCurrency):
    ADDRESS = "0x0e98c977b943f06075b2d795794238fbfb9b9a34"


class PolyMAI(AbstractCurrency):
    ADDRESS = "0xa3fa99a148fa48d14ed51d610c367c61876997f1"
