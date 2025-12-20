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
        fl = 0

    origin_name = deep_get(details, ['airport', 'origin', 'name'], 'N/A')
    dest_name = deep_get(details, ['airport', 'origin', 'name'], 'N/A')
    airline = deep_get(details, ['airline', 'name'], 'N/A')
    airline_icao = deep_get(details, ['airline', 'code', 'icao'], 'N/A')
    airline_iata = deep_get(details, ['airline', 'code', 'iata'], 'N/A')
    aircraft = deep_get(details, ['aircraft', 'model', 'text'], 'N/A')
    flight_status  = deep_get(details, ['status', 'text'], 'N/A')

    """If the flight is not scheduled, extract time only (used for notification)"""
    if flight_status != "Scheduled":
        estimated_time = re.search(r'\d{1,2}:\d{2}', flight_status)
        if estimated_time:
            flight_status = estimated_time.group()
        else:
            return flight_status

    if airline_iata is not None and airline_icao is not None:
        logging.info(f"IATA: {airline_iata} of type: {type(airline_iata)} and ICAO: {airline_icao} of type: {type(airline_icao)} found, calling logo function")
        logo = get_logo_image(airline_iata, airline_icao)

    
    else:
        logging.info(
            f"Unable to fetch the logo due to lack of "
            f"IATA: {airline_iata} or ICAO: {airline_icao}."
        )

    # print("=== Flight Data Debug ===")
    # print(f"Airline Name   : {airline}")
    # print(f"Callsign       : {callsign}")
    # print(f"Flight Number  : {number}")
    # print(f"Aircraft       : {aircraft}")
    # print(f"Origin         : {origin_name}")
    # print(f"Destination    : {dest_name}")
    # print(f"Flight Status  : {flight_status}")
    # print(f"Flight Level   : {int(fl)}")
    # print("==========================")


    return {
        "airline_name": airline,
        "callsign": callsign,
        "number": number,
        "aircraft": aircraft,
        "origin": origin_name,
        "destination": dest_name,
        "flight_status": flight_status,
        "flight_level": int(fl),
        "logo" : logo
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
    try:
        logo = fr_api.get_airline_logo(airline_iata, airline_icao)
        filename = f'.//airline_logo.jpg'
        with open(filename, 'wb') as f:
            image = f.write(logo[0])
        return filename
    except:
        return None

def deep_get(data, keys, default=None):
    for key in keys:
        if not isinstance(data, dict):
            return default
        data = data.get(key)
        if data is None:
            return default
    return data