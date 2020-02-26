from tkinter import *
from Gmatrix import GMatrix

window = Tk()
window.title("Flood it")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
GMatrix(window, 10, 10, 50)

window.mainloop()
