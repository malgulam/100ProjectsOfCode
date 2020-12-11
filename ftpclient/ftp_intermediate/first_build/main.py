from tkinter import *
import os
from pathlib import Path
#globals declarations 
local_site = str(Path.home())
local_site_files = list(os.listdir(local_site))
print('Local files: ', local_site_files)
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
local_site_label = Label(root, text='Local site', padx=5, pady=5)
local_site_label.grid(row=2,column=0)
#local site frame
local_site_frame = LabelFrame(root, padx=30, pady=70)
local_site_frame.grid(row=3, column=0)
#variable to store last index file
last_indx_file = ''
#variable to store last index subdirectory/item
last_indx_sub = ''
#function to retrieve subdirs and files in a given dir
#do not take the name 'file' literally.I got this far with it.Will refactor
def view_folder_content(file):
    path = f'{Path.home()}/{file}'
    print('Path: ', path)
    # os.chdir(path)
    subs_ = list(os.listdir(path))
    print('Subs: ', subs_)
    #if the len of sub directories and items is less than or equal to 5 jus
    #view it on the screen
    if len(subs_) <=5:
        for item in subs_:
            Button(local_files_frame, text=item).grid(row=subs_.index(item))
    else:
        for item in subs_[:5]:
            if subs_.index(item) == 4:
                last_indx_sub = item[:]
                print('Last sub in group: ', last_indx_sub)
            Button(local_files_frame, text=item).grid(row=subs_.index(item))
    #empty label to create space between lisr of local files and buttons
    Label(local_files_frame).grid(row=6)
    if not len(subs_) <= 5:
        #create down and up buttons
        down_button = Button(local_files_frame, text="Down").grid(row=7, column=0)
        down_button = Button(local_files_frame, text="Up").grid(row=7, column=1)
    os.chdir(str(Path.home()))
#function to handle moving upwards in the frame
#where value is the last index
def _up(value):
    value += 1
    new_row_count = 0
    try:
        #first clear the already existing button
        #for widget in local_site_frame.winfo_children():
            # local_site_frame.grid_forget()
        #to destroy the widgets
        for widget in local_site_frame.winfo_children():
            widget.destroy()
        # for i in range(5):
        print('Value: ', value, 'New List: ', local_site_files[value:value+5])
        for file in list(local_site_files[value:value+5]):

            if list(local_site_files[value:value+5]).index(file) == 4:
                last_indx_file = file[:]
                print('Last file in group: ', last_indx_file)
            Button(local_site_frame, text=file, command=lambda: view_folder_content(file)).grid(row=new_row_count)
            new_row_count += 1
        up_button = Button(local_site_frame,text="Up", command=lambda:_up(value=local_site_files.index(last_indx_file))).grid(row=7,column=1)            
        down_button = Button(local_site_frame,text="Down", command=lambda:_down(value=local_site_files.index(last_indx_file))).grid(row=7,column=0)
    except IndexError:
        #first clear the already existing button
        #for widget in local_site_frame.winfo_children():
            # local_site_frame.grid_forget()
        #to destroy the widgets
        for widget in local_site_frame.winfo_children():
            widget.destroy()
        # for i in range(len(local_site_files[value:])):
        for file in local_site_files[value:]:
            if file == str(list(local_site_files[value:][-1])):
                last_indx_file == file[:]
            Button(local_site_frame, text=file).grid(row=new_row_count)
        up_button = Button(local_site_frame,text="Up", command=lambda:_up(value=local_site_files.index(last_indx_file))).grid(row=7,column=1)
        down_button = Button(local_site_frame,text="Down", command=lambda:_down(value=local_site_files.index(first_indx_file))).grid(row=7,column=0)
#function to handle moving downwards in the frame
#where value is the first index
first_indx_file = ''
def _down(value):
    try:
        #first clear the already existing button
        #for widget in local_site_frame.winfo_children():
            # local_site_frame.grid_forget()
        #to destroy the widgets
        for widget in local_site_frame.winfo_children():
            widget.destroy()
        #variable for new row count
        new_row_count = 0
        #value refers to index
        #firt rever the list
        try:
            retrieved_slice_of_original_local_files = local_site_files[value:value+5]
        except IndexError:
            retrieved_slice_of_original_local_files = local_site_files[value:]
        new_reverse_local_files_list = [i for i in retrieved_slice_of_original_local_files[::-1]]
        neg_index_of_value = -(value)
        print('New reversed local files', new_reverse_local_files_list, 'New negative index of the value: ', neg_index_of_value)
        #assigning first_file_indx her
        #todo: find bug and uncomment
        # first_file_indx = new_reverse_local_files_list[neg_index_of_value]
        # print('First file: ', first_file_indx)
        #while the new list len is greater than 5 do this
        # tmp = neg_index_of_value-1
        # new_list = new_reverse_local_files_list[tmp:tmp-5]
        if len(new_reverse_local_files_list) >=5:
            for file in [i for i in new_reverse_local_files_list[::-1]]:
                Button(local_site_frame, text=file, command=lambda:view_folder_content(file)).grid(row=new_row_count)
                new_row_count += 1
            up_button = Button(local_site_frame, text="Up", command=lambda:_up(value=local_site_files.index(last_indx_file))).grid(row=7,column=1)
            down_button = Button(local_site_frame,text="Down", command=lambda:_down(value=local_site_files.index(last_indx_file))).grid(row=7,column=0)
        else:
            for file in [i for i in new_reverse_local_files_list[::-1]]:
                Button(local_site_frame, text=file, command=lambda:view_folder_content(file)).grid()
            up_button = Button(local_site_frame, text="Up", command=lambda:_up(value=local_site_files.index(last_indx_file))).grid(row=7,column=1)
            down_button = Button(local_site_frame,text="Down", command=lambda:_down(value=local_site_files.index(last_indx_file))).grid(row=7,column=0)    
            
    except IndexError:
        #first clear the already existing button
        #for widget in local_site_frame.winfo_children():
            # local_site_frame.grid_forget()
        #to destroy the widgets
        for widget in local_site_frame.winfo_children():
            widget.destroy()
        print(e)
#create list of files in local site
if len(local_site_files) <=5:
    for file in local_site_files:
        Button(local_site_frame, text=file, command=lambda:view_folder_content(file)).grid(row=local_site_files.index(file))
else:
    for file in local_site_files[:5]:
        if local_site_files.index(file) == 4:
            last_indx_file = file[:]
            print('Last file in group: ', last_indx_file)
        Button(local_site_frame, text=file, command=lambda:view_folder_content(file)).grid(row=local_site_files.index(file))
#empty label to create space between list of local files and buttons
Label(local_site_frame).grid(row=6)
if not len(local_site_files) <=5:
    #create down and up buttons
    down_button = Button(local_site_frame,text="Down", command=lambda:_down(value=local_site_files.index(first_indx_file))).grid(row=7,column=0)
    up_button = Button(local_site_frame,text="Up", command=lambda:_up(value=local_site_files.index(last_indx_file))).grid(row=7,column=1)
#create remote site label
remote_site_label = Label(root, text='Remote site', padx=5, pady=5)
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
allLocalFilesList = Label(local_files_frame, text='this is a test all local files label')
allLocalFilesList.grid(row=0, column=0, padx=50, pady=60)
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