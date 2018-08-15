import requests
from django.shortcuts import render


# Create your views here.
def hello(request, name='Morrisa'):
    return render(request, "weather/hello.html", {'name': name})


def get_forecast_latlon(request, lat, lon):
    endpoint = 'https://api.weather.gov/points/{lat},{lon}/forecast'
    forecast_data = requests.get(endpoint.format(lat=lat, lon=lon))
    dir_strs = get_dir_strs(forecast_data)
    return render(request, "weather/forecast_temp.html",
                  {'now_data': forecast_data.json()['properties']['periods'][0], 'now_dir': dir_strs[0]})


def get_dir_strs(forecast_data):
    dir_strs = {}
    for i in range(len(forecast_data.json()['properties']['periods'])):
        wind_dir = forecast_data.json()['properties']['periods'][i]['windDirection']
        cur_str = ""
        if "N" in wind_dir:
            cur_str = "North"
        elif "S" in wind_dir:
            cur_str = "South"

        if "E" in wind_dir:
            if cur_str:
                cur_str += "east"
            else:
                cur_str = "East"
        elif "W" in wind_dir:
            if wind_dir.find("W") == 0:
                cur_str = "West"
            else:
                cur_str = cur_str + "west"

        dir_strs[len(dir_strs)] = cur_str
    return dir_strs
