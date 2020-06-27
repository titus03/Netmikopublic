from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
host = input('Enter the Ip address:')
start_time = datetime.now()
print(start_time)
cat4331 = {
    "device_type": "cisco_ios",
    "ip" : host,
    "username": 'trozario',
    "password": getpass(),
}
netconnect = ConnectHandler(**cat4331)
output = netconnect.send_command_timing("delete flash:Plus.gif")
if 'Delete' in output:
    output +=netconnect.send_command_timing("\n")
netconnect.disconnect()
print(output)
