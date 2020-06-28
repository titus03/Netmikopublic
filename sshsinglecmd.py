from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
host = input('Enter the Ip address:')
username = input('Enter the Username ')
start_time = datetime.now()
command = input('Enter command :')
print(start_time)
cat4331 = {
    "device_type": "cisco_ios",
    "ip" : host,
    "username": username,
    "password": getpass(),
}
netconnect = ConnectHandler(**cat4331)
output = netconnect.send_command(command)
print(output)

