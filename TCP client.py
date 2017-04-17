import socket
# Our tarex is google
# TAREX (Target to exfiltrate data from)

target_host = "www.google.com" # tarex
target_port = 80 # port

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET specifies that IPv4 address or the hostname
# SOCK_STREAM indicates this will be a TCP client ONLY


# connect the TAREX client
client.connect((target_host,target_port))
#This connects to our system to our google TAREX server


# send some data to identify whether TAREX server is up 
client.send("Get /HTTP/1.1\nHost: google.com\r\n\r\n")
# sending some data through port 80 on google.com 

# recieve some data
response = client.recv(4096)

#print out responce from TAREX

print reponse

# A very straightforward and basic TCP client
# When hacking you'll find yourself writing
# these more often than anything else 
