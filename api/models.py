from django.db import models
from django.contrib.postgres.indexes import BTreeIndex
from django.contrib.auth.models import User

TIME_TYPES = [
    ('daily', 'daily'),
    ('weekly', 'weekly'),
    ('bi-weekly', 'bi-weekly'),
    ('monthly', 'monthly'),
    ('annually', 'annually')
]

class Metric(models.Model):
    metric_name = models.CharField(max_length = 25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #time_type = models.CharField(choices=TIME_TYPES, default=TIME_TYPES[0], max_length=10)
    def __str__(self):
        return self.metric_name

class Entry(models.Model):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entry_time = models.DateTimeField('Entry Time', auto_now=True)
    class Meta:
        indexes = [
            BTreeIndex(fields=['metric_id', 'user_id'])
        ]
