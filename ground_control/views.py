from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    return render(request, 'ground_control/index.html')

def satellite(request, satellite_name, number_of_satellites):
    context = {
        'satellite_name': satellite_name,
        'number_of_satellites': number_of_satellites
    }
    return render(request, 'ground_control/satellite.html', context)
    
def tasks(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render (request, 'ground_control/tasks.html', context)
