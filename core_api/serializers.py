from rest_framework import serializers

from mpcontroller.models import muse_device, rasp_device

class RaspSerializer(serializers.Serializer):
    mac = serializers.CharField(required=False, allow_blank=True, max_length=24)
    ip = serializers.CharField(required=False, allow_blank=True, max_length=24)
    status = serializers.CharField(required=False, allow_blank=True, max_length=24)

    def create(self, validated_data):
        """
        Create and return a new `Raspberry` instance, given the validated data.
        """
        return rasp_device.objects.create(**validated_data)
