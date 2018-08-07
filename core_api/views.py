from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from mpcontroller.models import rasp_device, muse_device
from core_api.serializers import RaspSerializer

@api_view(['POST'])
def connectPi(request):
    if request.method == 'POST':
        serializer = RaspSerializer(data=request.data)
        if serializer.is_valid():
            mac_address = serializer.validated_data['mac']
            ip_address = serializer.validated_data['ip']
            connection_status = serializer.validated_data['status']
            raspb = rasp_device.objects.get(mac_address=mac_address)
            raspb.ip = ip_address
            if connection_status == 'disconnected':
                if raspb.connected_muse != None:
                    free_muse = raspb.connected_muse
                    free_muse.used = False
                    free_muse.save()
                raspb.connected_muse = None
            else:
                raspb.connected_muse = muse_device.objects.get(mac_address=connection_status)
                raspb.connected_muse.used = True
                raspb.connected_muse.save()
            raspb.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)