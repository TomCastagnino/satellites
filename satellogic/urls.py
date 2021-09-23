from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('ground_control/', include('ground_control.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('earth_api.urls'))
]

