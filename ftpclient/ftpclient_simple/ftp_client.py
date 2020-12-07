import socket

#initialising socket
s = socket.socket()
#assinging host and port
host = input(str('what is the hostname of the device you will like to connect to?\n=> '))
port = 8082
#connecting the hostname and port
s.connect((host, port))

print (f'Connected to {host}')
