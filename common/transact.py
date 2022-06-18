from common.w3config import W3Config
from common.gas_price import GasPriceType


class TransactConfig:
    def __init__(self, pay_val=None, nonce=None, max_gas=None, gas_price_type=GasPriceType.FAST,
                 max_gas_price=None, gas_price=None):
        """All the values should be in wei
        :param pay_val: if function needs payment in ether/ftm else None.
        :param nonce: Override nonce if you need to speed up the transaction,
        else leave it none, and it will be computed automatically.
        :param max_gas: W3Config has default value which will be used when
        max_gas=None, override if needed.
        :param gas_price_type: Fast or Normal.
        :param max_gas_price: Raise error if fetched gas_price is higher than max_gas_price.
        :param gas_price: This should be None and will be automatically fetched using
        W3Config, gas_price_type and max_gas_price. Override if needed.
        """
        self.pay_val = pay_val
        self.nonce = nonce
        self.max_gas = max_gas

        self.gas_price = gas_price
        self.gas_price_type = gas_price_type
        self.max_gas_price = max_gas_price


def transact(contract_func, transact_config: TransactConfig = None):
    w3_config = contract_func.web3.config
    """If transact_config is None, then use the default values"""
    _transact_config = transact_config or TransactConfig()
    tx_dict = _build_tx_dict(w3_config, transact_config)
    tx_hash = contract_func.transact(tx_dict)
    return tx_hash


def _build_tx_dict(w3_config: W3Config, transact_config: TransactConfig):
    tx_dict = {}
    if transact_config.pay_val is not None:
        tx_dict["value"] = transact_config.pay_val
    if transact_config.nonce is not None:
        tx_dict["nonce"] = transact_config.nonce
    _update_gas(w3_config, tx_dict, transact_config.max_gas)
    _update_gas_price(w3_config, tx_dict, transact_config)
    return tx_dict


def _update_gas(w3_config: W3Config, tx_dict, max_gas):
    if max_gas is not None:
        tx_dict["gas"] = max_gas
    else:
        tx_dict["gas"] = w3_config.MAX_GAS


def _update_gas_price(w3_config: W3Config, tx_dict, transact_config: TransactConfig):
    if transact_config.gas_price is not None:
        tx_dict["gasPrice"] = transact_config.gas_price
    else:
        gas_price = w3_config.get_gas_price(transact_config.max_gas_price, transact_config.gas_price_type)
        tx_dict["gasPrice"] = gas_price
