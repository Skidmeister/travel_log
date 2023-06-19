'''File handling forms for travel_logs'''
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	'''form for a new topic'''
	class Meta:
		model = Topic
		fields = ['text']
		labes = {'text':''}

class EntryForm(forms.ModelForm):
	'''form for a new entry for a topic'''
	class Meta:
		model = Entry
		fields = ['text']
		labels={'text':''}
		widgets = {'text':forms.Textarea(attrs={'cols':80})}
