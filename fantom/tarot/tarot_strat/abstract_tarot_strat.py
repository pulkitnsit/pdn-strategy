import logging
from typing import Type

from fantom.tarot.tarot import Tarot
from fantom.tarot.tarot_collateral import AbstractTarotCollateral
from fantom.tarot.tarot_utils import calculate_current_borrow_pct
from position_strategy.abstract_position_strategy import Position, AbstractPositionStrategy

logger = logging.getLogger(__name__)


class AccountStat:
    def __init__(self):
        self.lp_amount = 0
        self.main_curr_amount = 0
        self.base_curr_amount = 0
        self.main_curr_amount_in_wallet = 0
        self.base_curr_amount_in_wallet = 0
        self.main_borrow_amount = 0
        self.base_borrow_amount = 0

    def get_main_borrow_pct(self):
        assert self.main_curr_amount != 0
        borrow_pct = calculate_current_borrow_pct(self.main_curr_amount, self.main_borrow_amount)
        return borrow_pct

    def get_base_borrow_pct(self):
        assert self.base_curr_amount != 0
        borrow_pct = calculate_current_borrow_pct(self.base_curr_amount, self.base_borrow_amount)
        return borrow_pct

    def get_main_curr_to_lp(self, main_curr_amount):
        return int(main_curr_amount * self.lp_amount / self.main_curr_amount)

    def get_base_curr_to_lp(self, base_curr_amount):
        return int(base_curr_amount * self.lp_amount / self.base_curr_amount)


class TarotStratConfig:
    def __init__(self, min_base_liquidity=50, max_base_borrow_pct=1.5, max_main_borrow_pct=2.1,
                 min_main_borrow_pct=1.7, normal_main_borrow_pct=1.85, strat_max_main_borrow_pct=2,
                 min_base_amount_in_account=0.1):
        """Config for Borrow Strategy"""
        """Use min_base_liquidity to calculate min_main_liquidity as in 2share/FTM, 
        when 2share price is high, we require less min_liquidity of 2share, but when price is low, 
        we need more min_liquidity (to make it worth the gas spent), hence it is better to keep it 
        according to base_curr (ftm in this case)."""
        self.min_base_liquidity = min_base_liquidity
        self.max_base_borrow_pct = max_base_borrow_pct
        self.max_main_borrow_pct = max_main_borrow_pct
        self.min_main_borrow_pct = min_main_borrow_pct
        self.normal_main_borrow_pct = normal_main_borrow_pct
        self.strat_max_main_borrow_pct = strat_max_main_borrow_pct
        self.min_base_amount_in_account = min_base_amount_in_account


class AbstractTarotStrat:
    def __init__(self, w3, collateral: Type[AbstractTarotCollateral],
                 position_strat: AbstractPositionStrategy = None,
                 tarot_strat_config: TarotStratConfig = None, curr_pos: Position = None):
        """min_liq is in eth (i.e after multiplying with decimal)"""
        self.w3 = w3
        self.tarot = Tarot(w3)
        self.collateral = collateral(w3)
        self.config = tarot_strat_config or TarotStratConfig()
        self.position_strat = position_strat
        self.curr_pos = curr_pos

        self.account_stat = AccountStat()
        self.update_account_stat()

    def update_account_stat(self):
        logger.info("update_account_stat: Started")
        lp_amount = self.collateral.get_lp_amount_of()
        self.account_stat.lp_amount = lp_amount
        self.account_stat.main_curr_amount, self.account_stat.base_curr_amount = \
            self.collateral.get_tokens_amount_in_lp_from_lp_amount(lp_amount)
        self.account_stat.main_borrow_amount = self.collateral.main_borrowable.get_borrow_balance_of()
        self.account_stat.base_borrow_amount = self.collateral.base_borrowable.get_borrow_balance_of()
        logger.info("update_account_stat: Completed")
