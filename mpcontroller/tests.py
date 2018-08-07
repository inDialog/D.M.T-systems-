# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from mpcontroller.models import muse_device, rasp_device

def create_muse(mac, name):
    new_muse = muse_device.objects.create(name = name, mac_address=mac)
    new_muse.save()
    print ("Muse %s created successfully" %(name))
    return None

def create_pi(mac, name, ip, muse_mac):
    muse = muse_device.objects.get(mac_address= muse_mac)
    new_pi = rasp_device.objects.create(name = name, mac_address=mac, ip=ip, connected_muse = muse)
    new_pi.save()

muse_data[['','Tale of Us'],['','Recondite'],['','Hardwell'],['','Len Faki'],['','Plastikman'],['','Nina'],['','Villalobos']]
pi_data[['','Pink Floyd',''],['','The Beatles',''],['','Hendrix',''],['','Jethro Tull',''],['','Cobain',''],['','Nirvana',''],['','Police','']]

for current_muse in muse_data:
        create_muse(current_muse[0], current_muse[1])
count=0
for current_pi in pi_data:
    create_pi(current_pi[0],current_pi[1],current_pi[2], muse_data[count][0])
    count += 1