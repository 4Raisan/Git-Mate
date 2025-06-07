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

adt = Button(root, text="History")
adt.grid(columnspan=2, row=0, column=5, ipadx=10, ipady=3, pady=10,padx=3)

refreshCount = 0
scnt = Label(root, text=f" Undos: {refreshCount}")
scnt.grid(columnspan=2, row=0, column=7, ipadx=10, ipady=3, pady=10)

justspace2 = Label(root, text="-")
justspace2.grid(row=0, column=10)


# PATH ---------------------------------------------------S

#---------Display
path = Label(root, text="PATH : ")
path.grid(row=1 ,column=2)

epath = Entry(root, fg="grey")
epath.insert(0,"Enter REPOs local path...")
epath.grid(columnspan=6, row=1, column=3, ipady=3, ipadx=60, pady=5, sticky='e')

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

def plusone():
    global ecountvalue
    ecountvalue+=1
    ecount.delete(0, END)
    ecount.insert(0,f"{ecountvalue}")
    ecount.grid(row=2, column=3, pady=5, sticky='w', ipady=3)
    
def minusone():
    global ecountvalue
    if ecountvalue>1:
        ecountvalue-=1
        ecount.delete(0, END)
        ecount.insert(0, f"{ecountvalue}")

def clearepath():
    epath.delete(0, END)
    epath.grid(columnspan=6, row=1, column=3, ipady=3,ipadx=60, pady=5)


# PATH ---------------------------------------------------E


# RUN - CMD
# > cd "C:\Users\4Raisan\Desktop\GitHub\Git-Mate"

# Count - input commit count
count = Label(root, text=" UNDOs : ")
count.grid(row=2, column=2)

ecount = Entry(root, width=2)
ecountvalue = 1
ecount.insert(0,f"{ecountvalue}")
ecount.grid(row=2, column=3, pady=5, sticky='w', ipady=3)

ecountplus = Button(root, text=" + ", command=plusone)
ecountplus.grid(row=2, column=3)

ecountminus = Button(root, text=" - ", command=minusone)
ecountminus.grid(row=2, column=3, sticky='e')

epathclear = Button(root, text="Clear Path", command=clearepath)
epathclear.grid(row=2, column=8)


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
Ctype = Label(root, text="\nAvoid use, if your last commit is a File Upload !\nRemember their is no REDOs")
Ctype.grid(rowspan=3, columnspan=8, row=3, column=2)

# Check box -----------------------------------

#check box command

def check_conf():
    global direpath
    if check_vrbl.get():
        readypath = epath.get().replace('"','')
        direpath = os.path.isdir(readypath)

direpath = False
        
# Variable to track checkbox state (1 = checked, 0 = unchecked) 
check_vrbl = IntVar()
checkbox =  Checkbutton(root, text="Confirm and Check Details", variable=check_vrbl, command=lambda: (check_conf(), passcheck()))
checkbox.grid(columnspan=4, row=6, column=3)

#--------------------------------------------

# Final UNDO --------------------------------

def fin0b():
    final0button = Button(root, text="> UNDO <", bg='gray')
    final0button.grid(columnspan=4, row=7, column=3, ipadx=10)

def fin1b():
    final1button  = Button(root, text="> UNDO <", bg='red')
    final1button.grid(columnspan=4, row=7, column=3, ipadx=10)

def signgreen():
    pathsign = Label(root,text="✅")
    pathsign.grid(row=1, column=1)

fin0b()
def passcheck():
    if direpath:
        fin1b()
#--------------------------------------------
# totcount(ecount.get())
# command=lambda: (confirmproceed(),checkpath())


# Additionals

# 1. Commit History
# > git log --oneline

# 2. Branch Check
# > git status

root.mainloop() # ending
