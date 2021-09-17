from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:satellite_name>/', views.satellite, name='satellite'),
]