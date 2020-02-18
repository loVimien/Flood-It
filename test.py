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
        self.mat.updateEns(self.possibleColor[self.indCurrentColor])
        self.mat.updateEnsColor(self.possibleColor[self.indCurrentColor])
    def getNeighbour(self):
        neigh = []
        if(self.line+1 < self.mat.lines) :
            neigh.append(self.mat.mat[self.line+1][self.column])
        if(self.line-1 >= 0) :
            neigh.append(self.mat.mat[self.line-1][self.column])
        if(self.column+1 < self.mat.colums) :
            neigh.append(self.mat.mat[self.line][self.column+1])
        if(self.column-1 >= 0) :
            neigh.append(self.mat.mat[self.line][self.column-1])
        return neigh

class Matrix:
    def __init__(self, master, nbLines, nbCols, sqDim):
        self.lines = nbLines
        self.colums = nbCols
        self.mat = []
        for i in range(nbLines):
            line = []
            for j in range(nbCols):
                line.append(Square(master, sqDim, i, j, self))
            self.mat.append(line)
        self.inEns = []
        self.inEns.append(self.mat[0][0])
        self.updateEns(self.inEns[0].possibleColor[self.inEns[0].indCurrentColor])
    def updateEns(self, color):
        i = 0
        while(i < len(self.inEns)):
            neigh = self.inEns[i].getNeighbour()
            for j in range(len(neigh)):
                if(neigh[j].possibleColor[neigh[j].indCurrentColor] == color and not(neigh[j] in self.inEns)):
                    self.inEns.append(neigh[j])
            i += 1
    def updateEnsColor(self, color):
        for i in self.inEns:
            i.indCurrentColor = i.possibleColor.index(color)
            i.configure(background = color)



window = Tk()
M = Matrix(window, 15, 15, 50)

window.mainloop()