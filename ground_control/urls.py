from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:satellite_name>/<str:number_of_satellites>/', views.satellite, name='satellite'),
]