from possibleColor import PossibleColor

from random import choice


class Solve:
    @staticmethod
    def saveMatrix(matrix):
        return matrix._mat.copy(), matrix._currSet.copy()

    @staticmethod
    def restoreMatrix(matrix, copy):
        matrix._mat = copy[0].copy()
        matrix._currSet = copy[1].copy()

    @staticmethod
    def randomColor(matrix=None):
        """Renvoie une couleur aléatoire"""
        return choice(list(PossibleColor))

    @staticmethod
    def greedyColor(matrix):
        """Renvoie la couleur qui maximise le remplissage"""
        max = 0
        maxColor = choice(list(PossibleColor))
        # Sauvegarde de la matrice
        save = Solve.saveMatrix(matrix)
        for color in list(PossibleColor):
            matrix.updateSet(color)
            if len(matrix._currSet) > max:
                max = len(matrix._currSet)
                maxColor = color
            Solve.restoreMatrix(matrix, save)
        print(maxColor, "greedy")
        return maxColor

    @staticmethod
    def forceColor(matrix):
        """Renvoie la couleur qui maximise le remplissage sur 4 tours"""
        max = 0
        maxColor = choice(list(PossibleColor))
        # Sauvegarde de la matrice
        save = Solve.saveMatrix(matrix)
        for color1 in list(PossibleColor):
            for color2 in list(PossibleColor):
                for color3 in list(PossibleColor):
                    for color4 in list(PossibleColor):
                        matrix.updateSet(color1)
                        matrix.updateSet(color2)
                        matrix.updateSet(color3)
                        matrix.updateSet(color4)
                        if len(matrix._currSet) > max:
                            max = len(matrix._currSet)
                            if max == len(matrix._mat) * len(matrix._mat[0]):
                                # Au dernier tour il ne faut regarder qu'avec 1 tour d'avance
                                Solve.restoreMatrix(matrix, save)
                                return Solve.greedyColor(matrix)
                            maxColor = color1
                        Solve.restoreMatrix(matrix, save)
        #print(f"maxColor : {maxColor} | max : {max} | isFill : {self._mat.isFill()} | len(currSet) : {len(self._mat._currSet)} | nbCarrés : {len(self._mat._mat) * len(self._mat._mat[0])}")
        print(maxColor, "force")
        return maxColor

    @staticmethod
    def solve(matrix, funColor):
        """Retourne le nombre de coups nécessaires pour remplir le flood-it étant donné une fonction funColor de choix de la couleur."""
        save = Solve.saveMatrix(matrix)
        moves = 0
        while not matrix.isFill():
                matrix.updateSet(funColor(matrix))
                moves += 1
        # On remet tout dans la situation initiale pour pouvoir utiliser d'autres algorithmes de résolution
        Solve.restoreMatrix(matrix, save)
        return moves