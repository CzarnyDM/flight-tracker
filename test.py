from FlightRadar24.api import FlightRadar24API
import pygame
import requests
from io import BytesIO
from PIL import Image

fr_api = FlightRadar24API()

# min_lat = 50.8500000
# max_lat = 50.9650000
# min_lon = -1.4950000
# max_lon = -1.3200000

# Get flights in your area
flights = fr_api.get_flights(bounds="50.1,49.95,19.75,20.0")




# Loop through the list directly
for flight in flights:
    details = fr_api.get_flight_details(flight)
    origin_name = details['airport']['origin']['name']
    dest_name = details['airport']['destination']['name']
    airline = details['airline']['name']
    airline_icao = details['airline']['code']['icao']
    airline_iata = details['airline']['code']['iata']
    # logo = fr_api.get_airline_logo(airline_icao, airline_iata)

    # print("*" * 50)
    # print(f" Airline: {airline} \n Flight number: {flight.number} \n From: {origin_name} \n To: {dest_name} ")
    # print(logo)
    # print("*" * 50)
    # print(f"Callsign: {flight.callsign}")
    # print("---")
    # print(f"From: {flight.origin_airport_iata}")
    # print(f"To: {flight.destination_airport_iata}")

