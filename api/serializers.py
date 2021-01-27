from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from api.models import Metric, Entry
from django.contrib.auth.models import User


class EntrySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'metric', 'owner', 'quantity', 'entry_time']

class MetricSerializer(FlexFieldsModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    entries = serializers.PrimaryKeyRelatedField(many=True, queryset=Entry.objects.all())
    class Meta:
        model = Metric
        fields = ['id', 'metric_name', 'owner', 'entries']
        expandable_fields = {
            'entries': (EntrySerializer, {'many': True})
        }

class UserSerializer(serializers.ModelSerializer):
    metrics = serializers.PrimaryKeyRelatedField(many=True, queryset=Metric.objects.all())
    #days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        expandable_fields = {
            'metrics': (MetricSerializer, {'many': True})
        }

    #def get_days_since_joined(self, obj):
    #    return (now() - obj.date_joined).days
