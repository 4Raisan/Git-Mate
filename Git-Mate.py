from tkinter import *
root = Tk()
from subprocess import *
import os

root.title("Git-Mate")
root.iconbitmap(r"C:\Users\4Raisan\Desktop\GitHub\Git-Mate\just-logo.ico")
# custom windows size
#root.geometry("400x300")
# Disable resizing (both horizontally and vertically)
root.resizable(False, False)
#root.configure(bg='black')


# Top Row --------------------------------------------------------

justspace1 = Label(root, text="-")
justspace1.grid(row=0, column=0)

justspace2 = Label(root, text="-")
justspace2.grid(row=0, column=10)
# ---

name = Button(root, text="Git-Mate")
name.grid(columnspan=2, row=0, column=1, ipadx=10, ipady=3, pady=10,padx=3)

guide = Button(root, text="User Guide")
guide.grid(columnspan=2, row=0, column=3, ipadx=10, ipady=3, pady=10,padx=3)
# ---

refreshCount = 0
scnt = Label(root, text=f" Undos: {refreshCount}")
scnt.grid(columnspan=2, row=0, column=7, ipadx=10, ipady=3, pady=10)

def totcount(new):   # UPDATE Total count + Refresh GUI
    global refreshCount
    new = int(new)
    refreshCount+=new
    scnt = Label(root, text=f"Undos: {refreshCount}")
    scnt.grid(columnspan=2, row=0, column=7, ipadx=10, ipady=3, pady=10)

# History ---
history = Button(root, text="History", state=DISABLED)
history.grid(columnspan=2, row=0, column=5, ipadx=10, ipady=3, pady=10,padx=3)

def avblhistory():
    history = Button(root, text="History")
    history.grid(columnspan=2, row=0, column=5, ipadx=10, ipady=3, pady=10,padx=3)

#Z Top Row --------------------------------------------------------


# PATH 1-Row---------------------------------------------------
# Check Signs ---
def signgreen():
    pathsign = Label(root,text="✅", fg='green')
    pathsign.grid(row=1, column=1)

def signred():
    pathsign = Label(root,text="❌", fg='red')
    pathsign.grid(row=1, column=1)

# Path Entry Focus ---
''' Test
def focusepath(event):
    epath.delete(0, END)
    epath.config(fg="black")

def nofocusepath(event):
     if epath.get() == "":
         epath.insert(0,"Enter REPOs local path...")
         epath.config(fg="gray")

epath.bind("<FocusIn>", focusepath)
epath.bind("<FocusOut>", nofocusepath)'''

# Path Label ---
path = Label(root, text="PATH : ")
path.grid(row=1 ,column=2)

# Path Entry ---
epath = Entry(root, fg="grey")
#epath.insert(0,"Enter REPOs local path...")
epath.insert(0,r"C:\Users\4Raisan\Downloads\Animes")
epath.grid(columnspan=6, row=1, column=3, ipady=3, ipadx=63, pady=5, sticky='e')

#Z  PATH 1-Row---------------------------------------------------


# Numbers 2-Row---------------------------------------------------
# Main Functions of Row 3
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

# Displaying
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

#Z Numbers 2-Row---------------------------------------------------


# Instruction 3/4/5-Row---------------------------------------------------

Ctype = Label(root, text="\nAvoid use, if your last commit is a File Upload !\nRemember their is no REDOs")
Ctype.grid(rowspan=3, columnspan=8, row=3, column=2)

#Z Instruction 3/4/5-Row---------------------------------------------------


# Check box 6-Row------------------------------------------------------

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

#Z Check box 6-Row------------------------------------------------------


# Undo Row-7------------------------------------------------------

def undoDenied():  # Denied
    final0button = Button(root, text="> UNDO <", state=DISABLED)
    final0button.grid(columnspan=4, row=7, column=3, ipadx=10)

def undoapproved():  # Approved
    final1button  = Button(root, text="> UNDO <", bg='red', command=undo)
    final1button.grid(columnspan=4, row=7, column=3, ipadx=10)

def undo():
    totcount(ecount.get())

undoDenied()
def passcheck():
    if direpath:
        undoapproved()
        avblhistory()
        signgreen()
    else:
        signred()

#Z Undo Row-7------------------------------------------------------


# RUN - CMD
# > cd "C:\Users\4Raisan\Desktop\GitHub\Git-Mate"

# RUN - CMD HEAD
# > git reset --hard HEAD~1

# Done - Confirm
# > git push origin main --force

# 1. Commit History
# > git log --oneline

# 2. Branch Check
# > git status


root.mainloop() # ending
