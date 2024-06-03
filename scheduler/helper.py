
### Lib import
import re
import subprocess

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