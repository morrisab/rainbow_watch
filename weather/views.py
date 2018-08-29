import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from rainbow_watch.settings import GEONAMES_USER
from weather.models import Location


def get_forecast_zip(request, zip_code):
    zip_entry = Location.objects.get_or_create(zip=zip_code)
    if zip_entry[1]:
        geonames_endpoint = 'http://api.geonames.org/postalCodeSearchJSON?postalcode={zip}&country=US&username={user}'
        zip_data = requests.get(geonames_endpoint.format(zip=zip_code, user=GEONAMES_USER))
        # Location.objects.update(zip=zip_code, lat=zip_data.json()['postalCodes'][0]['lat'],
        #                         lon=zip_data.json()['postalCodes'][0]['lng'])
    final_endpoint = '/forecast/{lat},{lon}'
    # forecast_data = requests.get(final_endpoint.format(lat=zip_data.json()['postalCodes'][0]['lat'],
    #                                                    lon=zip_data.json()['postalCodes'][0]['lng']))
    return HttpResponseRedirect(final_endpoint.format(lat=zip_data.json()['postalCodes'][0]['lat'],
                                                       lon=zip_data.json()['postalCodes'][0]['lng']))
    # dir_strs = get_dir_strs(forecast_data)
    # return render(request, "weather/forecast_temp.html",
    #               {'now_data': forecast_data.json()['properties']['periods'][0], 'now_dir': dir_strs[0]})
    # zip_entry = Location.objects.get_or_create(zip=zip_code)
    # if zip_entry[1]:
    #     endpoint = 'http://api.geonames.org/postalCodeSearchJSON?postalcode={zip}&username={user}'
    #     zip_data = requests.get(endpoint.format(zip=zip_code, user=GEONAMES_USER))
    # return render(request, "weather/generic_display.html", {'data': zip_data})


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
