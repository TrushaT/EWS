from django.shortcuts import render
import json
import requests
from backend.settings import API_KEY

def getpollendata():
    url = "https://api.ambeedata.com/forecast/pollen/by-place"
    querystring = {"place":"Mumbai"}
    headers = {
    'x-api-key': API_KEY,
    'Content-type': "application/json"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    grass_pollen = str(json_data["Risk"]["grass_pollen"])
    return grass_pollen

def getaqi():
    url = "https://api.ambeedata.com/latest/by-city"
    querystring = {"city":"Bengaluru"}
    headers = {
    'x-api-key': API_KEY,
    'Content-type': "application/json"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    aqi = json_data["stations"]["aqiInfo"]
    return aqi

def getweather():
    url = "https://api.ambeedata.com/weather/forecast/by-lat-lng"
    querystring = {"lat":"12.9889055","lng":"77.574044","filter":"{hourly|minutely|daily}"}
    headers = {
        'x-api-key': API_KEY,
        'Content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    forecast = json_data['data'][forecast]
    return forecast




    


# Create your views here.
