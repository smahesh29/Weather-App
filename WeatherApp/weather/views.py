import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm

def index(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=241aa57fc2adaf81d5d55a3d129f6eb5'

        r = requests.get(url.format(city.name)).json()

        city_weather = {
            'id' : city.id,
            'city' : r['name'],
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather/weather.html', context)


def delete(request, id):

    if request.method == 'POST':
        City.objects.filter(id=id).delete()

    return redirect('/')