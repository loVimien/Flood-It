from tkinter import *
from numpy.random import randint

class Square(Canvas):
    def __init__(self, master, t, posi, posj, matParent):
        self._possibleColor = ['Blue', 'Red', 'Yellow', 'Black', 'Purple', 'Green']
        self._indCurrentColor = randint(0, len(self.possibleColor))
        super().__init__(master, width = t, height = t, background = self.possibleColor[self.indCurrentColor])
        self._mat = matParent
        self.bind('<Button-1>', self.onMouse)
        self.grid(row = posi, column = posj)
    def onMouse(self, event):
        self.mat.mat.updateMatrix(self.indCurrentColor)
    def _set_Color(self, ind):
        if(ind != self._indCurrentColor):
            self._indCurrentColor = ind
            self.configure(background = self._possibleColor[ind])
    def _get_Color(self):
        return self._indCurrentColor
    def _get_PossibleColor(self):
        return self._possibleColor
    def _get_ParentMatrix(self):
        return self._mat
    indCurrentColor = property(_get_Color, _set_Color)
    possibleColor = property(_get_PossibleColor)
    mat = property(_get_ParentMatrix)