from possibleColor import PossibleColor
import networkx as nx
from random import choice


class Solve:
    @staticmethod
    def _saveMatrix(matrix):
        """Fais une sauvegarde de la matrice"""
        return matrix.currSet.copy()

    @staticmethod
    def _restoreMatrix(matrix, copy):
        """Restaure une matrice sauvegardée"""
        matrix.currSet = copy.copy()

    @staticmethod
    def randomColor(matrix=None):
        """Renvoie une couleur aléatoire"""
        return choice(list(PossibleColor))

    @staticmethod
    def greedyColor(matrix):
        """Renvoie la couleur qui maximise le remplissage"""
        max = 0
        maxColor = choice(list(PossibleColor))
        # Sauvegarde du set
        save = Solve._saveMatrix(matrix)
        for color in list(PossibleColor):
            matrix.updateSet(color)
            if len(matrix.currSet) > max:
                max = len(matrix.currSet)
                maxColor = color
            Solve._restoreMatrix(matrix, save)
        return maxColor

    @staticmethod
    def forceColor(matrix):
        """Renvoie la couleur qui maximise le remplissage sur 4 tours"""
        max = 0
        maxColor = choice(list(PossibleColor))
        # Sauvegarde du set
        save = Solve._saveMatrix(matrix)
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
                                Solve._restoreMatrix(matrix, save)
                                return Solve.greedyColor(matrix)
                            maxColor = color1
                        Solve._restoreMatrix(matrix, save)
        return maxColor

    @staticmethod
    def solve(matrix, funColor):
        """Retourne le nombre de coups nécessaires pour remplir le flood-it étant donné une fonction funColor de choix de la couleur."""
        save = Solve._saveMatrix(matrix)
        moves = 0
        while not matrix.isFill():
            matrix.updateSet(funColor(matrix))
            moves += 1
        # On remet tout dans la situation initiale pour pouvoir utiliser d'autres algorithmes de résolution
        Solve._restoreMatrix(matrix, save)
        return moves

    @staticmethod
    def _model_graph(matrix):
        """Retourne une modélisation du Flood It sous forme de graphe"""
        vertices = {}
        mat_rep = []
        # Génération d'une matrice contenant la couleur de chaque case ainsi que le sommet du graphe auquels elles sont associées (None par défaut)
        for i in range(len(matrix.mat)):
            line = []
            for j in range(len(matrix.mat[i])):
                line.append([matrix[(i, j)], None])
            mat_rep.append(line)
        current_new_vertex = 0
        # Génération des sommets (dictionnaire contenant comme clés chaque sommet et comme valeurs les listes de chaque case de la matrice qui y sont associé)
        for i in range(len(mat_rep)):
            for j in range(len(mat_rep[i])):
                current_vertex = ""
                if mat_rep[i][j][1] == None:
                    vertices["v{}".format(current_new_vertex)] = [(i, j)]
                    mat_rep[i][j][1] = "v{}".format(current_new_vertex)
                    current_vertex = "v{}".format(current_new_vertex)
                    current_new_vertex += 1
                else:
                    current_vertex = mat_rep[i][j][1]
                if i - 1 >= 0 and mat_rep[i][j][0] == mat_rep[i - 1][j][0] and mat_rep[i - 1][j][1] == None:
                    vertices[current_vertex].append((i - 1, j))
                    mat_rep[i - 1][j][1] = current_vertex
                if i + 1 < len(mat_rep) and mat_rep[i][j][0] == mat_rep[i + 1][j][0] and mat_rep[i + 1][j][1] == None:
                    vertices[current_vertex].append((i + 1, j))
                    mat_rep[i + 1][j][1] = current_vertex
                if j - 1 >= 0 and mat_rep[i][j][0] == mat_rep[i][j - 1][0] and mat_rep[i][j - 1][1] == None:
                    vertices[current_vertex].append((i, j - 1))
                    mat_rep[i][j - 1][1] = current_vertex
                if j + 1 < len(mat_rep[i]) and mat_rep[i][j][0] == mat_rep[i][j + 1][0] and mat_rep[i][j + 1][1] == None:
                    vertices[current_vertex].append((i, j + 1))
                    mat_rep[i][j + 1][1] = current_vertex
        graph = nx.Graph()
        for i in vertices.keys():
            graph.add_node(i)
        # Génération des arrêtes (ajout de chaque arrête dans le graphe networkx)
        for i in range(len(mat_rep)):
            for j in range(len(mat_rep[i])):
                if i - 1 >= 0 and mat_rep[i][j][1] != mat_rep[i - 1][j][1] and (mat_rep[i][j][1], mat_rep[i - 1][j][1]) not in graph.edges() and (mat_rep[i - 1][j][1], mat_rep[i][j][1]) not in graph.edges():
                    graph.add_edge(mat_rep[i][j][0], mat_rep[i - 1][j][1])
                if i + 1 < len(mat_rep) and mat_rep[i][j][1] != mat_rep[i + 1][j][1] and (mat_rep[i][j][1], mat_rep[i + 1][j][1]) not in graph.edges() and (mat_rep[i + 1][j][1], mat_rep[i][j][1]) not in graph.edges():
                    graph.add_edge(mat_rep[i][j][1], mat_rep[i + 1][j][1])
                if j - 1 >= 0 and mat_rep[i][j][1] != mat_rep[i][j - 1][1] and (mat_rep[i][j][1], mat_rep[i][j - 1][1]) not in graph.edges() and (mat_rep[i][j - 1][1], mat_rep[i][j][1]) not in graph.edges():
                    graph.add_edge(mat_rep[i][j][1], mat_rep[i][j - 1][1])
                if j + 1 < len(mat_rep[i]) and mat_rep[i][j][1] != mat_rep[i][j + 1][1] and (mat_rep[i][j][1], mat_rep[i][j + 1][1]) not in graph.edges() and (mat_rep[i][j + 1][1], mat_rep[i][j][1]) not in graph.edges():
                    graph.add_edge(mat_rep[i][j][1], mat_rep[i][j + 1][1])
        return graph, vertices

    @staticmethod
    def _generate_dictionnary_graph(graph):
        """ Génère un graphe sous forme de dictionnaire dont les clés sont les différents sommets du graphes 
        et les valeurs sont les listes de tous les voisins à partir d'un graphe networkx """
        d_graph = {}
        for i in graph.nodes():
            d_graph[i] = []
            for j in graph.neighbors(i):
                d_graph[i].append(j)
        return d_graph

    @staticmethod
    def _number_of_vertices(graph):
        """Returns the number of vertices of the graph."""
        return len(graph.keys())

    @staticmethod
    def _bfs(rgraph, r):
        """Génère le BFS d'un graphe à partir du sommet r. Retourne le tuple
        (parent, d, color)."""
        graph = Solve._generate_dictionnary_graph(rgraph)
        parent = {}
        d = {}
        color = {}
        for i in graph:
            if i != r:
                color[i] = 'b'
                parent[i] = None
                d[i] = Solve._number_of_vertices(graph) + 1
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

    @staticmethod
    def _furthest_node(graph):
        """Renvoie le noeud le plus éloigné (noeud dont la distance BFS par rapport au noeud v0 (qui contient la case supérieurs gauche de la matrice)"""
        bfs = Solve._bfs(graph, "v0")
        max = 0
        node = "v0"
        for i, j in bfs[1].items():
            node = i if j > max else node
            max = j if j > max else max
        return node

    @staticmethod
    def _shortest_path_to_furthest_node(graph):
        """Renvoie le chemin vers le noeud le plus éloigné"""
        return nx.shortest_path(graph, "v0", Solve._furthest_node(graph))

    @staticmethod
    def resolve_with_graph(matrix):
        """Renvoie le nombre de coups requis pour résoudre le Flood It à l'aide du graphe en rejoignant d'abord la zone la plus éloignée puis en finissant par un algorithme greedy"""
        graph, vertices = Solve._model_graph(matrix)
        path = Solve._shortest_path_to_furthest_node(graph)
        save = Solve._saveMatrix(matrix)
        moves = 0
        for i in path:
            matrix.updateSet(matrix[vertices[i][0]])
            moves += 1
        while not matrix.isFill():
            matrix.updateSet(Solve.greedyColor(matrix))
            moves += 1
        Solve._restoreMatrix(matrix, save)
        return moves
