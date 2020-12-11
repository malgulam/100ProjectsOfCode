from tkinter import *
from tkinter import ttk

win = Tk()

remote_dirs_frame = LabelFrame(win)
remote_dirs_contents_frame = LabelFrame(win)

#create canvas
mycanvas = Canvas(remote_dirs_frame)
mycanvas.pack(side=LEFT, fill="both", expand="y")
mycanvas2 = Canvas(remote_dirs_contents_frame)
mycanvas2.pack(side=LEFT, fill="both", expand="y")

#initialise scrollbar
yscrollbar = ttk.Scrollbar(remote_dirs_frame, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")
yscrollbar2 = ttk.Scrollbar(remote_dirs_contents_frame, orient="vertical", command=mycanvas2.yview)
yscrollbar2.pack(side=RIGHT, fill="y")

#activvate scrollbar
mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas2.configure(yscrollcommand=yscrollbar2.set)

#bind function with mycanvas
mycanvas.bind('<Configure>', lambda e:mycanvas.configure(scrollregion = mycanvas.bbox("all")))
mycanvas2.bind('<Configure>', lambda e:mycanvas2.configure(scrollregion = mycanvas2.bbox("all")))

#create frame
myFrame = Frame(mycanvas)
myFrame2 = Frame(mycanvas2)
mycanvas.create_window((0,0), window=myFrame, anchor="nw")
mycanvas2.create_window((0,0), window=myFrame2, anchor="nw")

Label(win, text="Remote Dirs").pack()
remote_dirs_frame.pack(fill="both", expand="yes", padx=10, pady=10)
Label(win, text="Remote Dirs Contents").pack()
remote_dirs_contents_frame.pack(fill="both", expand="yes",padx=10, pady=10)

for i in range(50):
    Button(myFrame, text=f"my button{i}").pack()

for i in range(50):
    Button(myFrame2, text=f"my button{i}").pack()

win.geometry('500x500')
#set resizable to False
win.resizable(False,False)
win.title('myscroller')
win.mainloop()