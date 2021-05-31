#Install netmiko module using pip and run below command,This will help to login to remote device using SSH
from netmiko import ConnectHandler
#Import built-in getpass module for password prompt
import getpass
#Input Device Username
user = input("Username: ")
#Input password when prompted
password = getpass.getpass()

#Create a file which contains commands to execute on device in .txt format
with open('vyconfig.txt') as f:
    commands_list = f.read().splitlines()
#Create a file which contains device list/Ip addresses and save it in .txt format
#Open file and read contents one after the other
with open('devices2.txt') as f:
    devices_list = f.read().splitlines()
#For each item/IPs in devices_list, for loop will be executed
for devices in devices_list:
#print the below syntax along with the device name/IP
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
#Created dicionary and define values for each item and make sure to select device type as vyos for Vyatta and cisco_ios for Cisco devices
    vyos_12 = {
        'device_type': 'vyos',
        'ip': ip_address_of_device,
        'username': user,
        'password': password
        
    }
 # The below command connects the remote devices and run the commands as defined in the commands_list and save it in output variable 
    net_connect = ConnectHandler(**vyos_12)
    output = net_connect.send_config_set(commands_list)
#This will display the output     
    print (output)
#A new file will be created and import the output to the file for each items in devices_list file
    file = open(devices + '_output.txt', 'w')
    file.write(output)
#file is saved and closed
    file.close()

   

