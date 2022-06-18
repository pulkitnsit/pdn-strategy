import logging

from common.lp_calculator import LpCalculator
from fantom.tarot.tarot_utils import *

logger = logging.getLogger(__name__)


class TarotLpCalculator:
    def __init__(self, lp: LpCalculator, main_borrow_amount=None, main_borrow_pct=None,
                 base_borrow_amount=None, base_borrow_pct=None):
        self.lp = lp
        self.main_borrow_amount, self.main_borrow_pct = self.get_borrow_amount_and_pct(
            self.lp.main_curr, main_borrow_amount, main_borrow_pct)
        self.base_borrow_amount, self.base_borrow_pct = self.get_borrow_amount_and_pct(
            self.lp.base_curr, base_borrow_amount, base_borrow_pct)
        self.initial_base_curr = self.get_total_base_curr()

    @staticmethod
    def get_borrow_amount_and_pct(curr_in_collateral, borrow_amount, borrow_pct):
        if (borrow_amount is None) and (borrow_pct is None):
            return 0, 1
        if borrow_amount is None:
            borrow_amount = calculate_current_borrow_amount(curr_in_collateral, borrow_pct)
        else:
            borrow_pct = calculate_current_borrow_pct(curr_in_collateral, borrow_amount)
        return borrow_amount, borrow_pct

    def get_total_base_curr(self):
        total_base_curr = get_total_base_curr(
            self.lp.main_curr, self.lp.base_curr,
            self.main_borrow_amount, self.base_borrow_amount)
        return total_base_curr

    def borrow_amount_and_convert_to_lp_to_required_borrow_pct_for_main(self, borrow_pct):
        req_borrow_amount = calculate_borrow_amount_converted_to_lp_to_required_borrow_pct(
            self.lp.main_curr, self.main_borrow_amount, borrow_pct)
        logger.info(f"{req_borrow_amount=}")
        self.lp.convert_and_add_main_curr_to_lp(req_borrow_amount)
        self.main_borrow_amount += req_borrow_amount
        self.print_details()

    def print_details(self):
        self.lp.print_lp()
        current_main_borrow_pct = calculate_current_borrow_pct(self.lp.main_curr, self.main_borrow_amount)
        current_base_borrow_pct = calculate_current_borrow_pct(self.lp.base_curr, self.base_borrow_amount)
        _current_base_curr = get_total_base_curr(self.lp.main_curr, self.lp.base_curr,
                                                 self.main_borrow_amount, self.base_borrow_amount)
        change_base_curr = (_current_base_curr - self.initial_base_curr) * 100 / _current_base_curr
        total_borrow_pct = calculate_total_borrow_pct(self.lp.main_curr, self.lp.base_curr,
                                                      self.main_borrow_amount, self.base_borrow_amount)

        main_borrow_amount = round(self.main_borrow_amount / self.lp.decimal, 3)
        base_borrow_amount = round(self.base_borrow_amount / self.lp.decimal, 3)
        initial_base_curr = round(self.initial_base_curr / self.lp.decimal, 3)
        current_base_curr = round(_current_base_curr / self.lp.decimal, 3)
        print(f"{main_borrow_amount=}, {base_borrow_amount=}, {current_main_borrow_pct=}, "
              f"{current_base_borrow_pct=}, {total_borrow_pct=}")
        print(f"{initial_base_curr=}, {current_base_curr=}, {change_base_curr=}\n")
