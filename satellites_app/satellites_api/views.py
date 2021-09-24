from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from satellites_api import serializers
from satellites_api import models
from satellites_api import utils
from satellites_api.setup import NAME
from datetime import datetime


class Health(APIView):
    def get(self, request, format=None):
        return Response({'message': 'Hello, world!'})


class TasksView(APIView):
    serializer_class = serializers.TasksSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            tasks = serializers.validated_data.get('tasks')
            results = []
            for task in tasks:
                _, completed = utils.solve_task(task, error_margin=10)
                now = datetime.now()
                models.Task(name=task, date_added=now, assigned_to=NAME, completed=completed).save()
                results.append({
                    'name': task, 
                    'date_added': now,
                    'assigned_to': NAME,
                    'completed': completed
                    })
            return Response({'results': results})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


