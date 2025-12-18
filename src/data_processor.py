import time
import re 
from src.api_client import fr_api

def get_flight_data(details, flight):

    """ Extract details from the flight data """
    callsign = flight.callsign
    number = flight.number
    fl = flight.get_flight_level()
    origin_name = details.get('airport', {}).get('origin', {}).get('name', " N/A")
    dest_name = details.get('airport', {}).get('destination', {}).get('name' , "N/A")
    airline = details.get('airline', {}).get('name', "N/A")
    airline_icao = details.get('airline', {}).get('code', {}).get('icao', 'N/A')
    airline_iata = details.get('airline', {}).get('code', {}).get('iata', 'N/A')
    aircraft = details.get('aircraft', {}).get('model', {}).get('text', "N/A")
    flight_status = details.get('status', {}).get('text', "N/A")

    """" exclude any livery details from the airline name"""
    exclude_livery = re.search(r'^([^(]+)', airline)
    if exclude_livery:
        airline_name = exclude_livery.group()
    else:
        airline_name = "N/A"

    """ If the flight is not scheduled, extract time only in use for the notification"""
    if flight_status != "Scheduled":
        estimated_time = re.search(r'\d{1,2}:\d{2}', flight_status)
        if estimated_time:
            flight_status = estimated_time.group()
        else:
            return flight_status

    logo = get_logo_image(airline_iata, airline_icao, airline)


    return (f" Airline: {airline_name}  \n Callsign: {callsign} \n Flight number: {number} \n Aircraft Type: {aircraft} \n From: {origin_name} \n To: {dest_name} \n Flight status: {flight_status} ")


def get_logo_image(airline_iata, airline_icao, airline):
    logo = fr_api.get_airline_logo(airline_iata, airline_icao)
    filename = f'.//airline_logo.jpg'
    with open(filename, 'wb') as f:
        image = f.write(logo[0])


