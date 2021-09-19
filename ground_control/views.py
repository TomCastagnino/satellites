from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ground_control/index.html')

def satellite(request, satellite_name, number_of_satellites):
    return render(request, 'ground_control/satellite.html', {
        'satellite_name': satellite_name,
        'number_of_satellites': number_of_satellites
    })
