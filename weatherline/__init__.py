from weatherline import config
import json
import requests
import argparse

'''
Usage:
    weather -z 08852
Options:
    -z zipcode               
'''


def get_weather(place, lat, long):
    url = config.DARKSKYAPI.format(config.ds_api_secret, lat, long)
    response = requests.get(url)
    response_json = json.loads(response.text)

    currently = response_json["currently"]
    summary = currently["summary"]
    temperature = currently["temperature"]
    apparent_temperature = currently["apparentTemperature"]
    chance_of_rain = currently["precipProbability"]

    print(f" Hi, the weather in {place}\n"
          f" is {summary}. It is currently {temperature}F with a real feel of {apparent_temperature}F.\n"
          f" There is {chance_of_rain}% chance of rain.")


def get_coordinates(zipcode):
    place = ""
    lat = 0.0
    long = 0.0

    url = config.GOOGLEMAPSAPI.format(zipcode, config.gm_api_key)
    response = requests.get(url)
    response_json = json.loads(response.text)

    results = response_json["results"]

    for result in results:
        address = result["address_components"][1]
        place = address["long_name"]
        if result["geometry"]["location"]:
            lat = result["geometry"]["location"]["lat"]
            long = result["geometry"]["location"]["lng"]

    return place, lat, long


def __main__():
    parser = argparse.ArgumentParser(description='Whats the Weather?')
    parser.add_argument('-z','--zipcode',  help='zip code for weather')
    args = parser.parse_args()
    place, lat, long = get_coordinates(args.zipcode)
    get_weather(place, lat, long)
