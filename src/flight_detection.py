import re
from utils.geo import get_coordinates
from src.api_client import fr_api
from src.data_processor import get_flight_data, message, check_fl
from src.notifier import send_notification
from config.settings import BASE_LOCATION, save_to_file
import time
import logging

seen_flights = set()

valid_flight = True

logging.info(f"Current locaiton is {BASE_LOCATION}")
print(f"Current locaiton is {BASE_LOCATION}")
        
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
                    print(f"Duplicate flight {flight_key}")
                    logging.info(f"Duplicate flight {flight_key}")
                    continue

                seen_flights.clear() 
                seen_flights.add(flight_key)

                details = fr_api.get_flight_details(flight)
                save_to_file(details, "details")
                # logging.info(f"Details: {details}")

                flight_info = get_flight_data(details, flight)
                # print(f"Current flight info in detection {flight_info}")

                # Capture any errors from the API if not returned as dict
                if not isinstance(flight_info, dict):
                    logging.info("Details not returning dictonary, aborting the flight.")
                    continue

                else:
                    check_fl(flight_info)
                    # capture all flights that are within the specified FL
                    if check_fl(flight_info) is True:
                        send_notification(message(flight_info))
                    else:
                        continue
                time.sleep(5)



        else:
            logging.info("No flight detected.")
            print("No flights detected.")
        
        time.sleep(5)
