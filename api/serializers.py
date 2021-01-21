from rest_framework import serializers
from api.models import Metric, Entry
from django.contrib.auth.models import User


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ['id', 'metric_name', 'user']


    #metric_id = serializers.IntegerField(read_only=True)
    #metric_name = serializers.CharField(required=True, allow_blank=False, max_length=25)
    #time_type = serializers.ChoiceField(choices = TIME_TYPES, default='Daily')

    #def create(self, validated_data):
    #    return Metric.objects.create(**validated_data)

    #def update(self, instance, validated_data):
    #    #instance.time_type = validated_data.get('time_type', instance.time_type)
    #    instance.save()
    #    return instance

class EntrySerializer(serializers.Serializer):
    class Meta:
        model = Entry
        fields = ['metric', 'user', 'quantity', 'entry_time']
