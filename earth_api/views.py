from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Satellite
from earth_api import serializers


class RegisterSatellite(APIView):

    serializer_class = serializers.RegisterSatelliteSerializer

    def get(self, request, format=None):
        try:
            port_number = request.query_params.get('port', None)
            Satellite.objects.get(port=port_number)
            message = 'Found'
        except Satellite.DoesNotExist:
            message = 'Not found'
        return Response({'message': message})

    def post(self, request):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            port = serializers.validated_data.get('port')
            message = 'Satellite saved'
            try:
                Satellite(name=name, port=port).save()
            except Exception as e:
                message = e
            return Response({'message': message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


