from django.urls import path
from.views import SensorsViewSet

urlpatterns = [
    path('farm/get/soil-moisture', SensorsViewSet.as_view({'get': 'get_soil'}), name='get_soil'),
    path('farm/send/actuator', SensorsViewSet.as_view({'get': 'send_actuator'}), name='send_actuator'),
]