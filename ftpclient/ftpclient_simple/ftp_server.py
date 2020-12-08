import socket
import random
import time
from pathlib import Path
import os
import sys
sys.path.append(os.getcwd())
from helpers import command_processing
#initialising socket
s = socket.socket()
#assinging host and port
host = socket.gethostname()
port = 8081
print (f"FTP active\nHostname:{host}\nPort:{port}")
# try:
#binding the hostname and port
s.bind((host, port))
#listen to just one connection at a time
s.listen(1)
conn, addr = s.accept()
print (f'{addr} has just connected')
#send the user the base path and instructions
base_path = str(Path.home())
base_path_data_to_send = f'Base path of Host:{host}  is {base_path}\nYou may use simple linux commands such as "cd" to change directory'
conn.send(base_path_data_to_send.encode())
# send command list to user
commands = {'cd': 'change directory', "ls": 'list dirs in a given directory'}
commands_as_str = ''
for command in commands.keys():
    commands_as_str += f'{command} => {commands[command]} \n'
# print(commands_as_str)
# send commands_list
conn.send(commands_as_str.encode())
time.sleep(2)
#setting current cwd as global variable to help with cd and ls commands
cwd = str(os.getcwd())
running = True
try:
    while running:
        # receive commands
        time.sleep(3)
        command = (conn.recv(1024)).decode() + ' '
        full_command = command.split(' ')
        first_command = command.split(' ')[0]
        print(f'Received command: {command}\nFrom: {addr}')
        if first_command in commands.keys():
            response = command_processing(command, cwd=os.getcwd(), command_argument=full_command[1], first_command=first_command)
            print(response)
            conn.send(response.encode())
        else:
            response = 'command not in supported commands dict'
            print (response)
            conn.send(response.encode())
except KeyboardInterrupt:
    print ('QUITTING SERVER....')
    conn.close()
    exit(0)
# except Exception as e:
#     print (e)
#     print('Try changing the port')
#     exit(1)