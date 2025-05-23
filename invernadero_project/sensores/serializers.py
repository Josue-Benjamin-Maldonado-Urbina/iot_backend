from rest_framework import serializers
from .models import RegistroSensor

class RegistroSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroSensor
        fields = '__all__'
