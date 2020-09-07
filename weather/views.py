from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from .forms import UserForm
from .models import Member
from django.contrib.auth import authenticate
def weather(request):
    return render(request, "weather.html")

def registration(request):
    if request.method == "POST":
        Username = request.POST['Username']
        obj = Member.objects.all()
        for item in obj:
            if item.Username == Username:
                messages.info(request, "User already exists...!")
                return redirect('registration')
            else:
                form = UserForm(request.POST)
                form.save()
                messages.error(request, "Registration Successful...!")
                return redirect('registration')

    form = UserForm()

    context = {'form' : form}
    return render(request, "register.html", context)

def Login(request):
    if request.method == "POST":
        Username = request.POST['Username']
        Password = request.POST['Password']
        obj = Member.objects.all()
        for item in obj:
            if item.Username == Username:
                if item.Password1 == Password:
                    messages.info(request,"login successful...!")
                    return redirect('Login')
                else:
                    messages.info(request, "Invalid credentials...!")
                    return redirect('Login')
        #print(Username)
        #print(Password)
      #  form.save()
    form = UserForm()

    context = {'form' : form}
    return render(request, "login.html", context)

def home(request):
    return render(request, "home.html")

def About(request):
    return render(request, "about.html")

def weather_info(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=078d5756f17bf0a25d9ef2fa99846ae7'
    city = (request.POST["city_name"])
    print(city)
    r = requests.get(url.format(city)).json()
    #  weather_data = []
    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    # weather_data.append(city_weather)
    # print(weather_data)
    context = {'city_weather': city_weather}


    return render(request, "City.html", context)
