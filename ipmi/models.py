from djongo import models
from datetime import datetime
from django.utils import timezone
class Device(models.Model):
    ip = models.CharField(max_length=20)    
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    #所属网段
    network = models.CharField(max_length=20)
    mac = models.CharField(max_length=50)
    is_up = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    # 温度
    temperatures = models.TextField()
    class Meta:
        app_label = 'ipmi'
