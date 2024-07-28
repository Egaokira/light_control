from django.db import models

# Create your models here.

class LightSettings(models.Model):
    color = models.CharField(max_length=7)  # hex color
    intensity = models.IntegerField()
    pattern = models.CharField(max_length=20)

    def __str__(self):
        return f"Light Settings: {self.color}, {self.intensity}%, {self.pattern}"
