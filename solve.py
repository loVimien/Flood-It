from possibleColor import PossibleColor
import networkx as nx
from random import choice

class Solve:
    @staticmethod
    def saveMatrix(matrix):
        return matrix.mat.copy(), matrix.currSet.copy()

    @staticmethod
    def restoreMatrix(matrix, copy):
        matrix.mat = copy[0].copy()
        matrix.currSet = copy[1].copy()

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
            if len(matrix.currSet) > max:
                max = len(matrix.currSet)
                maxColor = color
            Solve.restoreMatrix(matrix, save)
        #print(maxColor, "greedy")
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
                        if len(matrix.currSet) > max:
                            max = len(matrix.currSet)
                            if max == len(matrix.mat) * len(matrix.mat[0]):
                                # Au dernier tour il ne faut regarder qu'avec 1 tour d'avance
                                Solve.restoreMatrix(matrix, save)
                                return Solve.greedyColor(matrix)
                            maxColor = color1
                        Solve.restoreMatrix(matrix, save)
        #print(f"maxColor : {maxColor} | max : {max} | isFill : {self._mat.isFill()} | len(currSet) : {len(self._mat._currSet)} | nbCarrés : {len(self._mat._mat) * len(self._mat._mat[0])}")
        #print(maxColor, "force")
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
    def model_graph(matrix):
        vertices = {}
        mat_rep = []
        for i in range(len(matrix.mat)):
            line = []
            for j in range(len(matrix.mat[i])):
                line.append([matrix[(i,j)], None])
            mat_rep.append(line)
        current_new_vertex = 0
        for i in range(len(mat_rep)):
            for j in range(len(mat_rep[i])):
                current_vertex = ""
                if mat_rep[i][j][1] == None:
                    vertices["v{}".format(current_new_vertex)] = [(i,j)]
                    mat_rep[i][j][1] = "v{}".format(current_new_vertex)
                    current_vertex = "v{}".format(current_new_vertex)
                    current_new_vertex += 1
                else:
                    current_vertex = mat_rep[i][j][1]
                if i-1 >= 0 and mat_rep[i][j][0] == mat_rep[i-1][j][0] and mat_rep[i-1][j][1] == None:
                    vertices[current_vertex].append((i-1,j))
                    mat_rep[i-1][j][1] = current_vertex
                if i+1 < len(mat_rep) and mat_rep[i][j][0] == mat_rep[i+1][j][0] and mat_rep[i+1][j][1] == None:
                    vertices[current_vertex].append((i+1,j))
                    mat_rep[i+1][j][1] = current_vertex
                if j-1 >= 0 and mat_rep[i][j][0] == mat_rep[i][j-1][0] and mat_rep[i][j-1][1] == None:
                    vertices[current_vertex].append((i,j-1))
                    mat_rep[i][j-1][1] = current_vertex
                if j+1 < len(mat_rep[i]) and mat_rep[i][j][0] == mat_rep[i][j+1][0] and mat_rep[i][j+1][1] == None:
                    vertices[current_vertex].append((i,j+1))
                    mat_rep[i][j+1][1] = current_vertex
        graph = nx.Graph()
        for i in vertices.keys():
            graph.add_node(i)
        for i in range(len(mat_rep)):
            for j in range(len(mat_rep[i])):
                if i-1 >= 0 and mat_rep[i][j][1] != mat_rep[i-1][j][1] and (mat_rep[i][j][1], mat_rep[i-1][j][1]) not in graph.edges() and (mat_rep[i-1][j][1], mat_rep[i][j][1]) not in graph.edges():
                    graph.add_edge(mat_rep[i][j][0], mat_rep[i-1][j][1])
                if i+1 < len(mat_rep) and mat_rep[i][j][1] != mat_rep[i+1][j][1] and (mat_rep[i][j][1], mat_rep[i+1][j][1]) not in graph.edges() and (mat_rep[i+1][j][1], mat_rep[i][j][1]) not in graph.edges():
                    graph.add_edge(mat_rep[i][j][1], mat_rep[i+1][j][1])
                if j-1 >= 0 and mat_rep[i][j][1] != mat_rep[i][j-1][1] and (mat_rep[i][j][1], mat_rep[i][j-1][1]) not in graph.edges() and (mat_rep[i][j-1][1], mat_rep[i][j][1]) not in graph.edges():
                    graph.add_edge(mat_rep[i][j][1], mat_rep[i][j-1][1])
                if j+1 < len(mat_rep[i]) and mat_rep[i][j][1] != mat_rep[i][j+1][1] and (mat_rep[i][j][1], mat_rep[i][j+1][1]) not in graph.edges() and (mat_rep[i][j+1][1], mat_rep[i][j][1]) not in graph.edges():
                    graph.add_edge(mat_rep[i][j][1], mat_rep[i][j+1][1])
        return graph, vertices

    def generate_dictionnary_graph(graph):
        d_graph = {}
        for i in graph.nodes():
            d_graph[i] = []
            for j in graph.neighbors(i):
                d_graph[i].append(j)
        return d_graph
    
    def number_of_vertices(graph):
        """Returns the number of vertices of the graph."""
        return len(graph.keys())
    
    def bfs(rgraph, r):
        """Makes the BFS of the graph from vertex r. Returns a tuple
        (parent, d, color)."""
        graph = Solve.generate_dictionnary_graph(rgraph)
        parent = {}
        d = {}
        color = {}
        for i in graph:
            if i != r:
                color[i] = 'b'
                parent[i] = None
                d[i] = Solve.number_of_vertices(graph) + 1
        f = []
        f.append(r)
        color[r] = 'g'
        d[r] = 0
        while len(f) != 0:
            u = f[0]
            for i in graph[u]:
                if color[i] == 'b':
                    color[i] = 'g'
                    d[i] = d[u] + 1
                    parent[i] = u
                    f.append(i)
            f.pop(0)
            color[u] = 'n'
        return (parent, d, color)
    
    def furthest_node(graph):
        bfs = Solve.bfs(graph, "v0")
        max = 0
        node = "v0"
        for i,j in bfs[1].items():
            node = i if j > max else node
            max = j if j > max else max
        return node
    
    def shortest_path_to_furthest_node(graph):
        return nx.shortest_path(graph, "v0", Solve.furthest_node(graph))
    
    def resolve_with_graph(matrix):
        graph, vertices = Solve.model_graph(matrix)
        path = Solve.shortest_path_to_furthest_node(graph)
        save = Solve.saveMatrix(matrix)
        moves = 0
        for i in path:
            matrix.updateSet(matrix[vertices[i][0]])
            moves += 1
        while not matrix.isFill():
            matrix.updateSet(Solve.greedyColor(matrix))
            moves += 1
        Solve.restoreMatrix(matrix, save)
        return moves