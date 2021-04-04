from django.contrib.auth.models import User
from api.models import Metric, Entry
from api.serializers import *
#from api.permissions import IsOwnerOrReadOnly

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_flex_fields import is_expanded
#from rest_framework_simplejwt.views import TokenObtainPairView

class MetricList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        metrics = Metric.objects.filter(owner=request.user)
        serializer = MetricSerializer(metrics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MetricCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MetricDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Metric.objects.get(pk=pk)
        except Metric.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        metric = self.get_object(pk)
        serializer = MetricSerializer(metric)
        return Response(serializer.data)

    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        if serialzier.is_valid():
            serlizer.save(metric=request.metric)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        metric = self.get_object(pk)
        serializer = MetricCreateSerializer(metric, data=request.data)
        if serializer.is_valid():
            serliazer.save(owner=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        metric = self.get_object(pk)
        metric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EntryDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, fk):
        try:
            return Entry.objects.get(fk=fk, pk=pk)
        except Entry.DoesNotExist:
            raise Http404

    def get(self, request, pk, fk):
        entry = self.get_object(pk, fk)
        serliazer = EntrySerializer(entry)
        return Response(serializer.data)

    def put(self, request, pk, fk):
        entry = self.get_object(pk, fk)
        serliazer = EntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serliazer.save(metric=request.metric)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, fk):
        entry = self.get_object(pk, fk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
