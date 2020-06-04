mat = None

def main():
    def new_grid():
        global mat
        mat.destroyAll()
        mat = GMatrix(window, 10, 10, 2, 0, 50)
        mat.display(2)

    def reset():
        global mat
        mat.resetMatrix()

    global mat
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
    try:
        import networkx
    except ImportError:
        print("The library networkx isn't installed. Please install it with pip install networkx")
        quit()
    try:
        from tkinter import *
    except ImportError:
        print("The library tkinter isn't installed. Please install it with pip install tkinter")
    from Gmatrix import GMatrix
    main()
