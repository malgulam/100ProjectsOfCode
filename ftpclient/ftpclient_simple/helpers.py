#!/usr/bin/python3
import os
from pathlib import Path
#function to process commands
def command_processing(command, **kwargs):
    commands = ['ls', 'cd']
    if str(kwargs['first_command']).lower() == 'ls':
        splitted_command = command.split(' ')
        if splitted_command[1] != ' ':
            specified_dir = splitted_command[1]
            print(specified_dir)
            dirs = os.listdir(f'{kwargs["cwd"]}/{specified_dir}')
            return str(dirs)
        else:
            return str(os.listdir(kwargs['cwd']))
            # return f'{command}, {len(splitted_command)}, {splitted_command}, sad'
        # print(command)
        # if command.split(' ')[1] != ' ':
        #     return str(os.listdir(str(kwargs['cwd']) + str(command.split(' ')[1])))
        # else:
        #     return str(os.listdir(kwargs['cwd']))


