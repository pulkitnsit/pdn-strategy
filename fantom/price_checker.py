import logging
import os
import time
import traceback

from playsound import playsound
from web3 import Web3

from avax.currency import AVAXUSDC, THORUS
from avax.exchanges import ThorusSwap, TraderJoe
from binance_network.exchanges import PancakeSwap

from binance_network.currency import Helena, WBNB
from common.rpc_networks import RpcNetworks
from fantom.accounts import ReadOnlyAccount
from fantom.currency import *
from fantom.exchanges import *
from fantom.tarot.tarot_collateral import *
from fantom.tarot.tarot_utils import calculate_current_borrow_pct

logger = logging.getLogger(__name__)


class PriceChecker:
    def __init__(self):
        # self.w3 = Web3(Web3.HTTPProvider('https://rpc-mainnet.matic.quiknode.pro'))
        # self.w3 = Web3(Web3.HTTPProvider("http://rpc.fantom.network/"))
        # self.w3 = Web3(Web3.HTTPProvider("https://rpc.neist.io/"))

        self.tarot_ftm_w3 = ReadOnlyAccount().get_w3(os.environ.get("tarot_ftm_address"))
        self.bshare_ftm_w3 = ReadOnlyAccount().get_w3(os.environ.get("bshare_ftm_address"))
        self.avax_w3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))
        self.bsc_w3 = RpcNetworks.bsc()

    def check_price(self):
        spooky_swap = SpookySwap(self.tarot_ftm_w3)
        spirit_swap = SpiritSwap(self.tarot_ftm_w3)
        tomb_swap = TombSwap(self.tarot_ftm_w3)
        solid_swap = SolidSwap(self.tarot_ftm_w3)
        thorus_swap = ThorusSwap(self.avax_w3)
        pancake_swap = PancakeSwap(self.bsc_w3)
        # thorus_swap = TraderJoe(self.avax_w3)

        oxd_tarot = TarotOxdBorrowable(self.tarot_ftm_w3)
        tarot_3omb_borrowable = ThreeOmbFtmBorrowableThree(self.tarot_ftm_w3)
        tarot_2share_borrowable = TwoShareFtmBorrowableTwo(self.tarot_ftm_w3)
        tarot_2omb_borrowable = TwoOmbFtmBorrowableTwo(self.tarot_ftm_w3)
        tarot_bshare_borrowable = BshareFtmBorrowableBshare(self.tarot_ftm_w3)
        tshare_mai_borrowable = TshareMaiBorrowableTshare(self.tarot_ftm_w3)

        dei_deus_collateral = DeiDeusCollateral(self.tarot_ftm_w3)
        two_ftm_collateral = TwoShareFtmCollateral(self.tarot_ftm_w3)
        tomb_ftm_collateral = TombFtmCollateral(self.tarot_ftm_w3)
        bshare_ftm_collateral = BshareFtmCollateral(self.bshare_ftm_w3)
        based_mai_collateral = BasedMaiCollateral(self.bshare_ftm_w3)
        tshare_mai_collateral = TshareMaiCollateral(self.tarot_ftm_w3)
        while True:
            # self.check_curr_price(spooky_swap, USDC, TSHARE, shit_ratio=11000, use_curr1_ratio=True)
            # self.check_curr_price(spooky_swap, [USDC, WFTM], shit_ratio=(1/0.45))
            self.check_curr_price(spooky_swap, [WFTM, USDC], shit_ratio=0.33)
            # self.check_curr_price(spooky_swap, [MAI, WFTM], shit_ratio=0.27)
            # self.check_curr_price(spooky_swap, [WFTM, MAI], shit_ratio=1.6)
            # self.check_curr_price(spooky_swap, [DAI, WFTM], shit_ratio=0.34)
            # self.check_curr_price(spooky_swap, [WFTM, DAI], shit_ratio=1.55)
            # self.check_curr_price(tomb_swap, [TOMB, MAI], shit_ratio=0.98)
            # self.check_curr_price(tomb_swap, [MAI, TOMB], shit_ratio=0.85)
            self.check_curr_price(spooky_swap, [TOMB, WFTM], shit_ratio=0.58)
            # self.check_curr_price(spooky_swap, [WFTM, TOMB], shit_ratio=1/0.52)
            # self.check_curr_price(spooky_swap, [Based, TOMB], shit_ratio=1.25)
            # self.check_curr_price(spooky_swap, [TOMB, Based], shit_ratio=0.63)
            # self.check_curr_price(spooky_swap, [Bshare, WFTM], shit_ratio=1150)
            # self.check_curr_price(spooky_swap, [WFTM, Bshare], shit_ratio=0.0005)
            # self.check_curr_price(spooky_swap, [GRAIL, WFTM], shit_ratio=205)
            # self.check_curr_price(spooky_swap, [TSHARE, WFTM], shit_ratio=2600)
            # self.check_curr_price(spooky_swap, [WFTM, TSHARE], shit_ratio=0.000365)
            self.check_curr_price(tomb_swap, [TSHARE, MAI], shit_ratio=720)
            # self.check_curr_price(tomb_swap, [MAI, TSHARE], shit_ratio=1/4000)
            # self.check_curr_price(spooky_swap, [TwoShare, WFTM], shit_ratio=44)
            # self.check_curr_price(spooky_swap, [WFTM, TwoShare], shit_ratio=0.021)
            # self.check_curr_price(spooky_swap, [Solid, WFTM], shit_ratio=1.59)
            # self.check_curr_price(spooky_swap, [WFTM, Solid], shit_ratio=0.54)
            # self.check_curr_price(spooky_swap, [WFTM, ThreeOmb], shit_ratio=0.25)
            # self.check_curr_price(spooky_swap, [ThreeOmb, WFTM], shit_ratio=0.95)
            # self.check_curr_price(spooky_swap, [WFTM, TSHARE], shit_ratio=0.000149)
            # self.check_curr_price(spooky_swap, [TAROT, WFTM], shit_ratio=0.05)
            # self.check_curr_price(spooky_swap, [WFTM, TAROT], shit_ratio=0.6)
            # self.check_curr_price(solid_swap, [Dei, Deus], shit_ratio=0.0024)
            # self.check_curr_price(solid_swap, [Deus, Dei], shit_ratio=300)
            # self.check_curr_price(spirit_swap, [CRV, WFTM], shit_ratio=1.4)
            # self.check_curr_price(spirit_swap, [WFTM, CRV], shit_ratio=0.5)
            # self.check_curr_price(spooky_swap, [OXD, USDC], shit_ratio=0.0175)
            # self.check_curr_price(swap, USDC, OXD, shit_ratio=11.7)
            # self.check_curr_price(thorus_swap, AVAXUSDC, THORUS, shit_ratio=2.8)
            # self.check_curr_price(thorus_swap, THORUS, AVAXUSDC, shit_ratio=0.26)
            # self.check_curr_price(pancake_swap, [Helena, WBNB], shit_ratio=0.025)

            # self.check_borrow_pct_with_account_balance(
            #     dei_deus_collateral, base_lower_limit=1.95, base_upper_limit=2.05)
            # self.check_borrow_pct_with_account_balance(
            #     two_ftm_collateral, main_lower_limit=1.95, main_upper_limit=2.2)

            # self.check_borrow_pct(bshare_ftm_collateral, main_upper_limit=1.95, base_upper_limit=1.7)
            # self.check_borrow_pct(based_mai_collateral, base_upper_limit=2.65, base_lower_limit=1.90)
            self.check_borrow_pct(based_mai_collateral, base_upper_limit=1.8, main_upper_limit=1.8)
            self.check_borrow_pct(tomb_ftm_collateral, base_upper_limit=2.5, main_upper_limit=1)
            # self.check_borrow_pct(tshare_mai_collateral, base_upper_limit=2.65, base_lower_limit=1.95, main_upper_limit=1.5)

            # self.check_liq(oxd_tarot, max_threshold=1000)
            # self.check_liq(tarot_3omb_borrowable, max_threshold=25, raise_alarm=False)
            # self.check_liq(tarot_2omb_borrowable, max_threshold=25, raise_alarm=False)
            # self.check_liq(tarot_2share_borrowable, max_threshold=0.02, raise_alarm=False)
            # self.check_liq(tarot_bshare_borrowable, min_threshold=50, raise_alarm=True)
            # self.check_liq(tshare_mai_borrowable, min_threshold=230, raise_alarm=True)
            time.sleep(30)

    def check_curr_price(self, swap, curr_path: list, shit_ratio, amount=10, use_curr1_ratio=False):
        try:
            curr2_ratio, _, curr1_ratio = swap.get_ratio(curr_path, amount)
            if use_curr1_ratio:
                if curr1_ratio < shit_ratio:
                    self.raise_alarm()
            else:
                if curr2_ratio < shit_ratio:
                    self.raise_alarm()
            time.sleep(1)
        except Exception:
            logger.info(traceback.format_exc())
            time.sleep(5)
            self.check_curr_price(swap, curr_path, shit_ratio, amount, use_curr1_ratio)

    def check_borrow_pct(self, collateral, main_lower_limit=0.0, main_upper_limit=2.0,
                         base_lower_limit=0.0, base_upper_limit=2.0):
        try:
            main_curr_in_collateral, base_curr_in_collateral = collateral.get_tokens_amount_in_lp_of()

            main_borrow = collateral.main_borrowable.get_borrow_balance_of()
            main_borrow_pct = calculate_current_borrow_pct(main_curr_in_collateral, main_borrow)
            base_borrow = collateral.base_borrowable.get_borrow_balance_of()
            base_borrow_pct = calculate_current_borrow_pct(base_curr_in_collateral, base_borrow)

            logger.info(f"{collateral.__class__.__name__}: {main_borrow_pct=}, "
                        f"{base_borrow_pct=}")

            if not(main_lower_limit < main_borrow_pct < main_upper_limit):
                self.raise_alarm()
            if not(base_lower_limit < base_borrow_pct < base_upper_limit):
                self.raise_alarm()
        except Exception:
            logger.info(traceback.format_exc())
            time.sleep(5)
            self.check_borrow_pct(collateral, main_lower_limit, main_upper_limit, base_lower_limit, base_upper_limit)

    def check_borrow_pct_with_account_balance(
            self, collateral, main_lower_limit=0.0, main_upper_limit=2.0,
            base_lower_limit=0.0, base_upper_limit=2.0):
        try:
            main_curr_in_collateral, base_curr_in_collateral = collateral.get_tokens_amount_in_lp_of()

            main_borrow = collateral.main_borrowable.get_borrow_balance_of()
            main_curr_in_account = collateral.main_borrowable.curr.get_balance_of()
            main_borrow = max(0, main_borrow - main_curr_in_account)
            main_borrow_pct = calculate_current_borrow_pct(main_curr_in_collateral, main_borrow)

            base_borrow = collateral.base_borrowable.get_borrow_balance_of()
            base_curr_in_account = collateral.base_borrowable.curr.get_balance_of()
            base_borrow = max(0, base_borrow - base_curr_in_account)
            base_borrow_pct = calculate_current_borrow_pct(base_curr_in_collateral, base_borrow)

            logger.info(f"{collateral.__class__.__name__}: {main_borrow_pct=}, "
                        f"{base_borrow_pct=}")

            if not(main_lower_limit < main_borrow_pct < main_upper_limit):
                self.raise_alarm()
            if not(base_lower_limit < base_borrow_pct < base_upper_limit):
                self.raise_alarm()
        except Exception:
            logger.info(traceback.format_exc())
            time.sleep(5)
            self.check_borrow_pct_with_account_balance(
                collateral, main_lower_limit, main_upper_limit, base_lower_limit, base_upper_limit)

    def check_liq(self, tarot_borrowable, min_threshold=None, max_threshold=None, raise_alarm=True):
        try:
            available_supply = tarot_borrowable.get_available_liq_in_eth()
            logger.info(f"{tarot_borrowable.__class__.__name__}: {available_supply}")
            if max_threshold is not None:
                if available_supply > max_threshold:
                    logger.info(f"{tarot_borrowable.__class__.__name__}: supply available")
                    if raise_alarm:
                        self.raise_alarm()
            if min_threshold is not None:
                if available_supply < min_threshold:
                    logger.info(f"{tarot_borrowable.__class__.__name__}: supply available")
                    if raise_alarm:
                        self.raise_alarm()
        except Exception:
            logger.info(traceback.format_exc())
            time.sleep(5)
            self.check_liq(tarot_borrowable, min_threshold, max_threshold, raise_alarm)

    def __check_utilization(self, tarot_borrowable, min_required=1000.0, raise_alarm=True):
        # ToDo: Could not complete this
        try:
            available_supply = tarot_borrowable.get_available_liq()
            logger.info(f"{tarot_borrowable.__class__.__name__}: {available_supply}")
            if available_supply > min_required:
                logger.info(f"{tarot_borrowable.__class__.__name__}: supply available")
                if raise_alarm:
                    self.raise_alarm()
        except Exception:
            logger.info(traceback.format_exc())
            time.sleep(5)
            self.check_liq(tarot_borrowable, min_required, raise_alarm)

    @staticmethod
    def raise_alarm():
        while True:
            playsound("alarm_sounds/relaxing_electropop.mp3")


def main():
    # stabilize_collateral()
    price_checker = PriceChecker()
    price_checker.check_price()


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stdout, format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)
    main()
