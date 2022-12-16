"""
Providing tools for interacting with OpenWeatherMap API for the United States.

Requires an account with OpenWeatherMap (https://openweathermap.org/). 

This module follows the free version, which allows only immediate weather information or a 5-day, 3-hour forecast. 
"""

import requests
import smtplib
import time

# openweathermap api info
APIKEY = ""
LOCATIONAPI = "http://api.openweathermap.org/geo/1.0/direct?"
WEATHERAPI = "https://api.openweathermap.org/data/2.5/weather?"
USACOUNTRYCODE = 840

# email SMTP info
SENDEREMAIL = ""
SENDERPASSWORD = ""
RECEIVEREMAIL = ""
SMTPSERVER = ""


def get_coordinates(city_name: str, state_abbreviation: str) -> dict:
    """Takes city name and state as arguments to return a coordinate dictionary."""
    
    info_dict = {
        "q": f"{city_name},US-{state_abbreviation},{USACOUNTRYCODE}",
        "appid": APIKEY
    }

    location = requests.get(LOCATIONAPI, params=info_dict)
    location_info = location.json()
    lat_long = {"lat": location_info[0]["lat"], "lon": location_info[0]["lon"]} #parse json file from request to get latitude and longitude
    return lat_long

def get_weather(location_coordinates: dict) -> dict:
    """Takes city coordinate dictionary as argument and returns current weather for that city as JSON."""

    login_info = {**location_coordinates, "appid": APIKEY}
    r = requests.get(WEATHERAPI, params=login_info)
    weather_dictionary = r.json()
    return weather_dictionary

def weather_parser(weather_json: dict) -> str:
    '''Parses JSON file for current weather status and temperature.'''

    weather_overview = weather_json["weather"][0]["description"]
    weather_temperature_kelvin = weather_json["main"]["temp"]
    weather_temperature_fahrenheit = int((1.8*(weather_temperature_kelvin-273)+32))
    weather_temperature_celsius = (weather_temperature_kelvin-273.15)
    return f"{weather_overview}, {weather_temperature_fahrenheit} degrees F/{weather_temperature_celsius} degrees C."

def email_weather(weather_message: str, city: str, state: str):
    '''Sends basic email message containing requested weather. 
    Uses pre-defined constants for sender and receiver addresses.'''

    smtpObj = smtplib.SMTP(SMTPSERVER, 587)
    smtpObj.ehlo()
    time.sleep(1)
    smtpObj.starttls()
    time.sleep(1)
    smtpObj.login(SENDEREMAIL, SENDERPASSWORD)
    time.sleep(1)
    smtpObj.sendmail(SENDEREMAIL, RECEIVEREMAIL, f'Subject: Weather now in {city}, {state}.\nRight now it is {weather_message} in {city}, {state}.')
    smtpObj.quit()



def main():
    requested_city = input("Please enter your city. ")
    requested_state = input("Please enter your state abbreviation. ")
    requested_coordinates = get_coordinates(requested_city, requested_state)
    requested_weather = get_weather(requested_coordinates)
    requested_weather_output = weather_parser(requested_weather)
    email_weather(requested_weather_output, requested_city, requested_state)

if __name__ == "__main__":
    main()
