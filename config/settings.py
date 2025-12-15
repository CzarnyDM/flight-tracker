from FlightRadar24.api import FlightRadar24API
from pathlib import Path

import json
import os

BASE_DIR = Path(__file__).resolve().parent.parent

BASE_LOCATION = "Southampton"

LOCATIONS_FILE = BASE_DIR / "config" / "locations.json"

#get locations
with open(LOCATIONS_FILE, 'r') as file:
    LOCATION = json.load(file)

