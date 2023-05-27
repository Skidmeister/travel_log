from django.db import models

# Create your models here.

class Topic(models.Model):
	'''A trip the user has undertaken'''
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		'''string representation of the class'''
		return self.text


class Entry(models.Model):
	'''A specific entry to a trip'''
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		'''stirng representation of the entry'''
		return f'{self.text[:50]}...'