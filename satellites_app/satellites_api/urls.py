from django.urls import path
from satellites_api import views

urlpatterns = [
    path('health/', views.Health.as_view()),
    path('tasks/', views.TasksView.as_view())
]
