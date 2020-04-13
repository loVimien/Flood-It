from possibleColor import PossibleColor
# from Gmatrix import updateSet

from random import choice


class Solve:
    def __init__(self, matrix, currSet):
        self._mat = matrix.copy() # Matrice des couleurs et leur position
        self._currSet = currSet.copy()
        self._moves = 0


    def randomColor(self):
        """Choisis une couleur aléatoire"""
        return choice(list(PossibleColor))

    def updateMat(self, colorToUpdate):
        """Résoud le jeu et retoune le nombre de coups"""
        i = 0
        while(i < len(self._currSet)):
            currI = self._currSet[i][1]
            currJ = self._currSet[i][2]
            currCol = self._currSet[i][0]

            if currI + 1 < len(self._mat) and self._mat[currI + 1][currJ].color == colorToUpdate and not([currCol, currI + 1, currJ] in self._currSet):
                self._currSet.append([currCol, currI + 1, currJ])
            if currI - 1 >= 0 and self._mat[currI - 1][currJ].color == colorToUpdate and not([currCol, currI - 1, currJ] in self._currSet):
                self._currSet.append([currCol, currI - 1, currJ])
            if currJ + 1 < len(self._mat[0]) and self._mat[currI][currJ + 1].color == colorToUpdate and not([currCol, currI, currJ + 1] in self._currSet):
                self._currSet.append([currCol, currI, currJ + 1])
            if currJ - 1 >= 0 and self._mat[currI][currJ - 1].color == colorToUpdate and not([currCol, currI, currJ - 1] in self._currSet):
                self._currSet.append([currCol, currI, currJ - 1])
            i += 1
        self._moves += 1
        for i in range(len(self._currSet)):
            self._currSet[i][0] = colorToUpdate


    def isFill(self):
        if len(self._currSet) == len(self._mat) * len(self._mat[0]):
        # Si le nombre de carré de la nouvelle couleur est égal au nombre total alors toute la grille est remplie
        # Le Flood It est rempli d'une seule couleur
            return True
        else:
            return False


    def solveMat(self):
        while not self.isFill():
            self.updateMat(self.randomColor())
        return self._moves
