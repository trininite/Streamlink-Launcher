from tkinter import *
import subprocess as simp

def runSubroutine(input):
    cmdline = ["streamlinkLauncher.bat", input]
    simp.Popen(cmdline, cwd="./")

root = Tk()
mainFrame = Frame(root)

forsen = Button(mainFrame, text="forsen", command=lambda:runSubroutine("nymn"))
xqc = Button(mainFrame, text="xqc",command=lambda:runSubroutine("nymn") )
poke = Button(mainFrame, text="pokelawls",command=lambda:runSubroutine("nymn") )
nymn = Button(mainFrame, text="nymn", command=lambda:runSubroutine("nymn"))

mainFrame.pack()

inputs = (forsen, xqc, poke, nymn)

col = 0
for i in inputs:
    i.config(
        background="#222222", 
        fg="#ffffff", 
        padx=5, 
        pady=5
    )
    i.grid(row=0, column=col)
    col = col + 1


root.mainloop()