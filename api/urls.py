from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('metrics/', views.MetricList.as_view()),
    path('metrics/<int:pk>/', views.MetricDetail.as_view()),
    path('metrics/<int:fk>/<int:pk>/', views.EntryDetail.as_view()),
    path('', include(router.urls)),
]
