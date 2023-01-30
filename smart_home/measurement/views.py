
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.serializers import SensorSerializer, MeasuresSerializer, OneSensorSerializer
from measurement.models import Measures, Sensor

class SensorsList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
class OneSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = OneSensorSerializer
        
class Measure(ListCreateAPIView):
    queryset = Measures.objects.all()
    serializer_class = MeasuresSerializer
    