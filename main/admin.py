from django.contrib import admin
from main.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'stream_url', 'protocol', 'mac', 'ip', 'status')
    readonly_fields = ('status',)
    search_fields = ['name', 'ip']
    list_filter = ('protocol', 'status')
    ordering = ['name']