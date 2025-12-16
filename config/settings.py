from pathlib import Path

import json
import os

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_LOCATION = "New York"
LOCATIONS_FILE = BASE_DIR / "config" / "locations.json"


with open(LOCATIONS_FILE, 'r') as file:
    locations = json.load(file)
COORDINATES = locations['locations'][BASE_LOCATION]
