from tkinter import *
from Gmatrix import GMatrix

def retry():
    global b
    global mat
    mat.destroyAll()
    mat = GMatrix(window, 10, 10, 50)

window = Tk()
window.title("Flood it")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
mat = GMatrix(window, 10, 10, 50)
b = Button(window, text="Recommencer", command=retry)
b.grid(row=0, column=5, columnspan=5)

window.mainloop()
