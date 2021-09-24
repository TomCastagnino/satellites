from django.urls import path

from earth_api import views


urlpatterns = [
    path('register_satellite/', views.RegisterSatellite.as_view()),
    path('task_results/', views.TaskResults.as_view()),
    path('start_button/', views.StartButton.as_view()),
]