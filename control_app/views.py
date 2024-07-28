
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import LightSettings
from .serializers import LightSettingsSerializer

class LightSettingsViewSet(viewsets.ModelViewSet):
    queryset = LightSettings.objects.all()
    serializer_class = LightSettingsSerializer

def index(request):
    return render(request, 'control_app/index.html')
