# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseRedirect

from mpcontroller.models import muse_device, rasp_device

from rest_framework.decorators import api_view
from rest_framework.response import Response

from mpcontroller.serializers import RaspSerializer

def index(request):
    muse_devices = muse_device.objects.all()
    rasp_devices = rasp_device.objects.all()
    return render(request, 'mpcontroller/index.html', {'muse_devices':muse_devices, 'rasp_devices':rasp_devices})


def updateMac(request):
    if request.method == 'POST':       
        mac_muse = request.POST['muse-mac']
        raspb_mac = request.POST['raspberry-mac']
        raspb = rasp_device.objects.get(mac_address=raspb_mac)
        if mac_muse == '':
            free_muse = raspb.connected_muse
            free_muse.used = False
            free_muse.save()
            raspb.connected_muse = None
        else:
            muse = muse_device.objects.get(MAC_address=mac_muse)
            raspb.connected_muse = muse
            muse.used = True
            muse.save()
        raspb.save()
        
    return HttpResponseRedirect('/')

@api_view(['POST'])
def connectPi(request):
    if request.method == 'GET':
        serializer = RaspSerializer(data=request.data)
        if serializer.is_valid():
            print (request.body)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
