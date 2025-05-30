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

epath = Entry()
epath.insert(0,"")
epath.grid(columnspan=2, row=1, column=1)


# RUN - CMD
# > cd "C:\Users\4Raisan\Desktop\GitHub\Git-Mate"

# Count - input commit count
count = Label(root, text="UNDO : ")
count.grid(row=2, column=0)

ecount = Entry()
ecount.insert(0,"")
ecount.grid(columnspan=2, row=2, column=1)

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
Ctype.grid(rowspan=2, row=3, column=1)

econfirm = Entry()
econfirm.insert(0,"")
econfirm.grid(columnspan=3, row=5, column=0)

CButton = Button(root, text="Confirm", command=totcount)
CButton.grid(columnspan=3, row=6, column=0)


# Additionals


# 1. Commit History
# > git log --oneline

# 2. Branch Check
# > git status

root.mainloop() # ending
