#!/usr/bin/python3
# -*-coding:utf-8 -*

from tkinter import *
from Gmatrix import GMatrix

window = Tk()
window.title("Flood it")
window.iconbitmap("icon.ico")
M = GMatrix(window, 10, 10, 50)

window.mainloop()
