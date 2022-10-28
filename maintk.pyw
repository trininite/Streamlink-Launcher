
import tkinter as tk
import subprocess as simp


class App:
    def __init__(self, root):
        
        self.customVar = tk.StringVar()

        self.root = root
        mainFrame = tk.Frame(root)

        self.forsen = tk.Button(mainFrame, text="forsen", command=lambda:self.runSubroutine("forsen"))
        self.xqc = tk.Button(mainFrame, text="xqc",command=lambda:self.runSubroutine("xqc") )
        self.poke = tk.Button(mainFrame, text="pokelawls",command=lambda:self.runSubroutine("poke") )
        self.nymn = tk.Button(mainFrame, text="nymn", command=lambda:self.runSubroutine("nymn"))
        self.custom = tk.Button(mainFrame, text="Custom", command=self.customInput)
        
        mainFrame.grid(row=0, column=0)

        inputs = (self.forsen, self.xqc, self.poke, self.nymn, self.custom)
        self.updateLayout(inputs)

    def customInput(self):
        self.top = tk.Toplevel(self.root)

        self.topFrame = tk.Frame(self.top)
        self.topFrame.configure(background='#222222')
        
        self.userIn = tk.Entry(self.topFrame, textvariable=self.customVar, bg="#333333", fg="#ffffff", insertbackground="#ffffff")
        
        self.enter = tk.Button(self.topFrame, text="Enter", bg="#333333", fg="#ffffff", command=lambda:self.runSubroutine(self.customVar.get()))


        self.topFrame.grid(row=0, column=0)
        self.userIn.grid(row=0, column=0)
        self.enter.grid(row=0, column=1)



    def runSubroutine(self, inn):
        try:
            self.top.destroy()
        except:
            pass
        cmdline = ["streamlinkLauncher.bat", inn]
        simp.Popen(cmdline, cwd="./")
        quit()

    def updateLayout(self, inputs):
        col = 0
        for i in inputs:
            i.config(background="#222222", fg="#ffffff", padx=5, pady=5)
            i.grid(row=0, column=col)
            col = col + 1

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()