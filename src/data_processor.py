from ..config.settings import BASE_LOCATION
import time
import json
import re
import os

# IDEAS:
# - Add geo-cordinates based on the location or allow to insert the address and export it from that.


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

seen_flights = set()
geo = ""



