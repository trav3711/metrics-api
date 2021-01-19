from django.db import models
from django.contrib.postgres.indexes import BTreeIndex
from django.contrib.auth.models import User

class Timetypes(models.Model):
    types = models.CharField(max_length=10)

class Metrics(models.Model):
    metric_name = models.CharField(max_length = 25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_type = models.ForeignKey(Timetypes, on_delete=models.CASCADE)
    def __str__(self):
        return self.metric_name

class Entries(models.Model):
    metric = models.ForeignKey(Metrics, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entry_time = models.DateTimeField('Entry Time', auto_now=True)
    class Meta:
        indexes = [
            BTreeIndex(fields=['metric_id', 'user_id'])
        ]
