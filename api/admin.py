from django.contrib import admin
from api.models import Metric, Entry
from django.contrib.auth.models import Group

admin.site.site_header = 'Metrics API Admin'

admin.site.register(Metric)
admin.site.register(Entry)

admin.site.unregister(Group)


# Register your models here.
