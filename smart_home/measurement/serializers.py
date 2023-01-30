from rest_framework import serializers

from measurement.models import Sensor, Measures


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description',]
        
        
class MeasuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measures
        fields = ['sensor', 'measure', 'created_at' ]
        
        
class OneSensorSerializer(serializers.ModelSerializer):
    measurements = MeasuresSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
