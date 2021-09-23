from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Satellite, Task
from earth_api import serializers


class RegisterSatellite(APIView):
    """port is Satellite's PK so if someone tries to save an already saved satellite nothing will happen.
    There's no need to safe check first. In a way, that makes the get/ method unnecessary. 
    I'll keep it nontheless. For it could be handy to know if a satellite is store in the db or not.
    """

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
            try:
                Satellite(name=name, port=port).save() 
            except Exception as e:
                return Response({'message': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({'message': 'Satellite saved.'})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskResults(APIView):
    """Used to get the results of the assigned tasks from the satellites.
    Because in this exercise the process time is almost non existent, we can 
    instead obtain this data from the response to the get method of the Tasks 
    view in satellites_app.satellites_api.views.TasksView
    """
    serializer_class = serializers.TaskResultsSerializer

    def post(self, request):

        serializers = self.serializer_class(data=request.data)
        
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            date_added = serializers.validated_data.get('date_added')
            assigned_to = serializers.validated_data.get('assigned_to')
            completed = serializers.validated_data.get('completed')
            try:
                Task(
                    name=name,
                    date_added=date_added,
                    assigned_to=assigned_to,
                    completed=completed
                ).save()
            except Exception as e:
                return Response({'message': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({'message': 'Task saved.'})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
