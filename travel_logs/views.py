from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
	'''Home page of travel log'''
	return render(request, 'travel_logs/index.html')

def topics(request):
	'''Page presenting all trips that were added by the user'''
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'travel_logs/topics.html', context)

def topic(request, topic_id):
	'''Page for a single trip with all its entries'''
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries':entries}
	return render(request, 'travel_logs/topic.html', context)