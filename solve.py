from possibleColor import PossibleColor
# from Gmatrix import updateSet

from random import choice


class Solve:
    def __init__(self, matrix, currSet, moves):
        self._mat = matrix # Matrice des couleurs et leur position
        self._moves = moves # nombre de coups

        self.saveMat = self._mat._mat.copy()
        self.saveCurrSet = self._mat._currSet.copy()
        self.saveMoves = moves


    def saveMatrix(self):
        self.saveMat = self._mat._mat.copy()
        self.saveCurrSet = self._mat._currSet.copy()
        self.saveMoves = self._moves

    def restoreMatrix(self):
        self._mat._mat = self.saveMat
        self._mat._currSet = self.saveCurrSet
        self._moves = self.saveMoves

    def randomColor(self):
        """Renvoie une couleur aléatoire"""
        return choice(list(PossibleColor))

    def greedyColor(self):
        """Renvoie la couleur qui maximise le remplissage"""
        max = 0
        saveMat = self._mat._mat.copy()
        saveCurrSet = self._mat._currSet.copy()
        saveMoves = self._moves
        maxColor = choice(list(PossibleColor))
        for color in list(PossibleColor):
            self._mat.updateSet(color)
            if len(self._mat._currSet) > max:
                max = len(self._mat._currSet)
                maxColor = color
            self._mat._mat = saveMat.copy()
            self._mat._currSet = saveCurrSet.copy()
            self._moves = saveMoves
        return maxColor

    def randSolve(self):
        """Méthode de résolution aléatoire"""
        self.saveMatrix()
        while not self._mat.isFill():
            self._mat.updateSet(self.randomColor())
            self._moves += 1
        # On remet tout dans la situation initiale pour pouvoir utiliser d'autres algorithmes de résolution
        nbMoves = self._moves
        self.restoreMatrix()
        return nbMoves

    def greedySolve(self):
        """Méthode de résolution où à chaque tour, on colore un maximum de cases"""
        self.saveMatrix()
        while not self._mat.isFill():
            self._mat.updateSet(self.greedyColor())
            self._moves += 1
        # On remet tout dans la situation initiale pour pouvoir utiliser d'autres algorithmes de résolution
        nbMoves = self._moves
        self.restoreMatrix()
        return nbMoves
