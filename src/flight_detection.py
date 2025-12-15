from FlightRadar24 import *
import re


fr_api = FlightRadar24API()

seen_flights = set()

def detect_flight():
    while True:

        # norht lat, south lat, west long, east long
        flights = fr_api.get_flights(bounds="51.481329,51.456842,-0.424862,-0.363836")

        if flights:
            for flight in flights:

                flight_key = flight.callsign or flight.id 

                if flight_key in seen_flights:
                    continue
                seen_flights.clear() 
                seen_flights.add(flight_key)

                details = fr_api.get_flight_details(flight)
                origin_name = details['airport']['origin']['name']
                dest_name = details['airport']['destination']['name']
                airline = details['airline']['name']

                exclude_livery = re.search(r'^([^(]+)', airline)

                if exclude_livery:
                    airline_name = exclude_livery.group()
                else:
                    print("Unknown")

                airline_icao = details['airline']['code']['icao']
                airline_iata = details['airline']['code']['iata']
                flight_status = details['status']['text']
                estimated_time = re.search(r'\d{1,2}:\d{2}', flight_status)

                if estimated_time:
                    time_value = estimated_time.group()
                else:
                    print("Unknown")

                aircraft = details['aircraft']['model']['text']
                print("*" * 50)
                print(f" Airline: {airline_name} \n Callsign: {flight.callsign} \n Flight number: {flight.number} \n Aircraft Type: {aircraft} \n From: {origin_name} \n To: {dest_name} \n Scheduled time: {time_value} \n  ")
                print("*" * 50)


        else:
            print("No flights detected.")
        
        time.sleep(10)