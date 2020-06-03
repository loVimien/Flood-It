from Gmatrix import GMatrix
import os

def main():
    def new_grid():
        global b
        global mat
        mat.destroyAll()
        mat = GMatrix(window, 10, 10, 2, 0, 50)
        mat.display(2)

    def reset():
        global mat
        mat.resetMatrix()

    window = Tk()
    window.title("Flood it")
    icon = PhotoImage(file='icon.png')
    window.iconphoto(True, icon)
    mat = GMatrix(window, 10, 10, 2, 0, 50)
    mat.display(2)
    b_new = Button(window, text="Nouvelle grille", command=new_grid)
    b_reset = Button(window, text="Recommencer", command=reset)
    b_new.grid(row=0, column=8, columnspan=2)
    b_reset.grid(row=1, column=8, columnspan=2)

    window.mainloop()

if __name__ == "__main__":
    except:
        print("Installing networkx")
        try:
            os.system("python -m pip install networkx")
        except:
            print("Error with pip. Install pip, check your installation or check your connection")
            quit()
    try:
        from tkinter import *
    except:
        print("Installing tkinter")
        try:
            os.system("python -m pip install tkinter")
        except:
            print("Error with pip. Install pip, check your installation or check your connection")
            quit()
    try:
        import networkx
    main()
    
    