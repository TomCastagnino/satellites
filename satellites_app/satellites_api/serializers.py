from rest_framework import serializers


class TasksSerializer(serializers.Serializer):
    tasks = serializers.ListField(child=serializers.CharField())
    resources = serializers.ListField(child=serializers.IntegerField())