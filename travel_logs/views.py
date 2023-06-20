from django.shortcuts import render, redirect

from .models import Topic, Entry

from .forms import TopicForm, EntryForm

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

def new_topic(request):
	'''Page to introduce a new topic'''
	if request.method != 'POST':
		#no data submitted, create a blank form
		form = TopicForm()
	else:
		#POST data submitted
		form =TopicForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('travel_logs:topics')

	#Display blank form
	context ={'form':form}
	return render(request, 'travel_logs/new_topic.html', context)

def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	
	if request.method != 'POST':
		form = EntryForm()

	else:
		#Post data
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('travel_logs:topic', topic_id=topic_id)

	#Display a blank or invalid form
	context = {'topic':topic, 'form':form}
	return render(request, 'travel_logs/new_entry.html', context)


def edit_entry(request, entry_id):
	'''page to edit an entry'''
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		form = EntryForm(instance=entry)

	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('travel_logs:topic', topic_id=topic.id)

	context = {'form':form, 'topic':topic, 'entry':entry}
	return render(request, 'travel_logs/edit_entry.html', context)













