from rest_framework import serializers
from .models import LightSettings

class LightSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightSettings
        fields = ['color', 'intensity', 'pattern']
