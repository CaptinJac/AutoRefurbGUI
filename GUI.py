#begin GUI

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

def caller():    
    x = select.get()
    y = select1.get()
    z = select2.get()
    type = [x, y, z ]

    if sum(type) > 1:
        messagebox.showerror(title = "Oops!", message = "It looks like you selected to many options! Try again!")
    else:
        choice = type.index(1)
        if choice == 0:
            subprocess.call(r'classic.bat')
        elif choice == 1:
            subprocess.call(r'gamer.bat')
        else:
            subprocess.call(r'soon.bat')

root = Tk()
root.title("Auto Refurb Manager V1")
root.geometry("600x400")
tabControl = ttk.Notebook(root)

tab = ttk.Frame(tabControl)
tabControl.add(tab, text="Refurb")
tabControl.pack(expand = 1, fill="both")

Label(tab, text = "Choose Refurb Type").grid(row = 0, sticky = W)
Label(tab).grid(row = 1, sticky = W)

select = IntVar()
check = Checkbutton(tab, text = "Classic Reurb", variable = select).grid(row = 2, sticky = W)

select1 = IntVar()
check1 = Checkbutton(tab, text = "Gaming Refurb", variable = select1).grid(row = 3, sticky = W)

select2 = IntVar()
check2 = Checkbutton(tab, text = "Coming Soon", variable = select2).grid(row = 4, sticky= W)

fire = Button(tab, text = "Ready to Fire", command = caller).grid(row = 5, column = 4, sticky = W)
goodbye = Button(tab, text = "Exit", command = root.quit).grid(row = 5, column = 6, sticky = W)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Application Installer [BETA]")
tabControl.pack(expand = 1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="About")
tabControl.pack(expand = 1, fill="both")

root.mainloop()