from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('weather_info', views.weather_info, name = "weather_info"),
    path('weather', views.weather, name = "weather"),
    path('registration', views.registration, name = "registration"),
    path('Login', views.Login, name = "Login"),
    path('About', views.About, name = "About"),




]