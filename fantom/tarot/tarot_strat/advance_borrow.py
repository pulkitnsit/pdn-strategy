import logging
from typing import Type

from fantom.tarot.tarot_collateral import AbstractTarotCollateral
from fantom.tarot.tarot_strat.abstract_tarot_strat import TarotStratConfig, AccountStat
from fantom.tarot.tarot_utils import calculate_borrow_amount_to_required_borrow_pct

logger = logging.getLogger(__name__)


class AdvanceBorrow:
    def __init__(self, collateral: Type[AbstractTarotCollateral], tarot_strat_config: TarotStratConfig,
                 account_stat: AccountStat):
        self.collateral = collateral
        self.config = tarot_strat_config
        self.account_stat = account_stat

    def check_and_execute_borrow(self):
        avail_liq = int(self.collateral.main_borrowable.get_available_liq() * 0.95)
        min_main_liq = self.calculate_min_liq()
        if avail_liq > min_main_liq:
            self.borrow()

    def calculate_min_liq(self):
        min_main_liq = self.config.min_base_liquidity * self.account_stat.main_curr_amount / self.account_stat.base_curr_amount
        return int(min_main_liq)

    def borrow(self):
        # ToDo
        raise NotImplementedError

    def get_max_main_borrow(self):
        return self.get_max_borrow(self.account_stat.main_curr_amount,
                                   self.account_stat.main_borrow_amount, self.config.max_main_borrow_pct)

    def get_max_base_borrow(self):
        return self.get_max_borrow(self.account_stat.base_curr_amount,
                                   self.account_stat.base_borrow_amount, self.config.max_base_borrow_pct)

    def get_max_borrow(self, curr_in_collateral, borrow_amount, max_borrow_pct):
        return calculate_borrow_amount_to_required_borrow_pct(curr_in_collateral, borrow_amount, max_borrow_pct)
