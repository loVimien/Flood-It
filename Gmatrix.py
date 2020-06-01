from tkinter import StringVar, Label, font
from square import Square
from possibleColor import PossibleColor
from random import choice
from solve import *

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
        self._textFont = font.Font(family='Helvetica', size=10, weight='bold')
        self._textMoves = StringVar()
        self._labelMoves = Label(self._window, textvariable=self._textMoves, font=self._textFont)
        self._textWin = Label(self._window, text="Vous avez gagné", font=self._textFont)


        self.updateSet(self[(0, 0)])

        resoudre = Solve(self, self._currSet, self._moves)
        nbCoupsRand = resoudre.randSolve()
        nbCoupsGreed = resoudre.greedySolve()
        self._textMoves.set("Coups joués : 0,\n nombre de coups possible de manière aléatoire : {},\n nombre de coups possibles avec l'algorithme greedy {}".format(nbCoupsRand, nbCoupsGreed))
        print(f"Nombre de coups avec l'algorithme Greedy : {nbCoupsGreed}.")
        print(f"Nombre de coups en aléatoire : {nbCoupsRand}.")

    def display(self):
        self._labelMoves.grid(row = 0, column = 0, columnspan=8)
        for i in self._mat:
            for j in i:
                j.display()


    def __getitem__(self, coord):
        x, y = coord
        return self._mat[x][y].color

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

        for i in range(len(self._currSet)):
            self._currSet[i][0] = colorToUpdate


        # On applique le changement de couleur aux carrés présents dans la liste currSet

    def play(self, colorToUpdate):
        self.updateSet(colorToUpdate)
        self._moves += 1
        self._textMoves.set("Coups joués : {}".format(self._moves))
        self.updateGraphicMatrix()

        if self.isFill():
            self.win() # Quitte si on a gagné sinon renvoie faux


    def updateGraphicMatrix(self):
        for k in range(len(self._currSet)):
            currI = self._currSet[k][1]
            currJ = self._currSet[k][2]
            self._mat[currI][currJ].color = self._currSet[k][0]

    def isFill(self):
        if len(self._currSet) == len(self._mat) * len(self._mat[0]):
        # Si le nombre de carré de la nouvelle couleur est égal au nombre total alors toute la grille est remplie
        # Le Flood It est rempli d'une seule couleur
            return True
        else:
            return False

    def win(self):
        self.destroySquares()
        self._textWin.grid(row=1, column=0, columnspan=10)
        # print(len(self._currSet))

    def destroySquares(self):
        for i in self._mat:
            for j in i:
                j.destroy()

    def destroyAll(self):
        if self._textWin != None:
            self._textWin.destroy()
        self._labelMoves.destroy()
        self.destroySquares()
