import tkinter as tk
from tkinter import ttk
def popupmsg(msg, title):
    root =  tk.Tk()
    root.title(title)
    label = ttk.Label(root, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(root, text="Okay", command=root.destroy)
    B1.pack()
    root.mainloop()
popupmsg('hey', 'hey')