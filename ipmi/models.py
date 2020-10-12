from djongo import models

class Device(models.Model):
    ip = models.CharField(max_length=20)    
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    chassis_status = models.JSONField
    #所属网段
    network = models.CharField(max_length=20)
    #是否支持IPMI
    support_ipmi = models.BooleanField(default=False)
    class Meta:
        app_label = 'ipmi'