#!/usr/bin/python3
# -*-coding:utf-8 -*

from tkinter import *
from Gmatrix import GMatrix

window = Tk()
window.title("Flood it")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
M = GMatrix(window, 10, 10, 50)

window.mainloop()
