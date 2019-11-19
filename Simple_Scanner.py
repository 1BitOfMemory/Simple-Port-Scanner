import socket

#Get input
target = input('Input target IP address: ')
ports = input ('Enter port range: ')

#Split port range string to get high and low port
lowPort = int(ports.split('-')[0])
highPort = int(ports.split('-')[1])

#Verify settings
print("Scan ports", ports, "on machine", target, "? (Y/n): ")
resp = input() 

#Scan ports and print output
if (resp == 'Y'):
	for port in range (lowPort, highPort+1):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		status = s.connect_ex((target, port))
		if (status == 0):
			print(port, " - OPEN")
		else:
			print(port, " - CLOSED")	
		s.close()
else: 
	print("Exiting")
