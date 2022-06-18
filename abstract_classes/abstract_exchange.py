import logging

from web3 import Web3

from abstract_classes.abstract_contract import AbstractContract
from common.utils import get_deadline

logger = logging.getLogger(__name__)


class AbstractExchange(AbstractContract):
    ADDRESS: str

    def get_output_amounts(self, curr_path: list, curr1_amount, block_identifier='latest'):
        curr1 = curr_path[0]
        abs_curr1_amount = int(curr1_amount * curr1.DECIMAL)
        checksum_path = list(map(lambda x: Web3.toChecksumAddress(x.ADDRESS), curr_path))
        # breakpoint()
        output_amounts = self.get_amounts_out(abs_curr1_amount, checksum_path, block_identifier)
        rel_output_amounts = []
        for curr, output_amount in zip(curr_path, output_amounts):
            rel_output_amounts.append(output_amount / curr.DECIMAL)
        return rel_output_amounts

    def get_amounts_out(self, abs_curr1_amount, checksum_path, block_identifier='latest'):
        amounts_out = self.contract.functions.getAmountsOut(
            amountIn=abs_curr1_amount, path=checksum_path).call(block_identifier=block_identifier)
        return amounts_out

    def get_swap_amounts_out(self, abs_curr1_amount, checksum_path, to_address: str,
                             block_identifier='latest'):
        deadline = get_deadline()
        _to_address = Web3.toChecksumAddress(to_address)
        amounts_out = self.contract.functions.swapExactTokensForTokens(
            amountIn=abs_curr1_amount, amountOutMin=0, path=checksum_path,
            to=_to_address, deadline=deadline).call(block_identifier=block_identifier)
        return amounts_out

    def get_ratio(self, curr_path: list, curr1_amount, show_logs=True, block_identifier='latest'):
        curr1 = curr_path[0]
        curr2 = curr_path[-1]
        output_amounts = self.get_output_amounts(curr_path, curr1_amount, block_identifier)
        curr2_amount = output_amounts[-1]
        # print(curr2_amount)
        # breakpoint()
        curr2_ratio = round(curr2_amount / curr1_amount, 10)
        curr1_ratio = round(curr1_amount / curr2_amount, 10)
        if show_logs:
            logger.info(f"{self.__class__.__name__}: {curr1.__name__}={1}, "
                        f"{curr2.__name__}={curr2_ratio}, or {curr1.__name__}={curr1_ratio}")
        return curr2_ratio, curr2_amount, curr1_ratio

    def swap(self, curr_path: list, curr1_amount, min_curr2_amount, to_address=None):
        curr_in = curr_path[0]
        curr_out = curr_path[-1]
        abs_curr_in_amount = int(curr1_amount * curr_in.DECIMAL)
        abs_curr_out_amount = int(min_curr2_amount * curr_out.DECIMAL)
        checksum_path = list(map(lambda x: Web3.toChecksumAddress(x.ADDRESS), curr_path))
        if to_address is None:
            to_address = self.w3.eth.default_account
        deadline = get_deadline()

        tx_hash = self.contract.functions.swapExactTokensForTokens(
            amountIn=abs_curr_in_amount, amountOutMin=abs_curr_out_amount,
            path=checksum_path, to=to_address, deadline=deadline).transact()
        return tx_hash
