from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectTeam

def teams(request):
	context = {
		'projectteams': ProjectTeam.objects.all()
	}
	return render(request, 'resource_hopper/teams.html', context)

def home(request):
	return HttpResponse('<h1>Home Page</h1>')

