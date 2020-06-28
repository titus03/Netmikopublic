from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
host1 = input('Enter the Ip address:')
host2 = input('Enter the Ip address:')
host3 = input('Enter the Ip address:')
command1 = input('Enter command 1:')
command2 = input('Enter command 2:')
command3 = input('Enter command 3:')
command4 = input('Enter command 4:')
command5 = input('Enter command 5:')
password = getpass()
start_time = datetime.now()
print(start_time)
first = {
    "device_type": "cisco_ios",
    "ip" : host1,
    "username": 'trozario',
    "password": password,
}

second = {
    "device_type": "cisco_ios",
    "ip" : host2,
    "username": 'trozario',
    "password": password,
}

Basement = {
    "device_type": "cisco_ios",
    "ip" : host3,
    "username": 'trozario',
    "password": password,
}
for device in (first, second, Basement):
    netconnect=ConnectHandler(**device)
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
