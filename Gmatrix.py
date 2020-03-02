from square import Square


class Matrix:
    def __init__(self, square_list):
        self.graphicMat = square_list
        self.mat = []
        for i in range(len(square_list)):
            line = []
            for j in range(len(square_list[i])):
                line.append(square_list[i][j].indCurrentColor)
            self.mat.append(line)

		# couleur = currSet[abscisse][ordonnée]est la liste des carrés de même couleur voisins
        self.currSet = [[self.mat[0][0], 0, 0]]
        self.updateMatrix(self.mat[0][0])

    def updateMatrix(self, colorToUpdate):
        i = 0
        while(i < len(self.currSet)):
            currI = self.currSet[i][1]
            currJ = self.currSet[i][2]
            currCol = self.currSet[i][0]

			# On ajoute à la liste des carrés à changer de couleur les carrés voisins de même couleur et non présents dans la liste
            if currI + 1 < len(self.mat) and self.mat[currI + 1][currJ] == colorToUpdate and not([currCol, currI + 1, currJ] in self.currSet):
                self.currSet.append([currCol, currI + 1, currJ])
            if currI - 1 >= 0 and self.mat[currI - 1][currJ] == colorToUpdate and not([currCol, currI - 1, currJ] in self.currSet):
                self.currSet.append([currCol, currI - 1, currJ])
            if currJ + 1 < len(self.mat[0]) and self.mat[currI][currJ + 1] == colorToUpdate and not([currCol, currI, currJ + 1] in self.currSet):
                self.currSet.append([currCol, currI, currJ + 1])
            if currJ - 1 >= 0 and self.mat[currI][currJ - 1] == colorToUpdate and not([currCol, currI, currJ - 1] in self.currSet):
                self.currSet.append([currCol, currI, currJ - 1])
            i += 1

		# On applique le changmeent de couleur aux carrés présents dans la liste currSet
        for i in range(len(self.currSet)):
            self.currSet[i][0] = colorToUpdate
        self.updateGraphicMatrix()

    def updateGraphicMatrix(self):
        for k in range(len(self.currSet)):
            currI = self.currSet[k][1]
            currJ = self.currSet[k][2]
            self.graphicMat[currI][currJ].indCurrentColor = self.currSet[k][0]


class GMatrix:
    def __init__(self, master, nbLines, nbCols, sqDim):
        self.lines = nbLines
        self.colums = nbCols
        self.gMat = []
        for i in range(nbLines):
            line = []
            for j in range(nbCols):
                line.append(Square(master, sqDim, i, j, self))
            self.gMat.append(line)
        self._mat = Matrix(self.gMat)

    def _get_Mat(self):
        return self._mat

    mat = property(_get_Mat)
