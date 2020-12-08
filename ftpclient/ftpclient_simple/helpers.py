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
    if str(kwargs['first_command']).lower() == 'cd':
        splitted_command = command.split(' ')
        if splitted_command[1] != ' ':
            specified_dir = splitted_command[1]
            new_cwd = specified_dir[:]
            return f'Changed dir to {specified_dir}', new_cwd
        else:
            specified_dir = splitted_command[1]
            new_cwd = specified_dir[:]
            base_dir = str(Path.home())
            return f'Changed dir to {base_dir}', new_cwd
    if str(kwargs['first_command']).lower() == 'retrieve':
        splitted_command = command.split(' ')
        if splitted_command[1] != ' ':
            specified_file = splitted_command[1]
            filename_path = f'{kwargs["cwd"]}/{specified_file[:]}'
            if '/' in filename_path:
                file = filename_path.split('/')[-1]
                file_data = ''
                with open(filename_path, 'rb') as f:
                    lines = f.readlines()
                    for line in lines:
                        file_data += line.decode()
                return specified_file, file_data
            #else just read the file since we are in the cwd
            file_data = ''
            with open(specified_file, 'rb') as f:
                lines = f.readlines()
                for line in lines:
                    file_data += line.decode()
            return specified_file, file_data



