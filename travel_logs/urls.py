'''Defines URL patterns for travel_logs app'''

from django.urls import path
from . import views

app_name = 'travel_logs'

urlpatterns = [
	#home-page
	path('', views.index, name='index'),
	#page with all the listed topics
	path('topics/', views.topics, name='topics'),
	#detail page for a single topic
	path('topics/<int:topic_id>/', views.topic, name='topic')
	]