from api.models import Metric, Entry
from django.contrib.auth.models import User
from api.serializers import MetricSerializer, EntrySerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions

class MetricsList(generics.ListCreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MetricDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EntriesList(generics.ListCreateAPIView):
    pass

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
