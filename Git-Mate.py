from tkinter import *
root = Tk()
from subprocess import *

# Disable resizing (both horizontally and vertically)
root.resizable(False, False)

# PATH - input
path = Label(root, text="PATH")
path.grid(row=0 ,column=0)

ep = Entry()
ep.insert(0,"")
ep.grid(row=0, column=1)


# RUN - CMD
# > cd "C:\Users\4Raisan\Desktop\GitHub\Git-Mate"

# Count - input commit count


# RUN - CMD HEAD
# > git reset --hard HEAD~1

# UPDATE Total count + Refresh GUI


# Done - Confirm
# > git push origin main --force


# Additionals

# 1. Commit History
# > git log --oneline

# 2. Branch Check
# > git status


root.mainloop() # ending