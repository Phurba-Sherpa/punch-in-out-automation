
### Lib import
import re
import subprocess

OFFINE_MSG = 'Destination host unreachable.'
ONLINE_ECHO_FAILED_MSG = 'Request timed out.'
ONLINE_ECHO_SUCCESS_MSG = '0% loss'

### will fetch the physical address from arp table
arp_req_command = 'arp -a'
mac_addr_pattern = '([-0-9a-f]{17})'

def get_mac_addr_list():
    result = subprocess.run(arp_req_command, stdout=subprocess.PIPE)
    arp_table = result.stdout.decode('utf8')
    mac_addr_list = []
    for addr in re.findall(mac_addr_pattern, arp_table):
        mac_addr_list.append(addr)
    return mac_addr_list

def ping_device(ip_addr_list):
    online_ip_addr_list = []
    offline_ip_addr_list = []
    
    for ip_addr in ip_addr_list:
        ping_command = 'ping -n 1 '+ ip_addr    
        result = subprocess.run(ping_command, stdout=subprocess.PIPE)
        output = result.stdout.decode('utf8')
        
        print(output)
        if OFFINE_MSG in output:
            offline_ip_addr_list.append(ip_addr)
        elif  ONLINE_ECHO_FAILED_MSG in output or ONLINE_ECHO_SUCCESS_MSG in output:
            online_ip_addr_list.append(ip_addr)
    print('online ip addr', online_ip_addr_list)
    print('offline ip addr', offline_ip_addr_list)

ip_addr_list = ['192.168.1.93', '192.168.1.91', '192.168.1.73']
ping_device(ip_addr_list)
