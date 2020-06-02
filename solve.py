from possibleColor import PossibleColor

from random import choice


class Solve:
    def __init__(self, matrix, currSet, moves):
        self._mat = matrix  # Matrice des couleurs et leur position
        self._moves = moves  # nombre de coups

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
        maxColor = choice(list(PossibleColor))
        # Sauvegarde de la matrice
        saveMat = self._mat._mat.copy()
        saveCurrSet = self._mat._currSet.copy()
        saveMoves = self._moves
        for color in list(PossibleColor):
            self._mat.updateSet(color)
            if len(self._mat._currSet) > max:
                max = len(self._mat._currSet)
                maxColor = color
            self._mat._mat = saveMat.copy()
            self._mat._currSet = saveCurrSet.copy()
            self._moves = saveMoves
        return maxColor

    def forceColor(self):
        """Renvoie la couleur qui maximise le remplissage sur 4 tours"""
        max = 0
        maxColor = choice(list(PossibleColor))
        # Sauvegarde de la matrice
        saveMat = self._mat._mat.copy()
        saveCurrSet = self._mat._currSet.copy()
        saveMoves = self._moves
        for color1 in list(PossibleColor):
            for color2 in list(PossibleColor):
                for color3 in list(PossibleColor):
                    for color4 in list(PossibleColor):
                        self._mat.updateSet(color1)
                        self._mat.updateSet(color2)
                        self._mat.updateSet(color3)
                        if len(self._mat._currSet) > max:
                            max = len(self._mat._currSet)
                            if max == len(self._mat._mat) * len(self._mat._mat[0]):
                                # Au dernier tour il ne faut regarder qu'avec 1 tour d'avance
                                return self.greedyColor()
                            maxColor = color1
                        self._mat._mat = saveMat.copy()
                        self._mat._currSet = saveCurrSet.copy()
                        self._moves = saveMoves
        # print(f"maxColor : {maxColor} | max : {max} | isFill : {self._mat.isFill()} | len(currSet) : {len(self._mat._currSet)} | nbCarrés : {len(self._mat._mat) * len(self._mat._mat[0])}")
        return maxColor


    def solve(self, funColor):
        """Retourne le nombre de coups nécessaires pour remplir le flood-it étant donné une fonction funColor de choix de la couleur."""
        self.saveMatrix()
        while not self._mat.isFill():
            self._mat.updateSet(funColor())
            self._moves += 1
        # On remet tout dans la situation initiale pour pouvoir utiliser d'autres algorithmes de résolution
        nbMoves = self._moves
        self.restoreMatrix()
        return nbMoves
