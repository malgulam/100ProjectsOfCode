#!/usr/bin/python3

# imports
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from pathlib import Path
import helpers
import remote_server

# starting session
print('STARTED FTP Client')
helpers.initialise_session()

# declaring globals
ftp = None
remote_dirs = None
remote_files = None
status = 'Not Connected'
remote_server_window = None
running_state = None
# assigning root the Tk() class
root = Tk()

# configuring main window properties

# set the title
root.title("FTP Client")

# set the default screen size
root.geometry('905x805')

# create frames

# create button_options_frame
button_options_frame = LabelFrame(root, padx=10, pady=10)
button_options_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=6, sticky=W + E)

# create entries frame
entries_frame = LabelFrame(root, padx=10, pady=10)
# position entries_frame
entries_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=6, sticky=W + E)

#griding entries into entries_frame

# Creating Label  by the host_entry input
Label(entries_frame, text="Host:").grid(row=0, column=0)
# create host_entry input
host_entry = Entry(entries_frame, width=10, borderwidth=2)
host_entry.grid(row=0, column=1)
# putting default value  of host in host_entry input
host_entry.insert(0, "192.168.1.4")

# Creating Label by the username_entry input
Label(entries_frame, text="Username:").grid(row=0, column=2)
# create username_entry input
username_entry = Entry(entries_frame, width=10, borderwidth=2)
username_entry.grid(row=0, column=3)
# putting default value  of username in username_entry input
username_entry.insert(0, 'francis')

# Creating Label by the passwd_entry inoput
Label(entries_frame, text="Password:").grid(row=0, column=4)
# create passwd_entry input
passwd_entry = Entry(entries_frame, width=10, borderwidth=3)
passwd_entry.grid(row=0, column=5)
# putting default value of password in passwd_entry
passwd_entry.insert(0, 'francis')
# Creating Label by the port_entry input
Label(entries_frame, text='Port:').grid(row=0, column=6)
# create port_entry
port_entry = Entry(entries_frame, width=10, borderwidth=3)
port_entry.grid(row=0, column=7)
# putting default value of port in port_entry
port_entry.insert(0, 2221)

#function to take control of windows whilst running
def running():
    if running_state:
        print('-------------------------------')
        print('             running           ')
        print('-------------------------------')
        pass
# creating connect button in button_options_frame
# load icons/connect_big.png
connect_image = ImageTk.PhotoImage(Image.open("ftpclient/ftp_intermediate/icons/connect_big.png"))

# sub function to handle the connect  function in helpers and assign to globals the return value of the function
def sub_connect():
    global ftp
    global remote_dirs
    global remote_files
    global status
    ftp, remote_dirs, remote_files = helpers.connect(host=host_entry.get(), username=username_entry.get(),
                                                     passwd=passwd_entry.get(),
                                                     port=port_entry.get())
    print(f'Remote Dirs: {remote_dirs}')
    print(f'Remote Files: {remote_files}')
    # clear status frame
    for widget in status_frame.winfo_children():
        widget.destroy()
    # set status to Connected
    import time
    status = 'Connected'
    status_label = Label(status_frame, text=f"Status: {status}", padx=10, pady=10)
    status_label.grid(stick=W + E)
    # time.sleep(5)
    #destroy other widgets
    for widget in status_frame.winfo_children():
        widget.destroy()
    # set status to Ready
    status = 'Ready'
    status_label = Label(status_frame, text=f"Status: {status}", padx=10, pady=10)
    status_label.grid(stick=W + E)
    global remote_server_window
    # remote_server_window = helpers.new_window()
    remote_server_window = remote_server.RemoteServer(geometry="905x805",remote_dirs=remote_dirs, remote_files=remote_files, ftpObj=ftp)
    global running_state
    running_state = 'running'
    return running()


# label with Image
c_btn = Button(button_options_frame, image=connect_image, command=lambda: sub_connect())
c_btn.grid(row=0, column=0)

# creating tooltip on hover of the c_btn
helpers.CreateToolTip(c_btn, text='Connect')

# bind click event to connect_image
# c_btn.bind('<Button-1>', helpers.connect(host=host_entry.get(), username=username_entry.get(), passwd=passwd_entry.get(), port=int(port_entry.get())))

#create a frame to store all remote dirs

# creating status frame
status_frame = LabelFrame(root, padx=10, pady=10)
status_frame.grid(row=9, columnspan=6, sticky=E)
# create status label
status_label = Label(status_frame, text=f"Status: {status}", padx=10, pady=10)
status_label.grid(stick=W + E)



root.mainloop()
