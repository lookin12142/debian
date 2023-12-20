from rest_framework.decorators import api_view
from rest_framework.response import Response
from cord import serializers
from .serializers import GPSSerializer
from .models import GPS

@api_view()
def getUbi(request):
        ubicacion = GPS.objects.all()
        serializer = GPSSerializer(ubicacion, many=True)
        return Response(serializer.data)

        


