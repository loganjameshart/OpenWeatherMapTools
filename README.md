# OpenWeatherMapTools

Basic functions for interacting with the free version of the OpenWeatherMap API. Also provides a means of sending the received weather info via SMTP (requires a separate outside email account).

## Overview

My main motiviation for this project was to become familiar with the process of interacting with online APIs (GET requests, receiving and parsing JSON info, etc.). It works by using the requests module to deliver a payload of inputted data (city name and state) to the OpenWeatherMap API. From there, the information is parsed to get the current weather and temperature of the requested location.

## Requirements

A free OpenWeatherMap account (https://openweathermap.org/).
The Requests module (https://pypi.org/project/requests/).


