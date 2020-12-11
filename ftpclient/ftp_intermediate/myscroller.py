
from tkinter import *
from tkinter import ttk

win = Tk()

wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

#create canvas
mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LETF, fill="both", expand="both")

#initialise scrollbar
yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

#activvate scrollbar
mycanvas.configure(yscrollcommand=yscrollbar.set)

#bind function with mycanvas
mycanvas.bind('<Configure>', lambda e:mycanvas.configure(scrollregion = mycanvas.bbox("all")))

#create frame
myFrame = Frame(mycanvas)
mycanvas.create_window((0,0), window=myFrame, anchor="nw")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes",padx=10, pady=10)

for i in range(50):
    Button(myFrame, text=f"my button{i}").pack()

win.geometry('500x500')
#set resizable to False
win.resizable(False,False)
win.title('myscroller')
win.mainloop()
