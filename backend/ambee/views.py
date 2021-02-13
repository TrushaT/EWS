from django.shortcuts import render
import json
from geopy.geocoders import Nominatim
import requests
from rest_framework.parsers import JSONParser
import validators
from backend.settings import API_KEY
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

 

def getpollendata(place):
    url = "https://api.ambeedata.com/forecast/pollen/by-place"
    querystring = {"place":place}
    headers = {
    'x-api-key': API_KEY,
    'Content-type': "application/json"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    print(json_data[-1]["Risk"])
    grass_pollen = json_data[-1]["Risk"]
    return grass_pollen

def getaqi(place):
    url = "https://api.ambeedata.com/latest/by-city"
    querystring = {"city": place}
    headers = {
    'x-api-key': API_KEY,
    'Content-type': "application/json"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    aqi = json_data['stations'][0]["aqiInfo"]["category"]
    return aqi

def getweather(place):
    geolocator =  Nominatim(user_agent="dexterex")
    location = geolocator.geocode(place)
    url = "https://api.ambeedata.com/weather/latest/by-lat-lng"
    querystring = {"lat":location.latitude,"lng":location.longitude}
    headers = {
        'x-api-key': API_KEY,
        'Content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    #print(json_data)
    temperature = json_data['data']["temperature"]
    humidity = json_data['data']["humidity"]
    windSpeed = json_data['data']["windSpeed"]
    return temperature, humidity, windSpeed

@csrf_exempt
def test(request):
    if request.method == 'POST':
        # print(request.POST.get('location'))
        # data = JSONParser().parse(request)
        data_list = request.POST.get('location')
        # places = []
        # for data in data_list:
        #     if(not validators.url(data)):
        #         places.append(data)
        
        # place = places[0]
        # response = {}
        # response['pollen'] = getpollendata(place)
        # response['aqi'] = getaqi(place)
        # response['temperature'], response['humidity'], response['windSpeed'] = getweather(place)
        return JsonResponse({"response":'true'},safe=False)
    






