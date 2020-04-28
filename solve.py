from possibleColor import PossibleColor
# from Gmatrix import updateSet

from random import choice


class Solve:
    def __init__(self, matrix, currSet, moves):
        self._mat = matrix.copy() # Matrice des couleurs et leur position
        self._currSet = currSet.copy() # liste des couleurs à mettre à jour
        self._moves = moves # nombre de coups

        self.saveMat = matrix.copy()
        self.saveCurrSet = currSet.copy()
        self.saveMoves = moves


    def saveMatrix(self):
        self.saveMat = self._mat.copy()
        self.saveCurrSet = self._currSet.copy()
        self.saveMoves = self._moves


    def restoreMatrix(self):
        self._mat = self.saveMat
        self._currSet = self.saveCurrSet
        self._moves = self.saveMoves


    def randomColor(self):
        """Renvoie une couleur aléatoire"""
        return choice(list(PossibleColor))


    def greedyColor(self):
        """Renvoie la couleur qui maximise le remplissage"""
        max = 0 # Nombre maximum de cases remplies
        saveMat = self._mat.copy()
        saveCurrSet = self._currSet.copy()
        saveMoves = self._moves
        maxColor = choice(list(PossibleColor))
        for color in list(PossibleColor):
            self.updateMat(color)
            if len(self._currSet) > max:
                max = len(self._currSet)
                maxColor = color
            self._mat = saveMat.copy()
            self._currSet = saveCurrSet.copy()
            self._moves = saveMoves
        # print(maxColor)
        return maxColor


    def updateMat(self, colorToUpdate):
        """Met à jour ma matrice en fonction d'une couleur choisie"""
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
        """Renvoie un booléen : vrai si le Flood-it est rempli d'une seule couleur, faux sinon"""
        if len(self._currSet) == len(self._mat) * len(self._mat[0]):
        # Si le nombre de carré de la nouvelle couleur est égal au nombre total alors toute la grille est remplie
        # Le Flood It est rempli d'une seule couleur
            return True
        else:
            return False


    def randSolve(self):
        """Méthode de résolution aléatoire"""
        self.saveMatrix()
        while not self.isFill():
            self.updateMat(self.randomColor())
        # On remet tout dans la situation initiale pour pouvoir utiliser d'autres algorithmes de résolution
        nbMoves = self._moves
        self.restoreMatrix()
        return nbMoves


    def greedySolve(self):
        """Méthode de résolution où à chaque tour, on colore un maximum de cases"""
        self.saveMatrix()
        while not self.isFill():
            self.updateMat(self.greedyColor())
        # On remet tout dans la situation initiale pour pouvoir utiliser d'autres algorithmes de résolution
        nbMoves = self._moves
        self.restoreMatrix()
        return nbMoves
