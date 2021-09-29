from rest_framework import serializers
from .models import Satellite


class RegisterSatelliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satellite
        fields = '__all__'

    def create(self, validated_data):
        satellite = Satellite(**validated_data)
        satellite.save()
        return satellite


class TaskResultsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    date_added = serializers.DateTimeField()
    assigned_to = serializers.CharField(max_length=100)
    completed = serializers.BooleanField()


class StartButtonSerializer(serializers.Serializer):
    tasks = serializers.JSONField()  
    