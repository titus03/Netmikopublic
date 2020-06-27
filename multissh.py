from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
host1 = input('Enter the Ip address:')
host2 = input('Enter the Ip address:')
host3 = input('Enter the Ip address:')
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
for device in list["first", "second", "Basement"]:
    net_conn=ConnectHandler(**device)
    output = net_conn.send_command("show ip arp")
    print(output)


