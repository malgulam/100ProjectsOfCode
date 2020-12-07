import socket
import random
from pathlib import Path
#initialising socket
s = socket.socket()
#assinging host and port
host = socket.gethostname()
port = 9558
print (f"FTP active\nHostname:{host}\nPort:{port}")
try:
    #binding the hostname and port
    s.bind((host, port))
    #listen to just one connection at a time
    s.listen(1)
    conn, addr = s.accept()
    print (f'{addr} has just connected')
    #send the user the base path and instructions
    base_path = str(Path.home())
    base_path_data_to_send = f'Base path of Host:{host}  is {base_path}\nYou may use simple linux commands such as "cd" to change directory'
    conn.sendto(base_path_data_to_send.encode(), addr)
    running = True
    while running:
        #send command list to user
        commands = {'cd':'change directory'}
        commands_as_str = ''
        for command in commands.keys():
            commands_as_str += f'{command} => {commands[command]} \n'
        # print(commands_as_str)
        #send commands
        conn.sendto(commands_as_str.encode(), addr)
        # receive commands
        command = (conn.recv(1024)).decode()
        print(command)
except Exception as e:
    print (e)
    print('Try changing the port')