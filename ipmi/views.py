from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Device
from . import ipmitool
from datetime import datetime

def get_all_devices(request):
    ### 获取所有的设备
    devices = serializers.serialize('json', Device.objects.all())
    lists = json.loads(devices)
    for d in lists:
        fields = d['fields']
        if fields['username'] and fields['password']:
            update_power_status(
                fields['ip'], fields['username'], fields['password'])
    devices = serializers.serialize('json', Device.objects.all())
    return HttpResponse(devices,content_type='application/json')

@csrf_exempt
def scan_devices(request):
    json_data = json.loads(request.body)
    network = json_data['network']
    # 扫描
    scan(network)   
    devices = serializers.serialize('json',Device.objects.all())
    return HttpResponse(devices,content_type='application/json')

@csrf_exempt
def update_credentials(request):
    json_data = json.loads(request.body)
    ip = json_data['ip']
    username = json_data['username']
    password = json_data['password']
    update_userinfo(ip,username, password)
    return HttpResponse(json.dumps({'message': 'success'}))

def update_userinfo(ip,username,password):
    Device.objects.filter(ip=ip).update(username=username, password=password)

def get_device_by_ip(ip):
    return json.loads(serializers.serialize('json', [Device.objects.filter(ip=ip).first()]))[0]['fields']

@csrf_exempt
def powerctl(request):
    json_data = json.loads(request.body)
    ip = json_data['ip']
    status = json_data['status']
    
    device = get_device_by_ip(ip)

    username = device['username']
    password = device['password']

    r, msg = ipmitool.powerctl(ip, username, password, status)
    if r:
        return HttpResponse(json.dumps({'message': 'success'}))
    else:
        return HttpResponse(json.dumps({'message':msg}),status=500)

@csrf_exempt
def powerctl_patch(request):
    ### 批量开机、关机
    json_data = json.loads(request.body)
    ips = json_data['ips']
    hasUsernamePassword = False
    if 'username' in json_data:
        hasUsernamePassword = True
        username = json_data['username']
    if 'password' in json_data:
        password = json_data['password']    
    status = json_data['status']
    batch_results = []
    # 批量操作
    if hasUsernamePassword:
        # 使用指定的用户名密码
        for ip in ips:
            r,err = ipmitool.powerctl(ip, username, password, status)
            batch_results.append({'result': r, 'message': err,'ip':ip})
            # 更新机器的用户名密码
            update_userinfo(ip,username, password)
    else:
        # 使用各机器已设置的用户名密码
        devices = json.loads(serializers.serialize(
            'json', Device.objects.filter(ip__in=ips)))
        for d in devices:
            fields = d['fields']
            r,err = ipmitool.powerctl(fields['ip'], fields['username'], fields['password'], status)
            batch_results.append({'result': r, 'message':err,'ip':fields['ip']})

    return HttpResponse(json.dumps({'results': batch_results}))

# 获取电源状态
@csrf_exempt
def power_status(request):
    json_data = json.loads(request.body)
    ip = json_data['ip']
    device = get_device_by_ip(ip)
    username = device['username']
    password = device['password']
    r ,is_up= update_power_status(ip, username, password)
    if r:
        return HttpResponse(json.dumps({'is_up': is_up}))
    return HttpResponse(json.dumps({'message': is_up}), status=500)

# 更新电源状态
def update_power_status(ip,username,password):
    r, is_up = ipmitool.power_status(ip, username, password)
    if r:
        update_userinfo(ip,username, password)
        Device.objects.filter(ip=ip).update(is_up=is_up)
    return r,is_up
# 扫描设备
def scan(network):
    # 扫描
    devices = ipmitool.scan_devices(network)
    # 删除原有的数据
    Device.objects.all().delete()
    # 保存新的数据
    for device in devices:
        d = Device(ip=device['ip'], network=network,
                   mac=device['mac'])
        d.save()


def get_device_temperature(request,ip):
    # Device.objects.filter(ip=ip).update(temperatures=json.dumps([]))
    ### 获取设备的温度
    device = get_device_by_ip(ip)
    username = device['username']
    password = device['password']
    temperatures = device['temperatures']
    temperatures = json.loads(temperatures)
    results = ipmitool.temperature(ip,username, password)
    data = []
    if temperatures and len(temperatures) > 0:
        # 已有温度数据，
        for r in results:
            print(r)
            for t in temperatures:
                if r['sensor_name'] == t['name']:
                    t['temperatures'].append({
                        'temperature': r['temperature'],
                        'created_at': str(datetime.now()),
                    })
        data = temperatures            
    else:
        # 没有温度数据
        for r in results:
            sensor = {
                'name': r['sensor_name'],
                'status': r['sensor_status'],
                'temperatures': [
                    {
                        'temperature': r['temperature'], 
                        'created_at': str(datetime.now()),
                    }
                ]
            }
            data.append(sensor)
    # 更新温度数据
    Device.objects.filter(ip=ip).update(temperatures=json.dumps(data))
    return HttpResponse(json.dumps({'results':data}))
