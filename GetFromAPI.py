import json
import requests
import time

LatitudeDict = {'New York': 40.741775306237756, 'Washington': 38.89458198502483, 'Los Angeles': 33.88666371103062,
                'Istanbul': 41.043662307738096, 'Roma': 41.8882829747944, 'Berlin': 52.513908537962045 ,
                'Ankara' : 39.931467044255264}

LongitudeDict = {'New York': -73.97562370387732, 'Washington': -77.03930519969299, 'Los Angeles': -118.06569334643915,
                 'Istanbul': 29.01167159715636, 'Roma': 12.491002706568507, 'Berlin': 13.402708997868762,
                 'Ankara' : 32.8078353733421}

RadiusDict = {'New York': 61.555075594, 'Washington': 26.9978401728, 'Los Angeles': 92.3326133909,
              'Istanbul': 18.898488121, 'Roma': 10.7991360691, 'Berlin': 16.7386609071,
              'Ankara': 13.282937365}


def write_data_to_json(data):
    with open('flight_data.json', 'w') as flight_data:
        json.dump(data, flight_data, indent=4)


def load_flight_data():
    url = "https://api.adsb.lol/v2/ladd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        write_data_to_json(data)
        return True
    else:
        print("There was an error while fetching data")
        return False


def load_precise_data(city_name):
    lat = LatitudeDict.get(city_name)
    lon = LongitudeDict.get(city_name)
    radius = round(RadiusDict.get(city_name))
    url = f"https://api.adsb.lol/v2/point/{lat}/{lon}/{radius}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        write_data_to_json(data)
        return True
    elif response.status_code == 422:
        print(response.json())
    else:
        print("There was an error while fetching precise data")
        return False
