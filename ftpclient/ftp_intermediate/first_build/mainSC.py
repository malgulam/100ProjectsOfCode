from tkinter import *
import os
from pathlib import Path
import sys
sys.path.append(os.getcwd())
#globals declarations
local_site = str(Path.home())
local_site_files = list(os.listdir(local_site))
remote_site = 'REMOTE SITE'
root = Tk()
#set title
root.title("FTP Client")
#set default size of screen
root.geometry('905x805')
#create label for upper entries
entries_frame = LabelFrame(root, padx=10, pady=10)
entries_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=6)
#set entry to type hostname/ip
host_entry = Entry(entries_frame, width=10, borderwidth=2)
host_entry.grid(row=0, column=0, padx=10, pady=10)
host_entry.insert(0,'host')
#set entry to type username
username_entry = Entry(entries_frame, width=10, borderwidth=2)
username_entry.grid(row=0, column=1, padx=10, pady=10)
username_entry.insert(0,'username')
#set entry to type password
passwd_entry = Entry(entries_frame, width=10, borderwidth=2)
passwd_entry.grid(row=0, column=2, padx=10, pady=10)
passwd_entry.insert(0,'password')
#set entry to type port
port_entry = Entry(entries_frame, width=10, borderwidth=2)
port_entry.grid(row=0, column=3, padx=10, pady=10)
port_entry.insert(0,'port')
#adding quick connect button
quick_connect_button = Button(entries_frame, text="Quick Connect", padx=5, pady=5)
quick_connect_button.grid(row=0, column=4)
#create local site label
local_site_label = Label(root, text=f'Local site:{local_site}', padx=5, pady=5)
local_site_label.grid(row=2,column=0)
#local site frame
local_site_frame = LabelFrame(root, width = 70,
                                            height = 80,)
local_site_frame.grid(row=3, column=0)
#create a vertical scrollbar in the local site frame
# v_local = Scale(local_site_frame, from_=0, to=len(local_site_files), orient=VERTICAL)
# v_local.grid(sticky=E)
#create list of files in local site
#test code below
#testListLabel = Label(local_site_frame, text="this is a test local file label")
#testListLabel.grid(row=0, column=0, padx=50,pady=60)
#test code above
#uncomment if error arises
# for file in local_site_files:
    # Label(local_site_frame, text=file).grid(row=local_site_files.index(file), column=0)
#uncomment the above if error arises
#creating a scrolled textview to show list of local site
# local_site_files_text_area = st.ScrolledText(local_site_frame,
#                                             width = 30,
#                                             height = 8,
#                                             font = ("Times New Roman", 15))
# local_site_files_text_area.grid(column=0, pady=10, padx=10)                                            
#inserting the file names in local site files text area
def hello(event=None):
    print('hello')
for file in local_site_files:
    button = Button(local_site_frame,text=file, command=hello)
    # local_site_files_text_area.bind(file,hello)
    # local_site_files_text_area.insert(tk.INSERT, button)
    # local_site_files_text_area.insert(tk.INSERT, '\n')
#making text readonly
# local_site_files_text_area.configure(state='disabled')
#create remote site label
remote_site_label = Label(root, text=f'Remote site:{remote_site}', padx=5, pady=5)
remote_site_label.grid(row=2, column=3)
#remote site frame
remote_site_frame = LabelFrame(root, padx=30, pady=70)
remote_site_frame.grid(row=3, column=3)
#create list of files in remote site
remoteListLabel = Label(remote_site_frame, text='this is a test remote file label')
remoteListLabel.grid(row=0, column=0, padx=50, pady=60)
#create all local files label
allLocalFilesLabel = Label(root, text="All local files")
allLocalFilesLabel.grid(row=5, column=0)
#create all local files frame
local_files_frame = LabelFrame(root, padx=30, pady=70)
local_files_frame.grid(row=6,column=0)
#create list of all files in local_files_frame
#Test code below
allLocalFilesList = Label(local_files_frame, text='this is a test all local files label')
allLocalFilesList.grid(row=0, column=0, padx=50, pady=60)
#Test code above
#todo:create a label for each file in selected file in local_site_frame
#create all remote file label
allRemoteFilesLabel = Label(root, text="All remote files")
allRemoteFilesLabel.grid(row=5, column=3)
#create all remote files frame
remote_files_frame = LabelFrame(root, padx=30, pady=70)
remote_files_frame.grid(row=6, column=3)
#create lis of all files in remote_files_frame
allRemoteFilesList = Label(remote_files_frame, text='this is a test all remote files label')
allRemoteFilesList.grid(row=0, column=0, padx=50, pady=60)
#create status label
statusLabel = Label(root, text="status", padx=30, pady=70)
statusLabel.grid(row=9, column=5)
root.mainloop()
