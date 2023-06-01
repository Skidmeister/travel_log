'''Defines URL patterns for travel_logs app'''

from django.urls import path
from . import views

app_name = 'travel_logs'

urlpatterns = [
	path('', views.index, name='index'),
	]