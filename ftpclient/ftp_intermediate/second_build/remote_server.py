#this file handles all matters relating to the remote_server window

import time
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import helpers
from functools import partial
from pathlib import Path


class RemoteServer(object):
    def __init__(self, master=None, title='Remote Server', geometry=None, remote_dirs=None, remote_files=None, ftpObj=None):
        self.master = master
        self.title = title
        self.geometry = geometry
        self.remote_dirs = remote_dirs
        self.remote_files = remote_files
        self.ftpObj = ftpObj
        self.folder = self.ftpObj.pwd()
        print(f'RemoteServer-Remote dirs:{self.remote_dirs}, \n\n\nRemoteServer-Remote files:{self.remote_files}')
        remote_server_window = helpers.newWindow.__int__(self,master=self.master, title=self.title, geometry=self.geometry)
        self.remote_server_window = remote_server_window
        # remote_server_window = Toplevel(self.master)
        # remote_server_window = Tk()
        #destroy all elements present first
        for widget in remote_server_window.winfo_children():
            widget.destroy()
        remote_dirs_frame = LabelFrame(remote_server_window)
        remote_dirs_contents_frame = LabelFrame(remote_server_window)

        # create canvas
        remote_dirs_frame_canvas = Canvas(remote_dirs_frame)
        remote_dirs_frame_canvas.pack(side=LEFT, fill="both", expand="y")
        remote_dirs_contents_frame_canvas = Canvas(remote_dirs_contents_frame)
        remote_dirs_contents_frame_canvas.pack(side=LEFT, fill="both", expand="y")

        # initialise scrollbar
        yscrollbar = ttk.Scrollbar(remote_dirs_frame, orient="vertical", command=remote_dirs_frame_canvas.yview)
        yscrollbar.pack(side=RIGHT, fill="y")
        yscrollbar2 = ttk.Scrollbar(remote_dirs_contents_frame, orient="vertical", command=remote_dirs_contents_frame_canvas.yview)
        yscrollbar2.pack(side=RIGHT, fill="y")

        # activvate scrollbar
        remote_dirs_frame_canvas.configure(yscrollcommand=yscrollbar.set)
        remote_dirs_contents_frame_canvas.configure(yscrollcommand=yscrollbar2.set)

        # bind function with remote_dirs_frame_canvas
        remote_dirs_frame_canvas.bind('<Configure>', lambda e: remote_dirs_frame_canvas.configure(scrollregion=remote_dirs_frame_canvas.bbox("all")))
        remote_dirs_contents_frame_canvas.bind('<Configure>', lambda e: remote_dirs_contents_frame_canvas.configure(scrollregion=remote_dirs_contents_frame_canvas.bbox("all")))

        # create frame
        remote_dirs_FRAME = Frame(remote_dirs_frame_canvas)
        remote_dirs_contents_FRAME = Frame(remote_dirs_contents_frame_canvas)
        remote_dirs_frame_canvas.create_window((0, 0), window=remote_dirs_FRAME, anchor="nw")
        remote_dirs_contents_frame_canvas.create_window((0, 0), window=remote_dirs_contents_FRAME, anchor="nw")

        Label(remote_server_window, text="Remote Dirs").pack()
        remote_dirs_frame.pack(fill="both", expand="yes", padx=10, pady=10)
        Label(remote_server_window, text="Remote Dirs Contents").pack()
        remote_dirs_contents_frame.pack(fill="both", expand="yes", padx=10, pady=10)


        for self.item in self.remote_files:
            self.item_as_str = str(self.item)
            root, ext = os.path.splitext(self.item_as_str)
            # if there is no extension, then it is an extension
            if not ext:
                dir_image_ = PhotoImage(file='ftpclient/ftp_intermediate/icons/directory.png')
                dir_image_button = Button(remote_dirs_FRAME, text="Directory Image")
                # dir_image_button = Button(remote_dirs_FRAME, image=dir_image_)
                dir_image_button.pack()
                # Button(remote_dirs_FRAME, text=f"{self.item}", command= lambda : RemoteServer.retrieve_remote_dirs(self, remote_dirs_FRAME=remote_dirs_contents_FRAME, ftp_obj=self.ftpObj, folder=self.item)).pack()
                Button(remote_dirs_FRAME, text=f"{self.item}", command= partial(RemoteServer.retrieve_remote_dirs, self, remote_server_window=remote_server_window, remote_dirs_FRAME=remote_dirs_contents_FRAME, ftp_obj=self.ftpObj, folder=self.item)).pack()
            #else it is a file
            else:
                file_image_ = PhotoImage(file='ftpclient/ftp_intermediate/icons/file.png')
                file_image_button = Button(remote_dirs_FRAME, text="File Image")
                # file_image_button = Button(remote_dirs_FRAME, image=dir_image_)
                file_image_button.pack()
                # Button(remote_dirs_FRAME, text=f"{self.item}").pack()
                Button(remote_dirs_FRAME, text=f"{self.item}",
                       command=partial(RemoteServer.show_popup_options, self, remote_server_window=remote_server_window,
                                       ftpObj=self.ftpObj, type='file', folder=self.folder,
                                       filename_or_dirname=self.item)).pack()
        #placeholder in remote_dirs_contents_FRAME
        Label(remote_dirs_contents_FRAME, text="remote dirs contents fo here").pack()
        # for i in range(50):
        #     Button(remote_dirs_contents_FRAME, text=f"my button{i}").pack()

    def retrieve_remote_dirs(self, remote_server_window, remote_dirs_FRAME, ftp_obj, folder):
        self.remote_server_window = remote_server_window
        self.remote_dirs_FRAME = remote_dirs_FRAME
        self.ftp_obj = ftp_obj
        self.folder = folder
        self.contents = self.ftp_obj.nlst(self.folder)
        self.sub_dirs = list()
        print(f'remote_dirs_frame:{remote_dirs_FRAME}, ftp_obj:{ftp_obj}, folder:{folder}, self.contents:{self.contents}')
        #first clear all widgets present in the frame
        for self.widget in self.remote_dirs_FRAME.winfo_children():
            self.widget.destroy()
        #perform the for loop  only if the dir is not empty
        if self.contents:
            for self.item in self.contents:
                self.item_as_str = str(self.item)
                root, ext = os.path.splitext(self.item_as_str)
                #if there is no extension, then it is an extension
                if not ext:
                    dir_image_ = PhotoImage(file='ftpclient/ftp_intermediate/icons/directory.png')
                    dir_image_button = Button(self.remote_dirs_FRAME, text="Directory Image")
                    # dir_image_button = Button(remote_dirs_FRAME, image=dir_image_)
                    dir_image_button.pack()
                    Button(remote_dirs_FRAME, text=f"{self.item}", command=partial(RemoteServer.show_popup_options, self, remote_server_window=self.remote_server_window, ftpObj=self.ftpObj, type='directory', folder=self.folder, filename_or_dirname=self.item)).pack()
                else:
                    file_image_ = PhotoImage(file='ftpclient/ftp_intermediate/icons/file.png')
                    file_image_button = Button(self.remote_dirs_FRAME, text="File Image")
                    # file_image_button = Button(remote_dirs_FRAME, image=dir_image_)
                    file_image_button.pack()
                    Button(remote_dirs_FRAME, text=f"{self.item}", command=partial(RemoteServer.show_popup_options, self, remote_server_window=remote_server_window, ftpObj=self.ftpObj, type='file', folder=self.folder, filename_or_dirname=self.item)).pack()
        else:
            Label(remote_dirs_FRAME, text="No directories / files here!")
    #method to  show popup on button click in the remote_dirs_contents_FRAME
    def show_popup_options(self, remote_server_window, ftpObj, type, folder, filename_or_dirname):
        self.remote_sever_window = remote_server_window
        self.ftpObj = ftpObj
        #here type could either be file or directory
        self.type = type
        self.folder = folder
        self.filename_or_dirname = filename_or_dirname
        #first create a new window
        popup_window = helpers.newWindow.__int__(self,master=self.remote_sever_window, title='Opitions', geometry='650x650')
        #destroying all widgets in popup_window
        for widget in popup_window.winfo_children():
            widget.destroy()
        #creating popup options based on self.type.ie.)either file or directory
        if self.type == 'file':
            #create download button
            download_button = Button(popup_window, text="Download", command=lambda: RemoteServer.download(self, ftp_obj=self.ftpObj, path=self.folder, filename_or_dirname=self.filename_or_dirname)).pack()
        else:
            # create download button
            #todo: create view children function
            download_button = Button(popup_window, text="Download",
                                     command=lambda: RemoteServer.download(self, ftp_obj=self.ftpObj, path=self.folder,
                                                                           filename_or_dirname=self.filename_or_dirname)).pack()
    #method to download items from remote sevrer
    def download(self, ftp_obj, path, filename_or_dirname, to_path=f'{str(Path.home())}/Desktop'):
        self.ftp_obj = ftp_obj
        self.path = path
        self.filename_or_dirname = filename_or_dirname
        self.to_path = to_path
        #first change the cwd
        self.ftp_obj.cwd(f'{self.path}')
        handle = open(f'{to_path}/{filename_or_dirname}', 'wb')
        print(f'path:{path}, filename_or_dirname:{filename_or_dirname}')
        # retrieved_contents = self.ftp_obj.retrbinary(f'RETR {path}/{filename_or_dirname}', handle.write)
        retrieved_contents = self.ftp_obj.retrbinary(f'RETR {filename_or_dirname}', handle.write)
        handle.close()
        return
