
### Lib import
import re
import subprocess
from datetime import datetime, time

# Parameters
OFFINE_MSG = 'Destination host unreachable'     # Echo message from router if destination ip is offline/invalid
ONLINE_ECHO_FAILED_MSG = 'Request timed out.'   # Echo message from router if destination ip's firewall blocks echo
ONLINE_ECHO_SUCCESS_MSG = '0% loss'             # Echo message from router 
PUNCH_IN_TIME_MAX_TH= time(11, 0, 0)            # Max threashold time for punch in (11:00:00)
PUNC_OUT_TIME_MIN_TH = time(6, 0, 0)            # Min. threshold time for punch out (6:00:00)
MAC_ADDR_PATTERN = '([-0-9a-f]{17})'            # Mac address pattern in arp table
OPERATION_TYPES = {
    'PUNCH_IN': 'PI',
    'PUNCH_OUT': 'PO'
}

def get_mac_addr_list(ip_addr_list):
    ip_mac_table = {}
    for ip_addr in ip_addr_list:
        arp_req_command = 'arp -a ' + ip_addr
        result = subprocess.run(arp_req_command, stdout=subprocess.PIPE)
        arp_info = result.stdout.decode('utf8')
        
        # Extract mac
        matched_mac_addr_list = re.findall(MAC_ADDR_PATTERN, arp_info)
        
        # if matched then will have matched list, if not then []
        if len(matched_mac_addr_list) != 0:
            ip_mac_table[ip_addr] = matched_mac_addr_list[0]
    return ip_mac_table

def ping_device(ip_addr):
    """
    Function to ping the ip and return the echo message
    """

    ping_command = 'ping -n 1 '+ ip_addr    
    result = subprocess.run(ping_command, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf8')
    return output
    
def get_online_offline_devices(ip_addr_list):

    """
    1. For each of the ip-address, ping the device.
    2. Check the message echoed from ping.
    3. Based on the message echoed, insert the pinged ip in offline bucket or online bucket
    4. Return both bucket
    """

    online_ip_addr_list = []
    offline_ip_addr_list = []
    
    for ip_addr in ip_addr_list:
        output = ping_device(ip_addr)
        if OFFINE_MSG in output:
            offline_ip_addr_list.append(ip_addr)
        elif  ONLINE_ECHO_FAILED_MSG in output or ONLINE_ECHO_SUCCESS_MSG in output:
            online_ip_addr_list.append(ip_addr)

    return online_ip_addr_list, offline_ip_addr_list

def get_operation_type():
    """
    Return the action type: punch in/out.
    If it is before 11:00:00 then PI (PUNCH IN)
    If it is after 06:00:00 then PO (PUNCH OUT)
    """

    current_time = datetime.now().time()
    if current_time <= PUNCH_IN_TIME_MAX_TH:
        return OPERATION_TYPES.get('PUNCH_IN')
    elif current_time > PUNC_OUT_TIME_MIN_TH:
        return OPERATION_TYPES.get('PUNCH_OUT')