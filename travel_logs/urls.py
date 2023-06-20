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
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	#site to introduce a new topic
	path('new_topic/', views.new_topic, name='new_topic'),
	#site to introduce a new entry for a topic
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	#editing of entries
	path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry')
	]