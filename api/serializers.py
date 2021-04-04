from rest_framework import serializers

from api.models import Metric, Entry
from django.contrib.auth.models import User


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'metric', 'owner', 'quantity', 'entry_time']

class MetricCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Metric
        fields = ['id', 'metric_name', 'owner', 'created_at']

class MetricSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    entries = serializers.PrimaryKeyRelatedField(many=True, queryset=Entry.objects.all())
    class Meta:
        model = Metric
        fields = ['id', 'metric_name', 'owner', 'created_at', 'entries']

class UserSerializer(serializers.ModelSerializer):
    metrics = serializers.PrimaryKeyRelatedField(many=True, queryset=Metric.objects.all())
    #days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
