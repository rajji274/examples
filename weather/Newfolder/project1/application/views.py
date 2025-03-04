from django.shortcuts import render,redirect
from django.contrib.auth import login as dj_login
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages
from application.models import Register
from application.serializers import RegisterSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from application.forms import Registerform
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from application.tokens import account_activation_token


@csrf_exempt
def login(request):
    return render(request,"login.html")


#weather report
from datetime import datetime
from traceback import format_list
from django.shortcuts import render
import requests
from .models import Weatherdetails
from .forms import Weatherform
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json
# Create your views here.
@csrf_exempt
def index(request):
    weather_data=[]
    city=''
    data1=[]
    weather={}
    date_time=[]
    temperature=[]
    description=[]
    icon=[]
    humidity=[]
    pressure=[]
    windspeed=[]
    weatherList={}
    form1=[]
    form2={}
    if request.method == 'POST':
        city = request.POST['city']
        print(city)
        # url='https://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=224ef526eb5aa7d1fbb853c6b28a340b'
        url = 'https://api.openweathermap.org/data/2.5/forecast?appid=224ef526eb5aa7d1fbb853c6b28a340b&units=metric'
        url+= '&q=' + city
        city_weather= requests.get(url).json()      
        for data1 in city_weather['list']:
            time=data1['dt_txt']
            date, hour = time.split(' ')
            form2={
            'city':city,
            'date':date,
            'hour' : hour,
            'temperature' : data1['main']['temp'],
            'description': data1['weather'][0]['description'],
            'icon': data1['weather'][0]['icon'],
            'humidity': data1 ['main']['humidity'],
            'pressure':  data1['main']['pressure'],
            'windspeed': data1['wind']['speed']     
            }
            weatherList = Weatherdetails.objects.filter(city=form2['city']).filter(date=form2['date']).filter(hour=form2['hour']).values()
            while len(weatherList)>0:
                if weatherList[0]['city']==form2['city'] and weatherList[0]['date']==form2['date']:
                    print("enter into if")
                    form1=Weatherdetails(weatherList[0]['id'],form2['city'],form2['date'],form2['hour'],form2['temperature'],form2['description'],form2['icon'],form2['humidity'],form2['pressure'],form2['windspeed'])
                    form1.save()
                    break
            else:
                print("form2",form2)
                form3=Weatherdetails(None,form2['city'],form2['date'],form2['hour'],form2['temperature'],form2['description'],form2['icon'],form2['humidity'],form2['pressure'],form2['windspeed'])
                print(form3,"data saved")
                form3.save()
                
                
            weather_data.append(form2)
        weather={'weather_data':weather_data}         
    return render(request, 'index.html',weather)
    
def view_data(request):
    display_data=Weatherdetails.objects.all()
    return render(request,"get_data.html",{'display_data':display_data})




