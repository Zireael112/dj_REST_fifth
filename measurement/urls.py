from django.urls import path
from .views import SensorinfAPIView, CreateSensorAPIView, RetrieveUpdateAPIView, ListCreateAPIView

urlpatterns = [
    path('sen/', SensorinfAPIView.as_view()),
    path('create/', CreateSensorAPIView.as_view()),
    path('sen/<pk>/', RetrieveUpdateAPIView.as_view()),
    path('meus/', ListCreateAPIView.as_view())
]
