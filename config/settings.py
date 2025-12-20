from pathlib import Path
import logging
import json
import os
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent
BASE_LOCATION = "Chicago"
LOCATIONS_FILE = BASE_DIR / "config" / "locations.json"
DEFAULT_ALT = 10000
DATE_AND_TIME = datetime.now().strftime('%Y%m%d_%H%M%S')

with open(LOCATIONS_FILE, 'r') as file:
    locations = json.load(file)
COORDINATES = locations['locations'][BASE_LOCATION]

# Logging
logging.basicConfig(
    filename=f"./logs/log_{DATE_AND_TIME}.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def save_to_file(content, file_name):
    with open(f"./logs/{file_name}.txt", "a") as f:
        f.write(content)
