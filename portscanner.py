# PORT SCANNER
# A CLI application to scan open ports on "," separated multiple IP addresses.


# Importing Libraries

import pyfiglet
import socket
import termcolor

# ASCII BANNER
ascii_banner = pyfiglet.figlet_format("PORT SCANNER ")
print(ascii_banner)
print("By Vasu")

# Scan the port upto user-defined range

def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)

# Using Socket Library for scanning port

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass


print("-" * 50)
targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
print("-" * 50)

print("-" * 50)
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
print("-" * 50)


# Main Function 
# Targets: taking input from the user as an IP address
# Ports: The number of ports you want to scan
# You can scan multiple ports too but they should be "," separated.


