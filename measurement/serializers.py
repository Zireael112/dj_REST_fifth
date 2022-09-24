from rest_framework import serializers
from measurement.models import SensorDetail, Sensor
# TODO: опишите необходимые сериализаторы


class SensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class MeasurementsSerializers(serializers.ModelSerializer):
    model = SensorDetail
    fields = ['id', 'temperature', 'created_at']


class SensorDetailSerializers(serializers.ModelSerializer):
    measurements = MeasurementsSerializers(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
