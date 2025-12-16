import re
from utils.geo import get_coordinates
from src.api_client import fr_api
from src.data_processor import get_flight_data
import time

seen_flights = set()

def detect_flight():
    while True:
        # norht lat, south lat, west long, east long
        flights = get_coordinates()

        if flights:
            for flight in flights:

                flight_key = flight.callsign or flight.id 
                callsign = flight.callsign
                number = flight.number

                # prevent from duplicate entries
                if flight_key in seen_flights:
                    continue
                seen_flights.clear() 
                seen_flights.add(flight_key)

                details = fr_api.get_flight_details(flight)
                get_flight_data(details, callsign, number)            
        else:
            print("No flights detected.")
        
        time.sleep(10)