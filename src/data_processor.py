import time
import re 

def get_flight_data(details, callsign, number):
    
            origin_name = details['airport']['origin']['name']
            dest_name = details['airport']['destination']['name']
            airline = details['airline']['name']
            exclude_livery = re.search(r'^([^(]+)', airline)
            aircraft = details['aircraft']['model']['text']

            if exclude_livery:
                airline_name = exclude_livery.group()
            else:
                airline_name = "Unknown"

            airline_icao = details['airline']['code']['icao']
            airline_iata = details['airline']['code']['iata']
            flight_status = details['status']['text']
            estimated_time = re.search(r'\d{1,2}:\d{2}', flight_status)

            if estimated_time:
                time_value = estimated_time.group()
            else:
                time_value = "Unknown"

            return f" Airline: {airline_name} \n Callsign: {callsign} \n Flight number: {number} \n Aircraft Type: {aircraft} \n From: {origin_name} \n To: {dest_name} \n "

