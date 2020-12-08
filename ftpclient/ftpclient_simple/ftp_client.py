import base64
import os
import socket
import time
import pickle
from base64 import b64decode
#initialising socket
s = socket.socket()
#assinging host and port
host = input(str('what is the hostname of the device you will like to connect to?\n=> '))
port = 8083
#connecting the hostname and port
time.sleep(2)
s.connect((host, port))
print (f'Connected to {host}')
data = s.recv(2000)
print(data.decode())
time.sleep(2)
# receive command list
# command_list = s.recv(1024)
# command_list = command_list.decode()
# print('Commands list: ', command_list)
time.sleep(2)
running = True
try:
    try:
        # print('here')
        while running:
            # print('here2')
            command = input(str('Enter command: '))
            if command == 'retrieve':
                time.sleep(1)
                cwd = os.getcwd()
                print (f'file will be stored at {cwd}')
                s.send(command.encode())
                print('Processing')
                time.sleep(2)
                filename_response = s.recv(1024)
                print('Saving as: ', filename_response.decode())
                file_contents_response = s.recv(1024)
                file_contents_response = file_contents_response.decode()
                with open(f'{os.getcwd()}/{filename_response}', 'wb') as f:
                    f.write(file_contents_response)
                print('Done file transferring')

            #else treat the rest of the commands the same
            time.sleep(1)
            s.send(command.encode())
            print('Processing')
            time.sleep(2)
            command_response = s.recv(1024)
            command_response = (command_response).decode()
            print(command_response)

    except KeyboardInterrupt:
        print('QUITTING CLIENT....')
        s.close()
        exit(0)
except Exception as e:
    print (e)