from tkinter import *
root = Tk()
from subprocess import *
import os

root.title("Git-Mate")
# custom windows size
#root.geometry("400x300")
# Disable resizing (both horizontally and vertically)
root.resizable(False, False)


# Tops + Additionals + Guide + Counter
justspace1 = Label(root, text="-")
justspace1.grid(row=0, column=0)

name = Button(root, text="Git-Mate")
name.grid(columnspan=2, row=0, column=1, ipadx=10, ipady=3, pady=10,padx=3)

guide = Button(root, text="User Guide")
guide.grid(columnspan=2, row=0, column=3, ipadx=10, ipady=3, pady=10,padx=3)

adt = Button(root, text="additionals")
adt.grid(columnspan=2, row=0, column=5, ipadx=10, ipady=3, pady=10,padx=3)

refreshCount = 0
scnt = Label(root, text=f"  Undos: {refreshCount}")
scnt.grid(columnspan=2, row=0, column=7, ipadx=10, ipady=3, pady=10)

justspace2 = Label(root, text="-")
justspace2.grid(row=0, column=10)


# PATH ---------------------------------------------------S

#---------Display
path = Label(root, text="PATH : ")
path.grid(row=1 ,column=2)

epath = Entry(root, fg="grey")
epath.insert(0,"Enter REPOs local path...")
epath.grid(columnspan=6, row=1, column=3, ipady=3,ipadx=66, pady=5)

#---------Focus
def focusepath(event):
    epath.delete(0, END)
    epath.config(fg="black")

def nofocusepath(event):
     if epath.get() == "":
         epath.insert(0,"Enter REPOs local path...")
         epath.config(fg="gray")

epath.bind("<FocusIn>", focusepath)
epath.bind("<FocusOut>", nofocusepath)

#---------Check Path Validity
def checkpath():
    readypath = epath.get().replace('"','')
    direpath = os.path.isdir(readypath)
    
# PATH ---------------------------------------------------E


# RUN - CMD
# > cd "C:\Users\4Raisan\Desktop\GitHub\Git-Mate"

# Count - input commit count
count = Label(root, text="UNDOs : ")
#count.grid(row=2, column=1)

ecount = Entry()
ecount.insert(0,"1")
#ecount.grid(row=2, column=2,ipady=3, pady=5)


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
#Ctype.grid(rowspan=2, columnspan=3, row=3, column=0)

econfirm = Entry()
econfirm.insert(0,"")
#econfirm.grid(columnspan=3, row=5, column=0)

def confirmproceed():
    if (econfirm.get()).upper() == "C":
        totcount(ecount.get())
    econfirm.delete(0, END)


CButton = Button(root, text="UNDO", command=lambda: (confirmproceed(),checkpath()))
#CButton.grid(columnspan=3, row=6, column=0)


# Additionals


# 1. Commit History
# > git log --oneline

# 2. Branch Check
# > git status

root.mainloop() # ending
