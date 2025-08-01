from tkinter import *
root = Tk()
from subprocess import *
from tkinter.scrolledtext import ScrolledText
import os

root.title("Git-Mate   - v1.0")
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

name = Button(root, text="Git-Mate", bg='#00FF00', font=("Courier New", 9, 'bold'))
name.grid(columnspan=2, row=0, column=1, ipadx=9, ipady=2, pady=10,padx=3)

guide = Button(root, text="User Guide", bg="#0777FF", font=("Courier New", 9, 'bold'))
guide.grid(columnspan=2, row=0, column=3, ipadx=9, ipady=2, pady=10,padx=3)
# ---

# History ---
history = Button(root, text="History", font=("Courier New", 9, 'bold'), state=DISABLED)
history.grid(columnspan=2, row=0, column=5, ipadx=9, ipady=2, pady=10,padx=3)

def avblhistory():
    history = Button(root, text="History", bg="#C100F7", font=("Courier New", 9, 'bold'), command=showhistory)
    history.grid(columnspan=2, row=0, column=5, ipadx=9, ipady=2, pady=10,padx=3)

def showhistory():
    myhis = run(["git log --oneline"], shell=True, capture_output=True, text=True)
    print(myhis.stdout)

# Count ---
refreshCount = 0
scnt = Label(root, text=f"Undos: {refreshCount}", bg="#FBFF00", font=("Courier New", 9, 'bold'))
scnt.grid(columnspan=2, row=0, column=7, ipadx=9, ipady=5, padx=3)

def totcount(new):   # UPDATE Total count + Refresh GUI
    global refreshCount
    new = int(new)
    refreshCount+=new
    scnt = Label(root, text=f"Undos: {refreshCount}", bg="#FBFF00", font=("Courier New", 9, 'bold'))
    scnt.grid(columnspan=2, row=0, column=7, ipadx=9, ipady=5, padx=3)

#Z Top Row --------------------------------------------------------


# PATH 1-Row---------------------------------------------------
# Check Signs ---
def signgreen():
    global pathsign
    pathsign = Label(root,text=" ✅", fg='green')
    pathsign.grid(columnspan=2, row=1, column=1, sticky='w')

def signred():
    global pathsign
    pathsign = Label(root,text=" ❌", fg='red')
    pathsign.grid(columnspan=2, row=1, column=1, sticky='w')

# Path Label ---
path = Label(root, text="PATH : ")
path.grid(row=1 ,column=2)

# Path Entry ---
epath = Entry(root, fg="grey", font=("Segoe UI", 10))
epath.insert(0,"Enter REPOs local path...")
#epath.insert(0,r"C:\Users\4Raisan\Downloads\Animes")
epath.grid(columnspan=6, row=1, column=3, ipady=3, ipadx=65, pady=5, sticky='ew')

# Path Entry Accesss ---
def pathentryaccess(choise):
    if choise:
        epath.config(state='normal')
    else:
        epath.config(state='readonly')

# Path Entry Focus ---
def focusepath(event):
    epath.delete(0, END)
    epath.config(fg="black")

def nofocusepath(event):
     if epath.get() == "":
         epath.insert(0,"Enter REPOs local path...")
         epath.config(fg="gray")

epath.bind("<FocusIn>", focusepath)
epath.bind("<FocusOut>", nofocusepath)

#Z  PATH 1-Row---------------------------------------------------


# DONE
# Numbers 2-Row---------------------------------------------------
# Main Functions of Row 2
def plusone():
    global ecountvalue, ecount
    ecount.config(state='normal')
    ecountvalue+=1
    ecount.delete(0, END)
    ecount.insert(0,f"{ecountvalue}")
    ecount.grid(row=2, column=3, pady=5, sticky='w', ipady=3)
    ecount.config(state='disabled', disabledbackground='white', disabledforeground='black')
    
def minusone():
    global ecountvalue, ecount
    if ecountvalue>1:
        ecount.config(state='normal')
        ecountvalue-=1
        ecount.delete(0, END)
        ecount.insert(0, f"{ecountvalue}")
        ecount.config(state='disabled', disabledbackground='white', disabledforeground='black')

def clearepath():
    epath.delete(0, END)
    epath.grid(columnspan=6, row=1, column=3, ipady=3,ipadx=60, pady=5)

# Displaying
count = Label(root, text=" UNDOs : ")
count.grid(row=2, column=2)

def counter():
    global ecountvalue, ecount
    ecount = Entry(root, width=2, font=("Courier New", 11, 'bold'))
    ecountvalue = 1
    ecount.insert(0,f"{ecountvalue}")
    ecount.grid(row=2, column=3, pady=5, sticky='w', ipady=3, padx=1)
counter()
ecount.config(state='disabled', disabledbackground='white', disabledforeground='black')

ecountplus = Button(root, text=" + ", command=plusone, font=("arial", 11))
ecountplus.grid(columnspan=2, row=2, column=3)

ecountminus = Button(root, text=" - ", command=minusone, font=("arial", 11))
ecountminus.grid(columnspan=2, row=2, column=3, ipadx=2, sticky='e')

epathclear = Button(root, text="Clear Path", command=clearepath)
epathclear.grid(row=2, column=8)


#Z Numbers 2-Row---------------------------------------------------
# DONE


# DONE
# Instruction 3/4/5-Row---------------------------------------------------

instruction_avoid = Label(root, text="\nAvoid use, if your last commits have File Uploads !", fg='red')
instruction_avoid.grid(rowspan=2, columnspan=10, row=3, column=0)

instruction_redo = Label(root, text="... Remember their is no REDOs ...")
instruction_redo.grid(columnspan=10, row=5, column=0)

#Z Instruction 3/4/5-Row---------------------------------------------------
# DONE


# Check box 6-Row------------------------------------------------------
def checkflow():
    if check_vrbl.get()==1:
        passcheck()
        pathentryaccess(False)
    else:
        pathsign.destroy() 
        pathentryaccess(True) 
        undoDenied()    # Disable undo button 

# Variable to track checkbox state (1 = checked, 0 = unchecked) 
check_vrbl = IntVar()   # check_vrbl is an IntVar object - check_vrbl.get() 1/0
checkbox =  Checkbutton(root, text="Confirm and Check Details", variable=check_vrbl, command=checkflow)
checkbox.grid(columnspan=4, row=6, column=3)

#Z Check box 6-Row------------------------------------------------------


# Undo Row-7------------------------------------------------------

def undoDenied():  # Denied
    final0button = Button(root, text="> UNDO <", state=DISABLED)
    final0button.grid(columnspan=4, row=7, column=3, ipadx=10)

def undoapproved():  # Approved
    final1button  = Button(root, text="> UNDO <", bg='red', command=undo)
    final1button.grid(columnspan=4, row=7, column=3, ipadx=10)

undoDenied()

#Z Undo Row-7------------------------------------------------------


# MAIN FLOW and Validation

def passcheck():
    global direpath
    readypath = epath.get().replace('"','')
    direpath = os.path.isdir(readypath)
    if direpath:
        undoapproved()
        avblhistory()
        signgreen()
    else:
        signred()        
direpath = False

def undo():
    totcount(ecountvalue)   # Total UNDOs Update
    check_vrbl.set(0)   # Checkbox - Uncheck
    undoDenied()    # Disable undo button
    pathsign.destroy()  # Destroy the path Signs
    counter()   # Reset undo-counter
    pathentryaccess(True)


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
