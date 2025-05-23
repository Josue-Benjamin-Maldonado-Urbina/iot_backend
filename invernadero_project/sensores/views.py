from rest_framework import viewsets
from .models import RegistroSensor
from .serializers import RegistroSensorSerializer

class RegistroSensorViewSet(viewsets.ModelViewSet):
    queryset = RegistroSensor.objects.all().order_by('-timestamp')
    serializer_class = RegistroSensorSerializer
