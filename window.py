import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Window(tk.Frame):
    def __init__(self, master:tk, title:str, size:str):
        self.master = master
        super().__init__(self.master)
        self.pack()
        self.file_name = tk.StringVar(master=self.master,value="未選択")
        self.result = tk.StringVar(value="結果")

        self.master.geometry(size)
        self.master.title(title)
    
    def createLabel(self, master, text:tk.StringVar):
        label = tk.Label(textvariable=text, font=('', 12))
        label.pack(pady=10)

    def analys(self, files):
        print(str(self.file_name))

    def openfile(self):
        self.file_name.set(filedialog.askopenfilename(title="音声ファイル", filetypes=[("Audio file", " .wav .mp3 ")], multiple="true"))
        self.analys(self.file_name)

    def createOpenFileButton(self, master):
        button = tk.Button(master, text='ファイルを開く',
                        font=('', 16),
                        bg='#999999', 
                        command=self.openfile,
                        activebackground="#aaaaaa",
                        )
        button.pack(pady=40)


    def loop(self, master):
        self.master.mainloop()

    def callBack(self):
        pass
