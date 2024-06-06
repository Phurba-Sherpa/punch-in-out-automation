
### Lib import
import re
import subprocess
from datetime import datetime, time

OFFINE_MSG = 'Destination host unreachable.'
ONLINE_ECHO_FAILED_MSG = 'Request timed out.'
ONLINE_ECHO_SUCCESS_MSG = '0% loss'

PUNCH_IN_TIME = time(11, 0, 0)
PUNC_OUT_TIME = time(7, 0, 0)

PUNCH_STATUS = {
    'PUNCH_IN': 'PI',
    'PUNCH_OUT': 'PO'
}

### will fetch the physical address from arp table
mac_addr_pattern = '([-0-9a-f]{17})'

def get_mac_addr_list(ip_addr_list):
    ip_mac_table = {}
    for ip_addr in ip_addr_list:
        arp_req_command = 'arp -a ' + ip_addr
        result = subprocess.run(arp_req_command, stdout=subprocess.PIPE)
        arp_info = result.stdout.decode('utf8')
        
        # Extract mac
        matched_mac_addr_list = re.findall(mac_addr_pattern, arp_info)
        
        # if matched then will have matched list, if not then []
        if len(matched_mac_addr_list) != 0:
            ip_mac_table[ip_addr] = matched_mac_addr_list[0]
    return ip_mac_table

def ping_device(ip_addr):
    ping_command = 'ping -n 1 '+ ip_addr    
    result = subprocess.run(ping_command, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf8')
    return output
    
def get_online_offline_devices(ip_addr_list):
    online_ip_addr_list = []
    offline_ip_addr_list = []
    
    for ip_addr in ip_addr_list:
        output = ping_device(ip_addr)
        if OFFINE_MSG in output:
            offline_ip_addr_list.append(ip_addr)
        elif  ONLINE_ECHO_FAILED_MSG in output or ONLINE_ECHO_SUCCESS_MSG in output:
            online_ip_addr_list.append(ip_addr)

    return online_ip_addr_list, offline_ip_addr_list

def is_in_or_out_time():
    current_time = datetime.now().time()
    if current_time <= PUNCH_IN_TIME:
        return PUNCH_STATUS.get('PUNCH_IN')
    elif current_time < PUNC_OUT_TIME:
        return PUNCH_STATUS.get('PUNCH_OUT')