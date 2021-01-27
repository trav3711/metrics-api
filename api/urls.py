from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views

entry_list = views.EntryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'metrics', views.MetricViewSet, 'get_queryset')
#router.register(r'entries', views.EntryViewSet, 'get_queryset')
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('metrics/<int:pk>/entries/', entry_list, name='entry-list'),
    path('', include(router.urls)),
]
