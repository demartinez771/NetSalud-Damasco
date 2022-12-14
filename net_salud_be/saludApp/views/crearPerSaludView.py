from urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from saludApp.serializers.pSaludSerializer import PSaludSerializer

class CrearPersonalSaludView(views.APIView):
    def post(self,request):
        serializer=PSaludSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
