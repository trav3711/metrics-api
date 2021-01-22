from api.models import Metric, Entry
from django.contrib.auth.models import User
from api.serializers import MetricSerializer, EntrySerializer

from rest_framework import generics

class MetricsList(generics.ListCreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

class MetricDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

class EntriesList(generics.ListCreateAPIView):
    pass
