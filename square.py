from tkinter import *
from random import choice
from possibleColor import PossibleColor

class Square(Canvas):
    def __init__(self, color, master, t, posi, posj, matParent):
        self._currentColor = color
        super().__init__(master, width = t, height = t, background = self._currentColor.name)
        self._mat = matParent
        self.bind('<Button-1>', self.onMouse)
        self.grid(row = posi, column = posj)
    def onMouse(self, event):
        self._mat.updateSet(self._currentColor)
    def _set_Color(self, color):
        if(color != self._currentColor):
            self._currentColor = color
            self.configure(background = self._currentColor.name)
    def _get_Color(self):
        return self._currentColor
    color = property(_get_Color, _set_Color)