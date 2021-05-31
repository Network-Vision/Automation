from netmiko import ConnectHandler
import getpass
user = input("Username: ")
password = getpass.getpass()


with open('config.txt') as f:
    commands_list = f.read().splitlines()

with open('devices.txt') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': user,
        'password': password
        
    }
    
    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_list)
    
    print (output)

    file = open(devices + '_output.txt', 'w')
    file.write(output)
    file.close()

   

