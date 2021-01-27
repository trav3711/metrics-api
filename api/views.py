from django.contrib.auth.models import User
from api.models import Metric, Entry
from api.serializers import MetricSerializer, EntrySerializer, UserSerializer
#from api.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_flex_fields import is_expanded
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyTokenObtainPairSerializer

class MetricViewSet(viewsets.ModelViewSet):
    #queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset =  Metric.objects.filter(owner=self.request.user.id)

        if is_expanded(self.request, 'entries'):
            queryset = queryset.prefetch_related('entries')

        return queryset

    def perform_create(self, serializer):
        """
        binds a Metric to a user when created
        """
        serializer.save(owner=self.request.user)

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

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
        """
        Binds an Entry to a Metricd when created
        """
        serializer.save(metric=metric,
                        owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
