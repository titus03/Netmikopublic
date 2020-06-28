from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
host = input('Enter the Ip address:')
username  = input('Username:')
command1 = input('Enter command 1:')
command2 = input('Enter command 2:')
command3 = input('Enter command 3:')
command4 = input('Enter command 4:')
command5 = input('Enter command 5:')
start_time = datetime.now()
print(start_time)
cat4331 = {
    "device_type": "cisco_ios",
    "ip" : host,
    "username": username,
    "password": getpass(),
}
netconnect = ConnectHandler(**cat4331)
output = netconnect.send_command(command1)
print(output)
output = netconnect.send_command(command2)
print(output)
output = netconnect.send_command(command3)
print(output)
output = netconnect.send_command(command4)
print(output)
output = netconnect.send_command(command5)
print(output)

