from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('metrics/<int:user_fk>/', views.metrics_list),
    path('metrics/detail/<int:pk>/', views.metric_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
