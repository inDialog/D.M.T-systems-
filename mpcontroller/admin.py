# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from mpcontroller.models import rasp_device, muse_device

class Muse(admin.ModelAdmin):
    pass
admin.site.register(muse_device, Muse)

class Raspberry(admin.ModelAdmin):
    pass
admin.site.register(rasp_device, Raspberry)