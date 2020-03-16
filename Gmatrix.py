from tkinter import StringVar, Label, font
from square import Square
from possibleColor import PossibleColor
from random import choice

class GMatrix:
    def __init__(self, master, nbLines, nbCols, sqDim):
        self._lines = nbLines
        self._colums = nbCols
        self._window = master
        self._mat = []
        for i in range(1, nbLines):
            line = []
            for j in range(nbCols):
                line.append(Square(choice(list(PossibleColor)), master, sqDim, i, j, self))
            self._mat.append(line)
        self._moves = 0
        self._currSet = [[self._mat[0][0].color, 0, 0]]
        
        self._textFont = font.Font(family='Helvetica', size=12, weight='bold')
        self._textMoves = StringVar()
        self._textMoves.set("Coups joués : 0")
        self._labelMoves = Label(self._window, textvariable=self._textMoves, font=self._textFont)
        self._labelMoves.grid(row = 0, column = 0, columnspan=5)

    def __getitem__(self, coord):
        x, y = coord
        return selt._gMat[x][y]
    
    def updateSet(self, colorToUpdate):
        i = 0
        while(i < len(self._currSet)):
            currI = self._currSet[i][1]
            currJ = self._currSet[i][2]
            currCol = self._currSet[i][0]

            # On ajoute à la liste des carrés à changer de couleur les carrés voisins de même couleur et non présents dans la liste
            if currI + 1 < len(self._mat) and self._mat[currI + 1][currJ].color == colorToUpdate and not([currCol, currI + 1, currJ] in self._currSet):
                self._currSet.append([currCol, currI + 1, currJ])
            if currI - 1 >= 0 and self._mat[currI - 1][currJ].color == colorToUpdate and not([currCol, currI - 1, currJ] in self._currSet):
                self._currSet.append([currCol, currI - 1, currJ])
            if currJ + 1 < len(self._mat[0]) and self._mat[currI][currJ + 1].color == colorToUpdate and not([currCol, currI, currJ + 1] in self._currSet):
                self._currSet.append([currCol, currI, currJ + 1])
            if currJ - 1 >= 0 and self._mat[currI][currJ - 1].color == colorToUpdate and not([currCol, currI, currJ - 1] in self._currSet):
                self._currSet.append([currCol, currI, currJ - 1])
            i += 1


        # On applique le changement de couleur aux carrés présents dans la liste currSet
        self._moves += 1
        self._textMoves.set("Coups joués : {}".format(self._moves))
        for i in range(len(self._currSet)):
            self._currSet[i][0] = colorToUpdate
        self.updateGraphicMatrix()

        self.win() # Quitte si on a gagné sinon renvoie faux

    def updateGraphicMatrix(self):
        for k in range(len(self._currSet)):
            currI = self._currSet[k][1]
            currJ = self._currSet[k][2]
            self._mat[currI][currJ].color = self._currSet[k][0]
    
    def win(self):
        if len(self._currSet) == len(self._mat) * len(self._mat[0]):
        # Si le nombre de carré de la nouvelle couleur est égal au nombre total alors toute la grille est remplie
        # Le Flood It est rempli d'une seule couleur
            self.destroySquares()
            winText = Label(self._window, text="Vous avez gagné", font=self._textFont)
            winText.grid(row=1, column=0, columnspan=10)
        return False
    def destroySquares(self):
        for i in self._mat:
            for j in i:
                j.destroy()
    def destroyAll(self):
        self._labelMoves.destroy()
        self.destroySquares()