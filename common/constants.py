import os
import time
from pathlib import Path

os.environ['TZ'] = 'GMT'
time.tzset()

CAN_BREAKPOINT = os.environ.get("CAN_BREAKPOINT", False) == "true"
if CAN_BREAKPOINT:
    print(f"{CAN_BREAKPOINT=}")

DATA_FOLDER = Path("data")
KEYS_FOLDER = Path("data_account_keys")
DEFAULT_ADDRESS = "default_address"
