import re
from utils.geo import get_coordinates
from src.api_client import fr_api
from src.data_processor import get_flight_data, message, check_fl
from src.notifier import send_notification
import time
import logging

seen_flights = set()

valid_flight = True

def detect_flight():
    logging.info("Starting the script")
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
                logging.info(f"Details: {details}")

                flight_info = get_flight_data(details, flight)

                if check_fl(flight_info) is True:
                    formatted_message = message(flight_info)
                    send_notification(formatted_message)
                    time.sleep(10)
                else:
                    continue

        else:
            logging.info("No flight detected.")
            print("No flights detected.")
        
        time.sleep(10)
