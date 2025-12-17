import re
from utils.geo import get_coordinates
from src.api_client import fr_api
from src.data_processor import get_flight_data
from src.notifier import send_notification
import time

seen_flights = set()

def detect_flight():
    while True:
        # norht lat, south lat, west long, east long
        flights = get_coordinates()

        if flights:
            for flight in flights:
                
                flight_key = flight.callsign or flight.id 
                # prevent from duplicate entries
                if flight_key in seen_flights:
                    continue
                
                seen_flights.clear() 
                seen_flights.add(flight_key)

                details = fr_api.get_flight_details(flight)
                flight_info = get_flight_data(details, flight)
                return details, flight

                # push it via notification
                send_notification(flight_info)
        else:
            print("No flights detected.")
        
        time.sleep(10)