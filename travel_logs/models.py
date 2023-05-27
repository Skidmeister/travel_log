from django.db import models

# Create your models here.

class Topic(models.Model):
	'''A trip the user has undertaken'''
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		'''string representation of the class'''
		return self.text