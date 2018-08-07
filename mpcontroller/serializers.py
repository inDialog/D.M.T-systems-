from rest_framework import serializers

from mpcontroller.models import muse_device, rasp_device

class RaspSerializer(serializers.Serializer):
    ip = serializers.CharField(required=False, allow_blank=True, max_length=24)
    mac_address = serializers.CharField(required=False, allow_blank=True, max_length=24)
    connected_muse = serializers.CharField(required=False, allow_blank=True, max_length=24)
    name = serializers.CharField(required=False, allow_blank=True, max_length=24)

    def create(self, validated_data):
        """
        Create and return a new `Raspberry` instance, given the validated data.
        """
        return rasp_device.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Raspberry` instance, given the validated data.
        """
        instance.ip = validated_data.get('ip', instance.ip)
        instance.mac_address = validated_data.get('mac_address', instance.code)
        instance.connected_muse = validated_data.get('connected_muse', instance.connected_muse)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance