from urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from saludApp.serializers.histClinicaSerializer import HistClinicaSerializer

class CrearHistClinicaView(views.APIView):
    def post(self,request):
        serializer=HistClinicaSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAfrom urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from saludApp.serializers.histClinicaSerializer import HistClinicaSerializer

class CrearHistClinicaView(views.APIView):
    def post(self,request):
        serializer=HistClinicaSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        