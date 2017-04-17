# UDP (User Datagram protocl)
# TCP (Traffic Control Protocol)

# Their won't be much to modify in the code
# Only two small variables need to be modified
# to output UDP packets

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# this we changed SOCK_STREAM to SOCK_DGRAM

# pitch that data to TAREX
client.sendto("AAABBBCCC",(target_host, target_port))
# This pitches the data TAREX server. UDP is a connectionless protocol
# You wont have a call to establish a connection beforehand 

# recive your data 
data, addr = client.recvfrom(4096)
# This allows us to receive our UDP data 
# It will also give us details on what TAREX remote host
# and port

print data 

