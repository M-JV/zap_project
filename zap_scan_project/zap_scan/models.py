#zap_project/zap_scan/models.py
from django.db import models

# Create your models here.

class Alert(models.Model):
    sourceid = models.CharField(max_length=10)
    other = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    evidence = models.TextField()
    pluginId = models.CharField(max_length=10)
    cweid = models.CharField(max_length=10)
    confidence = models.CharField(max_length=10)
    wascid = models.CharField(max_length=10)
    description = models.TextField()
    messageId = models.CharField(max_length=10)
    inputVector = models.TextField()
    url = models.URLField()
    reference = models.URLField()
    solution = models.TextField()
    alert = models.CharField(max_length=255)
    param = models.CharField(max_length=255)
    attack = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    risk = models.CharField(max_length=10)
    alertRef = models.CharField(max_length=20)

    def __str__(self):
        return self.name
