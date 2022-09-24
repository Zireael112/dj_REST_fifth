# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, SensorDetail
from .serializers import SensorSerializers, SensorDetailSerializers, MeasurementsSerializers


class CreateSensorAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

    def post(self, request):
        review = SensorDetailSerializers(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class SensorinfAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers


class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializers

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializers(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class ListCreateAPIView(ListAPIView):
    queryset = SensorDetail.objects.all()
    serializer_class = MeasurementsSerializers

    def post(self, request):
        review = MeasurementsSerializers(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})
