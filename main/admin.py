from django.contrib import admin
from main.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'stream_url')