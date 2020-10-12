from djongo import models

class Device(models.Model):
    ### 设备
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=20)