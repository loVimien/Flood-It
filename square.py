from tkinter import *
from possibleColor import PossibleColor


class Square(Canvas):
    def __init__(self, color, master, t, posi, posj, matParent):
        self._currentColor = color # Couleur courante du carré
        super().__init__(master, width=t, height=t, background=self._currentColor.name) # Appel au constructeur de la classe Canvas (super classe)
        self._mat = matParent # Matrice parent du carré
        self.bind('<Button-1>', self.onMouse)
        self._i = posi # Position verticale du carré
        self._j = posj # Position horizontale du carré

    def onMouse(self, event):
        """ Fonction évènementielle appelée lors d'un clic sur le carré. Joue un coup en utilisant la couleur du carré courant """
        self._mat.play(self._currentColor)

    def display(self):
        """ Affiche le carré """
        self.grid(row=self._i, column=self._j)

    def _set_Color(self, color):
        """ Setter de l'attribut _currentColor. Met également la couleur à jour au niveau graphique """
        if(color != self._currentColor):
            self._currentColor = color
            self.configure(background=self._currentColor.name)

    def _get_Color(self):
        """ Getter de l'attribut __currentColor """
        return self._currentColor

    def _get_horiz_pos(self):
        """ Getter de l'attribut _j (position horizontale du carré) """
        return self._j

    def _get_vert_pos(self):
        """ Setter de l'attribut _i (position verticale du carré) """
        return self._i

    # Propriétés associant les différents getters et setters
    color = property(_get_Color, _set_Color)
    horiz = property(_get_horiz_pos)
    vert = property(_get_vert_pos)
