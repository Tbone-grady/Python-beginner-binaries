import socket
import threading


bind_IP   = "0.0.0.0"
bind_port = 9999
# Use any port I'd suggest using ones in 25000-60000, systems admins won't look around their
# I'd suggest using a virtualmachine or VMware to test this out

server = socket.socket(socket.AF_INET. socket.SOCK_STREAM)
# if you forgot some of this do review some from previous script in 
# the comments 

server((bind_ip, bind_port))

server.listen(5)
# I gave a maximum backlog of connections at 5
# This informs the server to start listening

print "[*] Listening on %s:%d" % (bind_ip, bind_port)
# We put the server into its main loop waiting for inbound connections

	# We're going to print what the clients sends
		request = client_socket.recv(1024)
		
		print"[*] Recieved: %s" % request
		
		# send back a packet
		client.socket.send("ACK!")
		
		client.socket.close()
	
	While true:
	
		client,addr = server.accept()
		# When a client connects we recieve the clients socket and
		# transfers into the client variable and remote connection details into addr variable
		# this directs us to handle_client func. And we pass on that socket obj from our client as
		# an arguement
		
		print "[*] Accepted connection from: %s: %d" % (addr[0],addr[1])
		# there's the accepted connection to your TCP server 
		
		# Spin up our client thread to handle incoming data
		client_handler = threading.Thread(target=handle_client,args=(client,))
		client_handler.start()
		# We start a thread to handle a client connection and our main server is able to handle
		# another inbound connection

		# YOU COULD USE THE TCP CLIENT TO SEND SOME TEST PACKETS AND YOU SHOULD GET SOME OUTPUT 
		
		# THAT LOOKS LIKE SO
		
		##################################################
		#                                                #
		# [*] LISTENING ON 0.0.0.0:9999                  #
		# [*] Accepted connection from: 127.0.0.1:53402  #
		# [*] Recieved: ABCDEF                           #
		#                                                #
		##################################################