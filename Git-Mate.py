from tkinter import *
root = Tk()
from subprocess import *
import os

root.title("Git-Mate")
# Disable resizing (both horizontally and vertically)
root.resizable(False, False)


# Tops + Additionals
name = Button(root, text="Git-Mate")
name.grid(row=0, column=0)

adt = Button(root, text="additionals")
adt.grid(row=0, column=1)

refreshCount = 0
scnt = Label(root, text=f"Undos: {refreshCount}")
scnt.grid(row=0, column=2)


# PATH - input

path = Label(root, text="PATH : ")
path.grid(row=1 ,column=0)

epath = Entry(root, fg="grey")
epath.insert(0,"Enter REPOs local path...")
epath.grid(columnspan=2, row=1, column=1)

def focusepath(event):
    epath.delete(0, END)
    epath.config(fg="black")

def nofocusepath(event):
     if epath.get() == "":
         epath.insert(0,"Enter REPOs local path...")
         epath.config(fg="gray")

epath.bind("<FocusIn>", focusepath)
epath.bind("<FocusOut>", nofocusepath)


def checkpath():
    readypath = epath.get().replace('"','')
    direpath = os.path.isdir(readypath)
    

# RUN - CMD
# > cd "C:\Users\4Raisan\Desktop\GitHub\Git-Mate"

# Count - input commit count
count = Label(root, text="UNDOs : ")
count.grid(row=2, column=0)

ecount = Entry()
ecount.insert(0,"1")
ecount.grid(columnspan=2, row=2, column=1)


# RUN - CMD HEAD
# > git reset --hard HEAD~1


# UPDATE Total count + Refresh GUI
def totcount(new):
    global refreshCount
    new = int(new)
    refreshCount+=new
    scnt = Label(root, text=f"Undos: {refreshCount}")
    scnt.grid(row=0, column=2)


# Done - Confirm
# > git push origin main --force
Ctype = Label(root, text="Enter 'C' for confirm\nRemember their is no REDOs")
Ctype.grid(rowspan=2, columnspan=3, row=3, column=0)

econfirm = Entry()
econfirm.insert(0,"")
econfirm.grid(columnspan=3, row=5, column=0)

def confirmproceed():
    if (econfirm.get()).upper() == "C":
        totcount(ecount.get())
    econfirm.delete(0, END)


CButton = Button(root, text="UNDO", command=lambda: (confirmproceed(),checkpath()))
CButton.grid(columnspan=3, row=6, column=0)


# Additionals


# 1. Commit History
# > git log --oneline

# 2. Branch Check
# > git status

root.mainloop() # ending
