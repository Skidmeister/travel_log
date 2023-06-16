'''File handling forms for travel_logs'''
from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
	'''form for a new topic'''
	class Meta:
		model = Topic
		fields = ['text']
		labes = {'text':''}

