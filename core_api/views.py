from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from mpcontroller.models import rasp_device, muse_device
from core_api.serializers import RaspSerializer

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@api_view(['POST'])
def connectPi(request):
    if request.method == 'POST':
        serializer = RaspSerializer(data=request.data)
        if serializer.is_valid():
            mac_address = serializer.validated_data['mac']
            ip_address = get_client_ip(request)
            connection_status = serializer.validated_data['status']
            raspb = rasp_device.objects.get(mac_address=mac_address)
            raspb.ip = ip_address
            if raspb.connected_muse != None:
                    free_muse = raspb.connected_muse
                    free_muse.used = False
                    free_muse.save()
            if connection_status == 'disconnected':
                raspb.connected_muse = None
            else:
                raspb.connected_muse = muse_device.objects.get(mac_address=connection_status)
                raspb.connected_muse.used = True
                raspb.connected_muse.save()
            raspb.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)