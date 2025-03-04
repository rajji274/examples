from django.shortcuts import render

import urllib.request
from . models import Weatherdetails
import json
import requests

def index(request):
    weather_data=[]
    if request.method=='POST':
        city=request.POST['city']
        url=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=imperial&appid=224ef526eb5aa7d1fbb853c6b28a340b')
        city_weather=json.loads(url) 
        weather = {
               
               'city' : city,
               'temperature' : city_weather['main']['temp'],
               'description' : city_weather['weather'][0]['description'],
               'humidity': city_weather['main']['humidity'],
               'pressure': city_weather['main']['pressure'],
               'country': city_weather['sys']['country'],
               'sunrise': city_weather['sys']['sunrise'],
               'sunset': city_weather['sys']['sunset'],
                'windspeed': city_weather['wind']['speed']
                
           } 
        form1=[]
        if weather !=None:  
            if request.method=='POST': 
                form1=Weatherdetails(None,weather['city'],weather['temperature'],weather['description'],weather['humidity'],weather['pressure'],weather['country'],weather['sunrise'],weather['sunset'],weather['windspeed']) 
                form1.save()
        weather_data.append(weather)     
    context = {'weather_data': weather_data}
    return render(request, 'index.html', context)



