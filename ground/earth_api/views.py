from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Satellite, Task
from earth_api import serializers
from earth_api.distributor import start_distribution, get_online_satellites


class RegisterSatellite(APIView):
    """port is Satellite's PK so if someone tries to save an already saved satellite nothing will happen.
    There's no need to safe check first. In a way, that makes the get/ method unnecessary. 
    I'll keep it nontheless. For it could be handy to know if a satellite is store in the db or not.
    """

    serializer_class = serializers.RegisterSatelliteSerializer

    def get(self, request, format=None):
        port_number = request.query_params.get('port', None)
        host = request.query_params.get('host', None)

        if not port_number:
            return Response({'port': 'Missing parameter'}, status=status.HTTP_400_BAD_REQUEST)
        if not host:
            return Response({'host': 'Missing parameter'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Satellite.objects.get(host, port=port_number)
            message = 'Found'
        except Satellite.DoesNotExist:
            return Response({'error': 'Satellite does not exists'},
                            status=status.HTTP_404_NOT_FOUND)
        return Response({'message': message})

    def post(self, request):
        data = request.data.copy()
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class OnlineSatellites(APIView):
    def get(self, request, format=None):
        online_satellites = get_online_satellites()
        serializer = serializers.RegisterSatelliteSerializer(online_satellites, many=True)
        return Response(serializer.data)


class StartButton(APIView):

    serializer_class = serializers.StartButtonSerializer

    def get(self, request, format=None):
        return Response({'example': DEMO})

    def post(self, request):

        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            tasks = serializers.validated_data.get('tasks')
            result = start_distribution(tasks)
            return Response({'message': result})       
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 


DEMO = {
    "tasks": [{
        "name": "fotos",
        "pay_off": 10,
        "resources": [1, 5]
        },
        {
        "name": "mantenimiento",
        "pay_off": 1,
        "resources": [1, 2]
        },
        {
        "name": "pruebas",
        "pay_off": 1,
        "resources": [5, 6]
        },
        {
        "name": "fsck",
        "pay_off": 0.1,
        "resources": [1, 6]
        }]
}
