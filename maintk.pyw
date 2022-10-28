from tkinter import *
import subprocess as simp


def runSubroutine(input):
    cmdline = ["streamlinkLauncher.bat", input]
    simp.Popen(cmdline, cwd="./")
    quit()


root = Tk()

mainFrame = Frame(root)


forsen = Button(
    mainFrame, 
    text="forsen", 
    padx=5, pady=5, 
    command = \
    lambda:runSubroutine("forsen")
    )

xqc = Button(
    mainFrame, 
    text="xqc", 
    padx=5, 
    pady=5, 
    bg="#333333",
    fg="#ffffff",
    command = \
    lambda:runSubroutine("xqc")
    )

poke = Button(
    mainFrame, 
    text="pokelawls", 
    padx=5, 
    pady=5, 
    command = \
    lambda:runSubroutine("pokelawls")
    )

nymn = Button(
    mainFrame, 
    text="nymn", 
    padx=5, 
    pady=5, 
    command = \
    lambda:runSubroutine("nymn")
    )


mainFrame.pack()

forsen.grid(row = 0, column = 0)
xqc.grid(row=0, column=1)
poke.grid(row=0, column=2)
nymn.grid(row=0, column=3)


inputs = (forsen, xqc, poke, nymn)

for i in inputs:
    i.config(background="#222222", fg="#ffffff")


root.mainloop()