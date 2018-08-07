# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class muse_device(models.Model):
    name = models.CharField(max_length=24, null=True, blank=True, unique=True)
    mac_address = models.CharField(max_length=18, null=True, blank=True)
    used = models.BooleanField(default=False)

class rasp_device(models.Model):
    name = models.CharField(max_length=24, null=True, blank=True)
    ip = models.CharField(max_length=24, null=True, blank=True)
    mac_address = models.CharField(max_length=24, primary_key=True, unique=True)
    connected_muse = models.OneToOneField(
        'muse_device',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
