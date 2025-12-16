
from src.api_client import fr_api
from config.settings import COORDINATES
import json 

def get_coordinates():
    return fr_api.get_flights(bounds=COORDINATES)