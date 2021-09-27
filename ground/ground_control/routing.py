from django.urls import re_path 
from .consumers import satellite_consumer, earth_consumer

websocket_urlpatterns = [
    re_path(r'ws/ground_control/earth/(?P<number_of_satellites>\w+)/$', earth_consumer.EarthConsumer.as_asgi()),
    re_path(r'ws/ground_control/(?P<satellite_name>\w+)/$', satellite_consumer.SatelliteConsumer.as_asgi()),
]