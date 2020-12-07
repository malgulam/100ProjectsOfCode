import socket

#initialising socket
s = socket.socket()
#assinging host and port
host = input(str('what is the hostname of the device you will like to connect to?\n=> '))
port = 9558
#connecting the hostname and port
s.connect((host, port))
print (f'Connected to {host}')
data = s.recv(1024)
print(data.decode())
running = True
while running:
    #receive command list
    command_list = s.recv(1024)
    command_list = command_list.decode()
    print('Commands list: ', command_list)
    command = input(str('Enter command: '))
    print('Processing')
    s.send(command.encode())
