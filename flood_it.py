mat = None # Variable globale qui contiendra l'objet GMatrix courant
nbLines = 10 # Nombre de ligne de la grille à créer
nbColumns = 10 # Nombre de colonnes de la grille à créer
squareDim = 50 # Dimension des carrés à créer

def main():
    def new_grid():
        """ Fonction appelée lors d'un clic sur le bouton Nouvelle grille. Détruit la grille courante et en regénère une nouvelle """
        global mat
        global nbLines
        global nbColumns
        global squareDim
        mat.destroyAll()
        mat = GMatrix(window, nbLines, nbColumns, 2, 0, squareDim)
        mat.display(2)

    def reset():
        """ Fonction appelée lors d'un clic sur le bouton Recommencer. Appelle la fonction resetMatrix pour remettre la grille courante à sont état initial """
        global mat
        mat.resetMatrix()

    global mat
    global nbLines
    global nbColumns
    global squareDim
    window = Tk() # Fenêtre principale Tkinter
    window.title("Flood it") # Titre de la fenêtre
    icon = PhotoImage(file='icon.png') # Icone de la fenêtre
    window.iconphoto(True, icon)
    mat = GMatrix(window, nbLines, nbColumns, 2, 0, squareDim)
    mat.display(2)
    b_new = Button(window, text="Nouvelle grille", command=new_grid) # Bouton Nouvelle grille
    b_reset = Button(window, text="Recommencer", command=reset) # Bouton Recommencer (recommencer la grille courante)
    b_new.grid(row=0, column=int(0.8*nbColumns), columnspan=2)
    b_reset.grid(row=1, column=int(0.8*nbColumns), columnspan=2)

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
