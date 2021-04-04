from django.db import models
from django.contrib.postgres.indexes import BTreeIndex

class Metric(models.Model):
    metric_name = models.CharField(max_length = 25)
    metric_description = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='metrics', default="", on_delete=models.CASCADE)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    def __str__(self):
        return self.metric_name

class Entry(models.Model):
    metric = models.ForeignKey(Metric, related_name='entries', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='entries', default="", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entry_time = models.DateTimeField('Entry Time', auto_now=True)
    class Meta:
        indexes = [
            BTreeIndex(fields=['metric_id'])
        ]
