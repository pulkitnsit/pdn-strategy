import logging
import time
from typing import Type

from fantom.tarot.tarot_strat.abstract_tarot_strat import AbstractTarotStrat
from fantom.tarot.tarot import Tarot
from fantom.tarot.tarot_collateral import AbstractTarotCollateral
from fantom.tarot.tarot_strat.advance_borrow import AdvanceBorrow
from fantom.tarot.tarot_utils import calculate_current_borrow_pct
from position_strategy.abstract_position_strategy import Position

logger = logging.getLogger(__name__)


class TarotStrat(AbstractTarotStrat):
    """Not using advance borrow for now to keep strategy simple"""
    def run_advance_borrow(self):
        event = self.w3.eth.filter({"address": self.collateral.main_borrowable.ADDRESS})
        while True:
            new_entries = event.get_new_entries()
            if len(new_entries) > 0:
                logger.info(f"In check_and_execute_borrow at {self.w3.eth.block_number}")
                AdvanceBorrow(self.collateral, self.config, self.account_stat).check_and_execute_borrow()
            time.sleep(0.1)

    def run_strategy(self):
        if self.curr_pos is None:
            predicted_pos = self.position_strat.get_latest_position()
            self.curr_pos = predicted_pos
        self._run_in_loop()

    def _run_in_loop(self):
        while True:
            predicted_pos = self.position_strat.get_latest_position()
            if self.curr_pos != predicted_pos:
                self.change_pos(predicted_pos)
            time.sleep(60)

    def change_pos(self, predicted_pos):
        if predicted_pos == Position.BUY:
            self.change_to_buy()
        elif predicted_pos == Position.SELL:
            self.change_to_sell()
