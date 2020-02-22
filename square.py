from tkinter import *
from numpy.random import randint

class Square(Canvas):
    def __init__(self, master, t, posi, posj, matParent):
        self.possibleColor = ['Blue', 'Red', 'Yellow', 'Black']
        self.indCurrentColor = randint(0, len(self.possibleColor))
        super().__init__(master, width = t, height = t, background = self.possibleColor[self.indCurrentColor])
        self.line = posi
        self.column = posj
        self.mat = matParent
        self.bind('<Button-1>', self.onMouse)
        self.grid(row = self.line, column = self.column)
    def onMouse(self, event):
        self.mat.mat.updateMatrix(self.indCurrentColor)
    def getColorIndex(self):
        return self.indCurrentColor
    def setColor(self, ind):
        if(ind != self.indCurrentColor):
            self.indCurrentColor = ind
            self.configure(background = self.possibleColor[ind])