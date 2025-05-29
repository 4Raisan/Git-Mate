from tkinter import *
root = Tk()
from subprocess import *

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

ep = Entry()
ep.insert(0,"")
ep.grid(columnspan=2, row=1, column=1)


# RUN - CMD
# > cd "C:\Users\4Raisan\Desktop\GitHub\Git-Mate"

# Count - input commit count
count = Label(root, text="UNDO : ")
count.grid(row=2, column=0)

ec = Entry()
ec.insert(0,"")
ec.grid(columnspan=2, row=2, column=1)

# RUN - CMD HEAD
# > git reset --hard HEAD~1

# UPDATE Total count + Refresh GUI
def totcount():
    global refreshCount
    refreshCount = 8
    scnt = Label(root, text=f"Undos: {refreshCount}")
    scnt.grid(row=0, column=2)


# Done - Confirm
# > git push origin main --force
Ctype = Label(root, text="Enter 'C' for confirm\nRemember their is no REDOs")
Ctype.grid(row=3, column=1)
CButton = Button(root, text="Confirm", command=totcount)
CButton.grid(columnspan=4, row=3, column=0)


# Additionals


# 1. Commit History
# > git log --oneline

# 2. Branch Check
# > git status

root.mainloop() # ending
