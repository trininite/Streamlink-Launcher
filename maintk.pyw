from tkinter import *
import subprocess as simp


class App:
    def __init__(self, root):

        mainFrame = Frame(root)

        self.forsen = Button(mainFrame, text="forsen", command=lambda:self.runSubroutine("forsen"))
        self.xqc = Button(mainFrame, text="xqc",command=lambda:self.runSubroutine("xqc") )
        self.poke = Button(mainFrame, text="pokelawls",command=lambda:self.runSubroutine("poke") )
        self.nymn = Button(mainFrame, text="nymn", command=lambda:self.runSubroutine("nymn"))
        
        mainFrame.pack()
        self.updateLayout()

    def runSubroutine(self, inn):
        cmdline = ["streamlinkLauncher.bat", inn]
        simp.Popen(cmdline, cwd="./")
        quit()

    def updateLayout(self):
        inputs = (self.forsen, self.xqc, self.poke, self.nymn)
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

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()