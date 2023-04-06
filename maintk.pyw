import tkinter as tk
import subprocess as simp
import os
from sys import platform
import json


class App:
    def __init__(self, root):

        root.title("Streamlink Launcher")
        
        self.custom_var = tk.StringVar()

        cache_list = self.get_cache()
        self.net_cache_ms = cache_list[0]
        self.file_cache_ms = cache_list[1]
        del(cache_list)


        self.OS = self.get_os()

        self.root = root

        mainFrame = tk.Frame(root)

        streamers = self.get_streamers()

        streamer_buttons = []
        for i in range(len(streamers)):
            button = tk.Button(
                mainFrame,
                text=streamers[i], 
                command=lambda:self.sub_routine(streamers[i])
            )
            streamer_buttons.append(button)

        #for some reason, the button takes the last streamer in the config as its command argument
        #these lines re-assign the command value and it seems to work (fingers crossed)
        tmp_int = 0
        for streamer in streamer_buttons:
            streamer.configure(command=lambda:self.sub_routine(streamers[tmp_int]))
        del(tmp_int)
            
        self.custom = tk.Button(
            mainFrame, 
            text="Custom", 
            command=self.custom_input
        )

        mainFrame.grid(row=0, column=0)

        inputs = streamer_buttons + [self.custom]
        self.update_layout(inputs)


    def get_os(self):
        if platform == "linux" or platform == "linux2":
            return "linux"
        elif platform == "win32":
            return "win"


    def get_cache(self):
        config = json.load(open("conf.json"))
        
        return [config["net_cache_ms"], config["file_cache_ms"]]


    def get_streamers(self):
        config = json.load(open("conf.json"))

        streamers = []
        for i in range(len(config["streamers"][0].split(","))):
            streamers.append(config["streamers"][0].split(",")[i].split(" ")[0])
        
        return streamers


    def custom_input(self):
        self.top = tk.Toplevel(self.root)

        self.top.title("Custom Input")

        self.topFrame = tk.Frame(self.top)
        self.topFrame.configure(background='#222222')
        
        self.userIn = tk.Entry(
            self.topFrame, 
            textvariable=self.custom_var, 
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
            command=lambda:self.sub_routine_input(self.custom_var.get())
        )


        self.topFrame.grid(row=0, column=0)
        self.userIn.grid(row=0, column=0)
        self.enter.grid(row=0, column=1)
        

    def sub_routine(self, sub_routine_input):
        if self.OS == "linux":
            try:
                self.top.destroy()
                self.top2.destroy()
            except:
                pass
            bashScriptPath = os.getcwd() + '/' + 'streamlinkLauncher.sh'
            cmdline = [bashScriptPath, sub_routine_input, str(self.file_cache_ms), str(self.net_cache_ms)]
            simp.Popen(cmdline, cwd="./")

        elif self.OS == "win":
            try:
                self.top.destroy()
                self.top2.destroy()
            except:
                pass
            cmdline = ["streamlinkLauncher.bat", sub_routine_input, str(self.file_cache_ms), str(self.net_cache_ms)]
            simp.Popen(cmdline, cwd="./")
            quit()


    def update_layout(self, widgets):
        for i in range(len(widgets)):
            widgets[i].config(background="#222222", fg="#ffffff", padx=5, pady=5)
            widgets[i].grid(row=0, column=i, sticky="NS")


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


main() if __name__ == "__main__" else None