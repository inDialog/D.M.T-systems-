# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseRedirect

from mpcontroller.models import muse_device, rasp_device
import liblo

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
            c = liblo.Message('/change_mac', 'disconnected')
            outputAddress = liblo.Address(raspb.ip, 6001)
            liblo.send(outputAddress, c)
        else:
            muse = muse_device.objects.get(mac_address=mac_muse)
            raspb.connected_muse = muse
            muse.used = True
            muse.save()
            c = liblo.Message('/change_mac', raspb.connected_muse.mac_address)
            outputAddress = liblo.Address(raspb.ip, 6001)
            liblo.send(outputAddress, c)
        raspb.save()
    return HttpResponseRedirect('/')

def addDevice(request):
    if request.method == 'POST':
        if request.POST['device-type'] == 'muse':
            new_muse = muse_device.objects.create(name = request.POST['device-name'], mac_address=request.POST['mac-address'])
            new_muse.save()
        else:
            new_pi = rasp_device.objects.create(name = request.POST['device-name'], mac_address=request.POST['mac-address'])
            new_pi.save()
