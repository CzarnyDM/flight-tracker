from pathlib import Path
import logging
import json
import os
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_LOCATION = "Chicago"
LOCATIONS_FILE = BASE_DIR / "config" / "locations.json"
DEFAULT_ALT = 10000

date_and_time = datetime.now().strftime('%Y%m%d_%H%M%S')
date = datetime.now().strftime('%Y_%m_%d')
time = datetime.now().strftime('%H_%M_%S')

logs_dir = f"./logs/"
date_file = os.makedirs(logs_dir, exist_ok=True)


with open(LOCATIONS_FILE, 'r') as file:
    locations = json.load(file)
COORDINATES = locations['locations'][BASE_LOCATION]


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # capture everything

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# INFO log
info_handler = logging.FileHandler(f"{logs_dir}/{date_and_time}.log")
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

# # WARNING+ log
# warning_handler = logging.FileHandler(f"{logs_dir}/details_{time}.log")
# warning_handler.setLevel(logging.WARNING)
# warning_handler.setFormatter(formatter)

logger.addHandler(info_handler)
# logger.addHandler(warning_handler)
