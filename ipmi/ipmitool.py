import pyipmi
import pyipmi.interfaces
import logging
import json
import shlex
import re
from subprocess import Popen,PIPE

logger = logging.getLogger(__name__)
    
# 扫描设备
def scan_devices(network):
    print('==========scan_devices:%s========' % network)
    cmd = 'sudo nmap -sU --script ipmi-version -p 623 %s' % network
    proc = Popen(shlex.split(cmd),stdout=PIPE,stderr=PIPE)
    hosts = []
    temp_host = ''''''
    while True:
        line = proc.stdout.readline()
        line = str(line.rstrip(),encoding='utf-8')
        if line == '' or is_nmap_started(line):
            continue
        if is_host_started(line):
            temp_host = line
        elif is_host_ended(line):
            temp_host += '''\n''' + line
            hosts.append(temp_host)
        elif is_nmap_ended(line):
            hosts.append(temp_host)
            break
        else:
            temp_host += '''\n''' + line
    r = []
    for host in hosts:
        if not is_ipmi_device(host):
            continue
        ip = get_host_ip(host)
        mac = get_host_mac(host)
        r.append({
            'ip': ip,
            'mac': mac,
        })
    print('scan_devices finished:%s' % r)
    return r    
def is_host_started(s):
    return 'Nmap scan report for' in s

def get_host_ip(s):
    r = re.findall(r'\d+\.\d+\.\d+\.\d+', s)
    if r and len(r) > 0:
        return r[0]
    return None    

def is_host_ended(s):
    return 'MAC Address' in s

def is_nmap_started(s):
    return 'Starting Nmap' in s

def is_nmap_ended(s):
    return 'Nmap done' in s

def is_host_up(s):
    return 'Host is up' in s    

def is_ipmi_device(s):
    return 'ipmi-version' in s

def get_host_mac(s):
    r = re.findall(r'(?:[0-9a-fA-F]:?){12}', s)
    if r and len(r) > 0:
        return r[0]
    return None    

# 获取电源状态
def power_status(ip,username,password):
    print('==========power_status: %s,%s,%s=======' % (ip,username, password))
    cmd = 'ipmitool -I lanplus -H %s -U %s -P %s  power status' % (ip,username,password)
    outs,errs = Popen(shlex.split(cmd), stdout=PIPE,stderr=PIPE).communicate()
    if errs:
        return False,str(errs,encoding='utf-8')
    is_up = 'on' in str(outs,encoding='utf-8').lower()
    return True,is_up    

# 开机/关机
def powerctl(ip,username,password,status):
    print('==========powerctl: %s,%s,%s,%s========' % (ip,username,password,status))
    cmd = 'ipmitool -I lanplus -H %s -U %s -P %s power %s' % (
        ip, username, password,status)
    outs, errs = Popen(shlex.split(cmd), stdout=PIPE,stderr=PIPE).communicate()
    if errs:
        return False, str(errs,encoding='utf-8')
    return True, str(outs,encoding='utf-8')

    
# 获取温度
def temperature(ip,username,password):
    print('==========temperature: %s,%s,%s========' % (ip, username, password))
    cmd = 'ipmitool -I lanplus -H %s -U %s -P %s sdr type Temperature' % (ip, username, password)
    proc = Popen(shlex.split(cmd), stdout=PIPE,stderr=PIPE)
    results = []
    names = []
    while True:
        line = proc.stdout.readline()
        line = str(line.rstrip(), encoding='utf-8')
        if not line:
            break
        sensor_name = line.split("|")[0].strip()
        sensor_status = line.split("|")[2].strip()
        temperature = line.split("|")[-1].strip()
        # 过滤重复的传感器名称
        if sensor_name in names:
            continue
        names.append(sensor_name)
        results.append({
            'sensor_name': sensor_name,
            'sensor_status': sensor_status,
            'temperature': temperature
        })
    return results


if __name__ == '__main__':
    temperature('10.1.35.36', 'aicity', 'aicity12345678')
