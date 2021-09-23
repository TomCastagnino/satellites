from rest_framework import serializers


class RegisterSatelliteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    port = serializers.IntegerField()


class TaskResultsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    date_added = serializers.DateTimeField()
    assigned_to = serializers.CharField(max_length=100)
    completed = serializers.BooleanField()