import base64
import json
import socket
import random
import time
from pathlib import Path
import os
import sys
import pickle

sys.path.append(os.getcwd())
from helpers import command_processing
#initialising socket
s = socket.socket()
#assinging host and port
host = socket.gethostname()
port = 8083
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
base_path_data_to_send = f'Base path of Host:{host}  is {base_path}\nYou may use simple linux commands such as "cd" to change directory, \n"ls" to list directories\n"retrieve "your_file_name" to retrieve a file.Eg)retrieve temp/temp.txt.NB:This saves all files to your current working directory(This project) by default unless you use the "cd" directory to change directory firt to your desired path then you have to use the full(absolute) path of the file you want to download"'
conn.send(base_path_data_to_send.encode())
# send command list to user
commands = {'cd': 'change directory', "ls": 'list dirs in a given directory', 'retrieve':'retrieve a file from the server.Eg)retrieve temp/temp.txt.NB:This saves all files to your current working directory(This project) by default unless you use the "cd" directory to change directory firt to your desired path then you have to use the full(absolute) path of the file you want to download'}
commands_as_str = ''
for command in commands.keys():
    commands_as_str += f'{command} => {commands[command]} \n'
# print(commands_as_str)
# send commands_list
conn.send(commands_as_str.encode())
time.sleep(2)
#setting current cwd as global variable to help with cd and ls commands
global cwd
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
            if first_command == 'cd':
                response, cwd = command_processing(command,cwd=os.getcwd(), command_argument=full_command[1], first_command=first_command)
                if cwd:
                    try:
                        os.chdir(cwd)
                    except FileNotFoundError:
                        print(f'File{cwd} does not exists')
                else:
                    try:
                        os.chdir(Path.home())
                    except FileNotFoundError:
                        print(f'File{cwd} does not exists')
                print(response)
                conn.send(response.encode())
            if first_command == 'ls':
                response = command_processing(command, cwd=os.getcwd(), command_argument=full_command[1], first_command=first_command)
                print(response)
                conn.send(response.encode())
            if first_command == 'retrieve':
                filename, file_data = command_processing(command, cwd=os.getcwd(), command_argument=full_command[1], first_command=first_command)
                print({filename:file_data})
                #first send the filename
                conn.send(filename.encode())
                #secondly send data
                time.sleep(2)
                conn.send(file_data.encode())
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