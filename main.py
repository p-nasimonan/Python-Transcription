"""
# 実行スクリプト
GUIで音声ファイルを入れて文字起こし、できれば人を分けたい
"""
import tkinter as tk
from tkinter import ttk
from window import Window

if __name__ == '__main__':
    root = tk.Tk()
    App = Window(master=root, title="文字起こし", size="300x400")
    App.createOpenFileButton(master=root)
    App.createLabel(master=root, text=App.file_name_tk)
    App.createLabel(master=root,text=App.result)
    App.loop(master=root)