from django.urls import path
from findweather import views

urlpatterns = [
    path('', views.home, name='home'),
]
