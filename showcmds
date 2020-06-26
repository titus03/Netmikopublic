from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
host = input('Enter the Ip address:')
Inputpath = input("Enter Input file path:")
outputpath = input("Enter Output file path:")
start_time = datetime.now()
print(start_time)
cat4331 = {
    "device_type": "cisco_ios",
    "ip" : host,
    "username": 'trozario',
    "password": getpass(),
}
def version():

    with open(Inputpath ,'r') as f:

        commands = f.read().splitlines()
        for list in commands:
            print("connecting to device" +  list)
            netconnect = ConnectHandler(**cat4331)
            output = netconnect.send_command(list)
            with open(outputpath,'a') as f:
                         f.write(output)
                         f.write("\n-----------end-------")
    print(output)
version()
