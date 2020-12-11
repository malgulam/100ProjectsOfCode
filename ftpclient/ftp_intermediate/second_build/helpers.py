#!/usr/bin/python3

#imports
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pathlib import Path
from datetime import datetime

#tooltip class
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def initialise_session():
    print('----------------------------------------------------------------')
    print('                   SESSION STARTED                              ')
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')
    print('                    Writing Sesion To File                      ')
    print('----------------------------------------------------------------')
    home = str(Path.home())
    now = str(datetime.utcnow())
    if not os.path.exists(f'{home}/ftp_client/'):
        os.mkdir(f'{home}/ftp_client/')
    session_file = f'{home}/ftp_client/{now}.txt'
    with open(session_file, 'w') as f:
        f.write('SESSION FILE')
        f.write(f'Started:{now}')
    print('----------------------------------------------------------------')
    print('                    Finished Writing Session To File            ')
    print('----------------------------------------------------------------')

def connect(host, username, passwd, port):
    from ftplib import FTP, error_perm
    print(f'host:{host}, username:{username} passwd:{passwd}, port: {port}')
    #instance of ftp
    ftp = FTP()
    #set the debig level
    ftp.set_debuglevel(2)
    #connect to ftp
    ftp.connect(host=str(host), port=int(port))
    print('connected')
    #login
    print('login in.....')
    if username:
        if passwd:
            ftp.login(user=username, passwd=passwd)
        else:
            print('Password required')
            exit(0)
    else:
        #login without username and password
        ftp.login()
    #return the dirs list and ftp object
    dirs = list()
    files = list()
    ftp.retrlines("LIST", dirs.append)
    try:
        files = ftp.nlst()
    except error_perm as resp:
        if str(resp) == "550 No files found":
            print("No files in this directory")
            files = []
        else:
            raise
    return ftp, dirs,files

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

#function to create new_window
# def new_window(master=None):
#     #open new window
#     if master:
#         new_window = Toplevel(master)
#     else:
#         new_window = Toplevel()
#     #set the title
#     new_window.title('Remote Server')
#     new_window.geometry('905x805')
#     # TESTING REMOTE SERVER WINDOW
#     Label(new_window,text="HEY THERE" ).pack()
#
#class to create new_window
class newWindow(object):
    def __int__(self, master=None, title=None, geometry=None):
        self.master = master
        self.title = title
        self.geometry = geometry
        print(f'master: {self.master}, title:{self.title}, geometry:{self.geometry}')
        if self.master:
            self.new_window = Toplevel(self.master)
        else:
            self.new_window = Toplevel()
        #set the title of window
        self.new_window.title(self.title)
        #set the geometry
        if self.geometry:
            self.new_window.geometry(self.geometry)
        #testing the new window
        Label(self.new_window, text="HEY THERE").pack()
        print(self.new_window)
        return self.new_window

def retrieve_remote_dirs(remote_dirs_FRAME, ftp_obj, folder):
    remote_dirs_FRAME = remote_dirs_FRAME
    ftp_obj = ftp_obj
    folder = folder
    contents = ftp_obj.nlst(folder)
    sub_dirs = list()
    # first clear all widgets present in the frame
    for widget in remote_dirs_FRAME.winfo_children():
        widget.destroy()
    # perform the for loop  only if the dir is not empty
    if contents:
        for item in contents:
            item_as_str = str(item)
            root, ext = os.path.splitext(item_as_str)
            # if there is no extension, then it is an extension
            if not ext:
                dir_image_ = PhotoImage(file='ftpclient/ftp_intermediate/icons/directory.png')
                dir_image_button = Button(remote_dirs_FRAME, text="Directory Image")
                # dir_image_button = Button(remote_dirs_FRAME, image=dir_image_)
                dir_image_button.pack()
                Button(remote_dirs_FRAME, text=f"{item}").pack()
            else:
                file_image_ = PhotoImage(file='ftpclient/ftp_intermediate/icons/file.png')
                file_image_button = Button(remote_dirs_FRAME, text="File Image")
                # file_image_button = Button(remote_dirs_FRAME, image=dir_image_)
                file_image_button.pack()
                Button(remote_dirs_FRAME, text=f"{item}").pack()
    else:
        Label(remote_dirs_FRAME, text="No directories / files here!")