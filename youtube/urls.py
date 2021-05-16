from .views import *
from django.urls import path, include



urlpatterns = [
	path('', index, name='index'),
	# path('download/', download, name='download'),
	# path('downloading/', downloading, name='downloading')
	

	path('home/', greetings, name='home'),
    path('home/download/', download, name='download'),
    path('home/downloading/', downloading, name='downloading'),
]
