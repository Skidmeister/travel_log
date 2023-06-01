from django.shortcuts import render

# Create your views here.

def index(request):
	'''Home page of travel log'''
	return render(request, 'travel_logs/index.html')