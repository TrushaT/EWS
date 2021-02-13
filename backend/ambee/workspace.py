API = 'RO1vim4vvN4QZB2WNW6jD8TAKkcwEPrR96jmxcM9'
import requests
url = "https://api.ambeedata.com/history/by-lat-lng"
querystring = {"lat":"12.9889055","lng":"77.574044","from":"2021-02-11 12:16:44","to":"2021-02-12 12:16:44"}

headers = {
    'x-api-key': API,
    'Content-type': "application/json"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)