from django.contrib import admin

from measurement.models import Sensor, SensorDetail


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass


@admin.register(SensorDetail)
class SensorDetail(admin.ModelAdmin):
    pass
