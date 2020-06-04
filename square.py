from tkinter import *
from possibleColor import PossibleColor


class Square(Canvas):
    def __init__(self, color, master, t, posi, posj, matParent):
        self._currentColor = color
        super().__init__(master, width=t, height=t, background=self._currentColor.name)
        self._mat = matParent
        self.bind('<Button-1>', self.onMouse)
        self._i = posi
        self._j = posj

    def onMouse(self, event):
        self._mat.play(self._currentColor)

    def display(self):
        self.grid(row=self._i, column=self._j)

    def _set_Color(self, color):
        if(color != self._currentColor):
            self._currentColor = color
            self.configure(background=self._currentColor.name)

    def _get_Color(self):
        return self._currentColor

    def _get_horiz_pos(self):
        return self._j

    def _get_vert_pos(self):
        return self._i

    color = property(_get_Color, _set_Color)
    horiz = property(_get_horiz_pos)
    vert = property(_get_vert_pos)
