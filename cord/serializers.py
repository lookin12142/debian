from rest_framework.serializers import ModelSerializer
from .models import GPS

class GPSSerializer(ModelSerializer):
    class Meta:
        model = GPS
        fields = ['longitud','latitud']