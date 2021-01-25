from rest_framework import serializers
from api.models import Metric, Entry
from django.contrib.auth.models import User


class MetricSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Metric
        fields = ['id', 'metric_name', 'owner']

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'metric', 'owner', 'quantity', 'entry_time']

class UserSerializer(serializers.ModelSerializer):
    metrics = serializers.PrimaryKeyRelatedField(many=True, queryset=Metric.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'metrics']
