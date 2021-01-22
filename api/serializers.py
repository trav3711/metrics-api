from rest_framework import serializers
from api.models import Metric, Entry
from django.contrib.auth.models import User


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ['id', 'metric_name', 'user']

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['metric', 'user', 'quantity', 'entry_time']

class UserSerializer(serializers.ModelSerializer):
    metrics = serializers.PrimaryKeyRelatedField(many=True, queryset=Metric.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'metrics']
