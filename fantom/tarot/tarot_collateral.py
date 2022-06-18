import logging

from abstract_classes.abstract_lp import Lp, AbstractLp
from fantom.tarot.tarot_borrowable import *
from fantom.tarot.tarot_vault import TarotVault, AbstractTarotVault

logger = logging.getLogger(__name__)


class AbstractTarotCollateral(AbstractCurrency):
    MAIN_BORROW_ADDR: str

    def __init__(self, w3):
        abi = json.loads("""[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"minter","type":"address"},{"indexed":false,"internalType":"uint256","name":"mintAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"mintTokens","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newLiquidationIncentive","type":"uint256"}],"name":"NewLiquidationIncentive","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newSafetyMarginSqrt","type":"uint256"}],"name":"NewSafetyMargin","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"redeemer","type":"address"},{"indexed":false,"internalType":"uint256","name":"redeemAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"redeemTokens","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"totalBalance","type":"uint256"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"LIQUIDATION_INCENTIVE_MAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"LIQUIDATION_INCENTIVE_MIN","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"SAFETY_MARGIN_SQRT_MAX","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"SAFETY_MARGIN_SQRT_MIN","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"address","name":"_underlying","type":"address"},{"internalType":"address","name":"_borrowable0","type":"address"},{"internalType":"address","name":"_borrowable1","type":"address"}],"name":"_initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"_setFactory","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"newLiquidationIncentive","type":"uint256"}],"name":"_setLiquidationIncentive","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"newSafetyMarginSqrt","type":"uint256"}],"name":"_setSafetyMarginSqrt","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"borrower","type":"address"}],"name":"accountLiquidity","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"shortfall","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"borrower","type":"address"},{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"accountLiquidityAmounts","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"shortfall","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"borrowable0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"borrowable1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"borrower","type":"address"},{"internalType":"address","name":"borrowable","type":"address"},{"internalType":"uint256","name":"accountBorrows","type":"uint256"}],"name":"canBorrow","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"exchangeRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"redeemer","type":"address"},{"internalType":"uint256","name":"redeemAmount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"flashRedeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"getPrices","outputs":[{"internalType":"uint256","name":"price0","type":"uint256"},{"internalType":"uint256","name":"price1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"liquidationIncentive","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"minter","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"mintTokens","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"redeemer","type":"address"}],"name":"redeem","outputs":[{"internalType":"uint256","name":"redeemAmount","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"safetyMarginSqrt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"liquidator","type":"address"},{"internalType":"address","name":"borrower","type":"address"},{"internalType":"uint256","name":"repayAmount","type":"uint256"}],"name":"seize","outputs":[{"internalType":"uint256","name":"seizeTokens","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"tarotPriceOracle","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"tokensUnlocked","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"underlying","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]""")
        super().__init__(w3, abi)
        self._main_borrowable = None
        self._base_borrowable = None
        self._underlying = None
        self._vault = None
        self._lp = None

    @property
    def main_borrowable(self) -> AbstractTarotBorrowable:
        if self._main_borrowable is None:
            self._assign_borrowables()
        return self._main_borrowable

    @main_borrowable.setter
    def main_borrowable(self, address: str):
        self._main_borrowable = TarotBorrowable(self.w3, address)

    @property
    def base_borrowable(self) -> AbstractTarotBorrowable:
        if self._base_borrowable is None:
            self._assign_borrowables()
        return self._base_borrowable

    @base_borrowable.setter
    def base_borrowable(self, address: str):
        self._base_borrowable = TarotBorrowable(self.w3, address)

    @property
    def underlying(self):
        if self._underlying is None:
            self._underlying = self.contract.functions.underlying().call()
        return self._underlying

    @property
    def vault(self) -> AbstractTarotVault:
        if self._vault is None:
            self._vault = TarotVault(self.w3, self.underlying)
        return self._vault

    @property
    def lp(self) -> AbstractLp:
        if self._lp is None:
            self._lp = Lp(self.w3, self.vault.underlying, self.main_borrowable.curr.ADDRESS)
        return self._lp

    def _assign_borrowables(self):
        borrowable0 = self.contract.functions.borrowable0().call()
        borrowable1 = self.contract.functions.borrowable1().call()
        if borrowable0.lower() == self.MAIN_BORROW_ADDR.lower():
            self.main_borrowable = borrowable0
            self.base_borrowable = borrowable1
        elif borrowable1.lower() == self.MAIN_BORROW_ADDR.lower():
            self.main_borrowable = borrowable1
            self.base_borrowable = borrowable0
        else:
            raise ValueError(f"{self.MAIN_BORROW_ADDR=} is not in {borrowable0=} or {borrowable1=}")

    def get_tokens_amount_in_lp_of(self, address=DEFAULT_ADDRESS):
        balance = self.get_lp_amount_of(address)
        main_curr_amount, base_curr_amount = self.get_tokens_amount_in_lp_from_lp_amount(balance)
        return main_curr_amount, base_curr_amount

    def get_lp_amount_of(self, address=DEFAULT_ADDRESS):
        collateral_balance = self.get_balance_of(address)
        return self.get_lp_amount_from_collateral_amount(collateral_balance)

    def get_tokens_amount_in_lp_from_lp_amount(self, lp_amount):
        main_curr_amount, base_curr_amount = self.lp.get_tokens_amount_from_lp_amount(lp_amount)
        return main_curr_amount, base_curr_amount

    def get_lp_amount_from_collateral_amount(self, amount):
        collateral_exchange_rate = self.get_exchange_rate()
        vault_exchange_rate = self.vault.get_exchange_rate()
        lp_tokens = int(collateral_exchange_rate * vault_exchange_rate * amount / 10**36)
        return lp_tokens

    def get_exchange_rate(self):
        return self.contract.functions.exchangeRate().call()


TarotCollateralType = [AbstractTarotCollateral, Type[AbstractTarotCollateral]]


class TshareFtmCollateral(AbstractTarotCollateral):
    ADDRESS = "0x40435ead2B5da9980f0511aF454C7f73BDdF9108"
    MAIN_BORROW_ADDR = TshareFtmBorrowableTshare.ADDRESS


class ThreeOmbFtmCollateral(AbstractTarotCollateral):
    ADDRESS = "0x8b927c1007807afd5bdb01751b1aba7fc845b62b"
    MAIN_BORROW_ADDR = ThreeOmbFtmBorrowableThree.ADDRESS


class TwoShareFtmCollateral(AbstractTarotCollateral):
    ADDRESS = "0x51084b9e086ffce96189ceaa817c1d094fa5c89c"
    MAIN_BORROW_ADDR = TwoShareFtmBorrowableTwo.ADDRESS


class DeiDeusCollateral(AbstractTarotCollateral):
    ADDRESS = "0x9f93abd08990eaa680108b06d9d21d1dd68c049a"
    MAIN_BORROW_ADDR = DeiDeusBorrowableDei.ADDRESS


class BshareFtmCollateral(AbstractTarotCollateral):
    ADDRESS = "0x32f502d7273cde0c877de08782cfc8d221478655"
    MAIN_BORROW_ADDR = BshareFtmBorrowableBshare.ADDRESS


class BasedMaiCollateral(AbstractTarotCollateral):
    ADDRESS = "0x8bdfd042ce29fb43b0b0b7dbceeab99169964700"
    MAIN_BORROW_ADDR = BasedMaiBorrowableBased.ADDRESS


class TshareMaiCollateral(AbstractTarotCollateral):
    ADDRESS = "0x73151cca9e1fb165ab4e527a3ebc4d22a66e8980"
    MAIN_BORROW_ADDR = TshareMaiBorrowableTshare.ADDRESS


class TombFtmCollateral(AbstractTarotCollateral):
    ADDRESS = "0x89e2edd65bb05351f5b8d3e5d245bfb38747e991"
    MAIN_BORROW_ADDR = TombFtmBorrowableTomb.ADDRESS
