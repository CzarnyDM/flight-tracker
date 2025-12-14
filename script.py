from opensky_api import OpenSkyApi
import requests
import json

#CONSTANTS
# Southampton (EGHI)
# min_lat = 50.8500000
# max_lat = 50.9650000
# min_lon = -1.4950000
# max_lon = -1.3200000

# Krakow Airport (EPKK) area
min_lat = 49.9500000
max_lat = 50.1000000
min_lon = 19.7500000
max_lon = 20.0000000

def get_callsign():

    #assign API Class
    api = OpenSkyApi()

    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states(bbox=(min_lat, max_lat, min_lon, max_lon))

    for s in states.states:
        callsign = s.callsign
        print(callsign)
        get_flight_info()

def get_flight_info():

    params_arr = {
        'flight_icao' : "W62046",
        'access_key': 'a465560855061c051cd7a364762271d8',
        'limit' : 1,
        # 'arr_icao' : 'EPKK'
      
}

#     params_dep = {
#         'flight_icao' : "W62046",
#         'access_key': 'a465560855061c051cd7a364762271d8',
#         'limit' : 1,
#         # 'dep_icao' : 'EPKK'
      
# }
    
    api_result_arr = requests.get('https://api.aviationstack.com/v1/flights', params_arr)
    # api_result_dep = requests.get('https://api.aviationstack.com/v1/flights', params_dep)

    api_response_arr = api_result_arr.json()
    print(api_response_arr)

    with open("json_arr.json", "w") as f:
       json.dump(api_response_arr, f)

    # api_response_dep = api_result_dep.json()
    # with open("json_dep.json", "w") as f:
    #   json.dump(api_response_dep, f)


get_callsign()
# def get_flight_info(callsign):
