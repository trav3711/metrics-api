from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from api.models import Metric, Entry
from django.contrib.auth.models import User
from api.serializers import MetricSerializer, EntrySerializer

@api_view(['GET', 'POST'])
def metrics_list(request, user_fk, format=None):
    """
    List all of the metrics for a given user, or create a new metric
    """
    if request.method == 'GET':
        metrics = Metric.objects.filter(user_id=user_fk)
        serializer = MetricSerializer(metrics, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MetricSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def metric_detail(request, pk, format=None):
    try:
        metric = Metric.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MetricSerializer(metric)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MetricSerializer(metric, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        metric.delete()
        return HttpResponse(status=204)

def entries_list(request, metric_fk):
    """
    List all of the entries for a given metric
    """
    if request.method == 'GET':
        entries = Entry.objects.filter(metric=metric)
        serializer = EntrySerializer(entries, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        pass



# Create your views here.
