import logging

from fantom.accounts import TarotBorrowAccount
from fantom.tarot.tarot_strat.advance_borrow import AdvanceBorrow
from fantom.tarot.tarot_borrowable import *

logger = logging.getLogger(__name__)


def prod_run():
    w3 = TarotBorrowAccount().get_w3()
    borrow_strat = AdvanceBorrow(w3, TshareMaiBorrowableTshare, 25)
    borrow_strat.run()


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stdout, format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)
    prod_run()
