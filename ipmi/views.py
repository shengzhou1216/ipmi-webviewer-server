from django.http import HttpResponse
import json
from .models import Device
def index(request):
    r = {'code':404,'message':'xxxxx'}
    return HttpResponse(json.dumps(r))

def get_all_devices(request):
    ### 获取所有的设备
    devices = list(Device.objects.all())
    print(devices)
    return devices

def scan_devices(request):
    ### 扫描设备
    pass

def connect_device(request):
    # 链接指定设备
    pass

def get_device_temperature(request):
    ### 获取设备的问题
    pass

def shutdown_devices_patch(request):
    ### 批量关闭设备
    pass

def shutdown_devices_all(request):
    ### 关闭所有设备
    pass

def startup_devices_patch(request):
    ### 启动所有设备
    pass

def startup_devices_all(request):
    ### 批量启动设备
    pass


