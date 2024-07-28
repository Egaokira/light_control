from django.db import models


class LightSettings(models.Model):
    color = models.CharField(max_length=7)  
    intensity = models.IntegerField()
    pattern = models.CharField(max_length=20)

    def __str__(self):
        return f"Light Settings: {self.color}, {self.intensity}%, {self.pattern}"
