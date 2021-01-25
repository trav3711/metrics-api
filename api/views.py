from api.models import Metric, Entry
from django.contrib.auth.models import User
from api.serializers import MetricSerializer, EntrySerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, status
from rest_framework import viewsets
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response

class MetricViewSet(viewsets.ModelViewSet):
    #queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly]

    def get_queryset(self):
        return Metric.objects.filter(owner=self.request.user.id)

    def perform_create(self, serializer):
        """
        binds a Metric to a user when created
        """
        serializer.save(owner=self.request.user)

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly]

    def get_queryset(self):
        return Entry.objects.filter(owner = self.request.user.id,
                                    metric = self.kwargs['pk'])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        metric = serializer.validated_data['metric']
        self.perform_create(serializer, metric)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, metric):
        serializer.save(metric=metric,
                        owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
