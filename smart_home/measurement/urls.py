from django.urls import path

from measurement.views import SensorsList, Measure, OneSensor

urlpatterns = [
    path('sensors/', SensorsList.as_view(),name='sensors'),
    path('measurements/', Measure.as_view(), name='measures'),
    path("sensors/<pk>/", OneSensor.as_view(), name="sensor")
]
