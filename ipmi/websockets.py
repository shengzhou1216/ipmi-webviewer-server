from channels.generic.websocket import WebsocketConsumer
import json
from . import nettool
from . import ipmitool
from .models import Device


class DevicesConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.scan_flag = None

    def disconnect(self, close_code):
        print('client disconnect %s' % close_code)

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        if text_data_json['type'] == 'scan':
            self.scan_devices()
        elif text_data_json['type'] == 'stop_scan':
            self.stop_scan_devices()
        elif text_data_json['type'] == 'add_device':
            self.add_device(text_data_json['data'])

    def scan_devices(self):
        # 扫描设备
        self.scan_flag = True
        gateway = nettool.get_gateways()
        ip_lists = nettool.get_ip_lists(gateway)
        for ip in ip_lists:
            if not self.scan_flag:
                break
            scan_rst = nettool.scan_ip_survial(ip)
            if scan_rst:
                self.send(text_data=json.dumps({
                    'type': 'scan',
                    'message': 'success',
                    'code': 200,
                    'data': scan_rst
                }))
        self.send(text_data=json.dumps({
            'type': 'scan',
                    'message': 'finished',
                    'code': 201
        }))

    def stop_scan_devices(self):
        # 停止扫描设备
        self.scan_flag = False

    def add_device(self, data):
        # 添加设备
        r, result = ipmitool.check_ipmi_device(
            data['ip'], data['username'], data['password'])
        if r:
            result['ip'] = data['ip']
            self.send(text_data=json.dumps({
                'type': 'add_device',
                'message': 'success',
                'code': 200,
                'data': result
            }))
            device = Device.objects.get(ip=data['ip'])
            if device:
                device.network = data['network']
                device.username = data['username']
                device.password = data['password']
                device.chassis_status = result
            else:
                device = Device(ip=data['ip'], username=data['username'],
                                password=data['password'], support_ipmi=True, network=data['network'])
            device.save()
        else:
            self.send(text_data=json.dumps({
                'type': 'add_device',
                'message': 'failed',
                'code': 500
            }))
