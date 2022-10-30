import tkinter as tk
import subprocess as simp


class App:
    def __init__(self, root):

        root.title("Streamlink Launcher")
        
        self.customVar = tk.StringVar()
        self.netCacheMS = tk.StringVar()
        self.fileCacheMS = tk.StringVar()

        settingsIconDark = tk.PhotoImage(file = "settingsDarkmode.png")

        self.root = root
        mainFrame = tk.Frame(root)

        self.forsen = tk.Button(
            mainFrame, text="forsen", 
            command=lambda:self.runSubroutine("forsen")
        )

        self.xqc = tk.Button(
            mainFrame, 
            text="xqc", 
            command=lambda:self.runSubroutine("xqc")
        )
    
        self.poke = tk.Button(
            mainFrame, 
            text="pokelawls",
            command=lambda:self.runSubroutine("poke")
        )

        self.nymn = tk.Button(
            mainFrame, 
            text="nymn", 
            command=lambda:self.runSubroutine("nymn")
        )
            
        self.custom = tk.Button(
            mainFrame, 
            text="Custom", 
            command=self.customInput
        )

        self.settingsB = tk.Button(
            mainFrame, 
            image=settingsIconDark,
            command=self.settings
        )
        self.settingsB.photo = settingsIconDark
        
        mainFrame.grid(row=0, column=0)

        inputs = (self.forsen, self.xqc, self.poke, self.nymn, self.custom, self.settingsB)
        self.updateLayout(inputs)

    def customInput(self):
        self.top = tk.Toplevel(self.root)

        self.top.title("Custom Input")

        self.topFrame = tk.Frame(self.top)
        self.topFrame.configure(background='#222222')
        
        self.userIn = tk.Entry(
            self.topFrame, 
            textvariable=self.customVar, 
            bg="#333333", 
            fg="#ffffff", 
            insertbackground="#ffffff", 
            width=30
        )
        
        self.enter = tk.Button(
            self.topFrame, 
            text="Enter", 
            bg="#333333", 
            fg="#ffffff", 
            command=lambda:self.runSubroutine(self.customVar.get())
        )


        self.topFrame.grid(row=0, column=0)
        self.userIn.grid(row=0, column=0)
        self.enter.grid(row=0, column=1)
 
        

    def settings(self):
        self.top2 = tk.Toplevel(self.root)

        self.topFrame2 = tk.Frame(self.top2)
        self.topFrame2.configure(background="#222222")

        self.netCacheLabel = tk.Label(
            self.topFrame2,
            text="Network Cache",
            bg="#333333",
            fg="#ffffff",
            padx=2,
            relief=tk.SUNKEN
        )

        self.netCacheEntry = tk.Entry(
            self.topFrame2, 
            textvariable=self.netCacheMS, 
            bg="#333333", 
            fg="#ffffff", 
            insertbackground="#ffffff", 
            width=30
        )

        self.fileCacheLabel = tk.Label(
            self.topFrame2,
            text="Local Cache",
            bg="#333333",
            fg="#ffffff",
            relief=tk.SUNKEN
        )

        self.fileCacheEntry = tk.Entry(
            self.topFrame2, 
            textvariable=self.fileCacheMS, 
            bg="#333333", 
            fg="#ffffff", 
            insertbackground="#ffffff", 
            width=30
        )


        self.netCacheLabel.grid(row=0, column=0)
        self.netCacheEntry.grid(row=0, column=1)
        self.fileCacheLabel.grid(row=1, column=0, sticky="EW")
        self.fileCacheEntry.grid(row=1, column=1)

        self.topFrame2.grid(row=0, column=0)

        

    def runSubroutine(self, inn):
        try:
            self.top.destroy()
        except:
            pass
        cmdline = ["streamlinkLauncher.bat", inn, str(self.fileCacheMS.get()), str(self.netCacheMS.get())]
        simp.Popen(cmdline, cwd="./")
        quit()

    def updateLayout(self, inputs):
        col = 0
        for i in inputs:
            i.config(background="#222222", fg="#ffffff", padx=5, pady=5)
            i.grid(row=0, column=col, sticky="NS")
            col = col + 1

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()



if __name__ == "__main__":
    main()