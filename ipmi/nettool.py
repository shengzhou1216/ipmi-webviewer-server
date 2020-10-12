import netifaces
import nmap3
import ipaddress

def cal_ip(ip_net):
    try:
        net = ipaddress.ip_network(ip_net, strict=False)
        print('IP版本号： ' + str(net.version))
        print('是否是私有地址： ' + str(net.is_private))
        print('IP地址总数: ' + str(net.num_addresses))
        print('可用IP地址总数： ' + str(len([x for x in net.hosts()])))
        print('网络号： ' + str(net.network_address))
        print('起始可用IP地址： ' + str([x for x in net.hosts()][0]))
        print('最后可用IP地址： ' + str([x for x in net.hosts()][-1]))
        print('可用IP地址范围： ' + str([x for x in net.hosts()]
                                 [0]) + ' ~ ' + str([x for x in net.hosts()][-1]))
        print('掩码地址： ' + str(net.netmask))
        print('反掩码地址： ' + str(net.hostmask))
        print('广播地址： ' + str(net.broadcast_address))
        return net.hosts()
    except ValueError:
        print('您输入格式有误，请检查！')
        return None


def get_gateways():
    return netifaces.gateways()['default'][netifaces.AF_INET][0]


def get_ip_lists(gateway):
    ip_lists = []
    for i in range(1, 256):
        ip_lists.append('{}{}'.format(gateway[:-1], i))
    return ip_lists


def scan_ip_survial(ip):
    nmScan = nmap3.NmapHostDiscovery()
    results = nmScan.nmap_portscan_only(ip)
    if results[ip] and len(results[ip]) > 0:
        return {'IP': ip,
                # 'Hostname:': nmScan[ip]['hostnames'][0]['name']
                }
    else:
        return None


def get_all_survial_hosts():
    survial_hosts = []
    gateway = get_gateways()
    ip_lists = get_ip_lists(gateway)
    for ip in ip_lists:
        scan_rst = scan_ip_survial(ip)
        if scan_rst:
            survial_hosts.append(scan_rst)
            print(scan_rst)
    return survial_hosts


if __name__ == '__main__':
    get_all_survial_hosts()
