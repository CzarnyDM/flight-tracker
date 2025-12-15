
from src.api_client import fr_api
from config.settings import LOCATION
import json 


def get_coordinates():
    return fr_api.flights(bounds=LOCATION)