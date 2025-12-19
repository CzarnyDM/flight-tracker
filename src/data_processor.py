import time
import re 
from src.api_client import fr_api
from config.settings import DEFAULT_ALT
import logging



def get_flight_data(details, flight):

    """ Extract details from the flight data """
    callsign = flight.callsign
    number = flight.number
    fl = flight.get_altitude()

    extract_int = re.search(r'\d+', fl)
    if extract_int:
        fl = extract_int.group()
    else:
        fl = "N/A"

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
    if airline_iata and airline_icao is not None:
        logo = get_logo_image(airline_iata, airline_icao)

    return {
        "airline_name": airline_name,
        "callsign": callsign,
        "number": number,
        "aircraft": aircraft,
        "origin": origin_name,
        "destination": dest_name,
        "flight_status": flight_status,
        "logo": logo,
        "flight_level": int(fl)
    }

def check_fl(flight_data):
    alt = flight_data['flight_level']
    nr = flight_data['number']
    if alt > DEFAULT_ALT:
        print(f"Discarded the flight {nr} because it is above 10k feet.")
        logging.info(f"Discarded the flight {nr} because it is above 10k feet.")
        return
    
    else:
        return True

def message(flight_data):
    msg = (
        f" Airline: {flight_data['airline_name']}\n"
        f" Callsign: {flight_data['callsign']}\n"
        f" Flight number: {flight_data['number']}\n"
        f" Aircraft Type: {flight_data['aircraft']}\n"
        f" From: {flight_data['origin']}\n"
        f" To: {flight_data['destination']}\n"
        f" Flight status: {flight_data['flight_status']}\n"
        f" Flight level: {flight_data['flight_level']}"
    )

    logging.info(msg)
    print(msg)
    return msg

def get_logo_image(airline_iata, airline_icao):
    logo = fr_api.get_airline_logo(airline_iata, airline_icao)
    filename = f'.//airline_logo.jpg'
    with open(filename, 'wb') as f:
        image = f.write(logo[0])


