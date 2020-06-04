from tkinter import StringVar, Label, font
from square import Square
from possibleColor import PossibleColor
from random import choice
from solve import *
import time
import networkx as nx

class GMatrix:
    def __init__(self, master, nbLines, nbCols, vertoffset, horizoffset, sqDim):
        self._lines = nbLines
        self._colums = nbCols
        self._window = master
        self._mat = []
        self._saveMat = []
        for i in range(vertoffset, nbLines+vertoffset):
            line = []
            lineSave = []
            for j in range(horizoffset, nbCols+horizoffset):
                color = choice(list(PossibleColor))
                lineSave.append(color)
                line.append(Square(color, master, sqDim, i, j, self))
            self._mat.append(line)
            self._saveMat.append(lineSave)
        self._moves = 0
        self._currSet = [[self._mat[0][0].color, 0, 0]]
        self._textFont = font.Font(family='Helvetica', size=10, weight='bold')
        self._textMoves = StringVar()
        self._labelMoves = Label(self._window, textvariable=self._textMoves, font=self._textFont)
        self._textWin = Label(self._window, text="Vous avez gagné", font=self._textFont)
        self._textPredic = None
        self._save = (self._mat.copy(), self._currSet.copy())


        self.updateSet(self[(0, 0)])
        self._saveSet = self._currSet.copy()

        self.solveFloodIt()


    def solveFloodIt(self):

        print("Génération et résolution de la grille ...\n" + 32 * "- ")

        begin = time.time()
        nbCoupsRand = Solve.solve(self, Solve.randomColor)
        print(f"Nombre de coups en aléatoire : {nbCoupsRand}.")
        print(f"Durée = {time.time() - begin} secondes.\n")

        begin = time.time()
        nbCoupsGreed = Solve.solve(self, Solve.greedyColor)
        print(f"Nombre de coups avec l'algorithme Greedy : {nbCoupsGreed}.")
        print(f"Durée = {time.time() - begin} secondes.\n")

        begin = time.time()
        nbCoupsGraph = Solve.resolve_with_graph(self)
        print("Nombre de coups avec la résolution par graphe : {}".format(nbCoupsGraph))
        print("Durée = {} secondes\n".format(time.time() - begin))

        begin = time.time()
        nbCoupsForce = Solve.solve(self, Solve.forceColor)
        print(f"Nombre de coups avec plusieurs tours de projection : {nbCoupsForce}.")
        print(f"Durée = {time.time() - begin} secondes.\n")

        self._textPredic = "nombre de coups possible de manière aléatoire : {},\n nombre de coups possibles avec l'algorithme greedy {},\n nombre de coups possibles avec la résolution par graphes {},\n nombre de coups possibles avec plusieurs tours de projection {}".format(nbCoupsRand, nbCoupsGreed, nbCoupsGraph, nbCoupsForce)
        self._textMoves.set("Coups joués : 0\n" + self._textPredic)

    def display(self, span):
        self._labelMoves.grid(row = 0, column = 0, columnspan=8, rowspan=span)
        for i in self._mat:
            for j in i:
                j.display()


    def __getitem__(self, coord):
        x, y = coord
        return self._mat[x][y].color

    def resetMatrix(self):
        self._currSet = self._saveSet.copy()
        self._moves = 0
        self._textWin.grid_forget()
        for i in range(len(self._mat)):
            for j in range(len(self._mat[i])):
                self._mat[i][j].color = self._saveMat[i][j]
                self._mat[i][j].display()
        self._textMoves.set("Coups joués : 0\n" + self._textPredic)

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
        self._textMoves.set("Coups joués : {}\n".format(self._moves) + self._textPredic)
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
        self.hideSquares()
        self._textWin.grid(row=self._mat[0][0].vert, column=0, columnspan=10)
        # print(len(self._currSet))

    def hideSquares(self):
        for i in self._mat:
            for j in i:
                j.grid_forget()

    def destroySquares(self):
        for i in self._mat:
            for j in i:
                j.destroy()

    def destroyAll(self):
        if self._textWin != None:
            self._textWin.destroy()
        self._labelMoves.destroy()
        self.destroySquares()

    def _get_mat(self):
        return self._mat

    def _set_mat(self, mat):
        self._mat = mat

    def _get_set(self):
        return self._currSet

    def _set_set(self, s):
        self._currSet = s

    mat = property(_get_mat, _set_mat)
    currSet = property(_get_set, _set_set)
