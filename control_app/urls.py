from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LightSettingsViewSet, index

router = DefaultRouter()
router.register(r'light-settings', LightSettingsViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
