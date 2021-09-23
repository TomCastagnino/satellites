from rest_framework import serializers


class RegisterSatelliteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    port = serializers.IntegerField()