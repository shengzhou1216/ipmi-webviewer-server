import pyipmi
import pyipmi.interfaces
import logging
import json
import shlex
import subprocess

logger = logging.getLogger(__name__)


def check_device():
    pass

def check_ipmi_device(deviceIp, username, password, port=623):
    # 检查是否为IPMI设备
    try:
        interface = pyipmi.interfaces.create_interface(interface='ipmitool',
                                                   interface_type='lanplus')
        ipmi = pyipmi.create_connection(interface)
        ipmi.session.set_session_type_rmcp(deviceIp, port=port)
        ipmi.session.set_auth_type_user(username, password)
        ipmi.target = pyipmi.Target(ipmb_address=0x20)
        ipmi.session.establish()
        device_id = ipmi.get_device_id()
        # Below code used only to print out the device ID information
        # print('''
        # Device ID:          %(device_id)s
        # Device Revision:    %(revision)s
        # Firmware Revision:  %(fw_revision)s
        # IPMI Version:       %(ipmi_version)s
        # Manufacturer ID:    %(manufacturer_id)d (0x%(manufacturer_id)04x)
        # Product ID:         %(product_id)d (0x%(product_id)04x)
        # Device Available:   %(available)d
        # Provides SDRs:      %(provides_sdrs)d
        # Additional Device Support:
        # '''[1:-1] % device_id.__dict__)
        functions = (
            ('SENSOR', 'Sensor Device'),
            ('SDR_REPOSITORY', 'SDR Repository Device'),
            ('SEL', 'SEL Device'),
            ('FRU_INVENTORY', 'FRU Inventory Device'),
            ('IPMB_EVENT_RECEIVER', 'IPMB Event Receiver'),
            ('IPMB_EVENT_GENERATOR', 'IPMB Event Generator'),
            ('BRIDGE', 'Bridge'),
            ('CHASSIS', 'Chassis Device')
        )
        for n, s in functions:
            if device_id.supports_function(n):
                logger.info('  %s' % s)
        if device_id.aux is not None:
            logger.info('Aux Firmware Rev Info:  [%s]' % (
                ' '.join('0x%02x' % d for d in device_id.aux)))
    except RuntimeError as err:
        print(err)
        return False,None
    data = {
        'device_id': device_id.__dict__['device_id'],
        'revision': str(device_id.__dict__['revision']),
        'fw_revision': str(device_id.__dict__['fw_revision']),
        'ipmi_version': str(device_id.__dict__['ipmi_version']),
        'available': device_id.__dict__['available'],
    }
    # get cahasis status 
    chassis_status =  get_chassis_status(ipmi)
    # get system_info
    # system_info = get_system_info(ipmi)

    return True, data


def ipmi_command(self,device,command):
    ### 执行IPMI命令
    ### 返回一个CompletedProcess实例
    cmd = "ipmitool -I lanplus -U %s -P %s -H %s %s" % (device.username,device.password,device.ip,command)
    return subprocess.run(shlex.split(cmd))
    

# 获取温度
def get_system_info(ipmi):
    r = ipmi.session.get_system_info()
    print(r)
    return {}

def get_chassis_status(ipmi):
    chassis_status = ipmi.get_chassis_status()
    print('restore_policy:%s'% chassis_status.restore_policy)
    print('control_fault:%s' % chassis_status.control_fault)
    print('fault:%s' % chassis_status.fault)
    print('interlock:%s' % chassis_status.interlock)
    print('overload:%s' % chassis_status.overload)
    print('power_on:%s' % chassis_status.power_on)
    print('last_event:%s' % chassis_status.last_event)
    print('chassis_state:%s' % chassis_status.chassis_state)
    return {
        'restore_policy': chassis_status.restore_policy,
        'control_fault': chassis_status.control_fault,
        'fault': chassis_status.fault,
        'interlock': chassis_status.interlock,
        'overload': chassis_status.overload,
        'power_on': chassis_status.power_on,
        'last_event': chassis_status.last_event,
        'chassis_state': chassis_status.chassis_state
    }

if __name__ == '__main__':
    check_ipmi_device('10.1.35.19', 'admin', 'admin')
