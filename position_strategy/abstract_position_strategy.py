from enum import Enum


class Position(Enum):
    BUY = "buy"
    SELL = "sell"
    NO_POS = "no_pos"


class AbstractPositionStrategy:
    def get_latest_position(self) -> Position:
        raise NotImplementedError
