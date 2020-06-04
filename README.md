# Flood-It

**Lilian HIAULT et Loïc VIMIEN**

Projet Prep'ISIMA 2 proposé par L. Yon.

* * *

## Informations

Voici une implémentation du Flood-It en Python 3 réalisé grâce à la bibliothèque graphique Tkinter.  
Cliquez sur une case pour changer de couleur et remplissez la grille d'une même couleur pour gagner. Le but est de remplir la grille en un nombre de coups minimums. Plusieurs indications de nombre de coups sont données grâce à différentes méthodes de résolution :

-   aléatoire
-   graphe
-   greedy
-   plusieurs tours de projections

## Algorithmes de résolution du Flood-It utilisés :

La fonction `solve(matrix, funColor)` joue tour par tour tant que la grille n'est pas remplie d'une seule couleur. Elle joue sur la matrice les coups dont la couleur est donnée par la fonction funColor (randomColor(), greedyColor() ou forceColor()).

-   **aléatoire** : à chaque tour une couleur est choisie aléatoirement parmis les couleurs possibles.
-   **greedy** : joue à chaque tour la couleur qui maximise le remplissage. Pour chaque couleur possible on joue le coup et on garde la couleur pour laquelle la taille de la liste des carrés de la vague est le plus grand. Si plusieurs couleurs maximplissage on la choisit dans l'ordre comme présent dans `possibleColor.py`
-   **plusieurs tours de projection** : nombre de coups en maximisant le remplissage sur plusieurs coups. On teste chaque combinaison de 4 couleurs possibles puis on retourne la 1ère couleur pour laquelle le remplissage est maximum dans 4 tours. Une exception est faîte lorsque la grille est remplie au bout de 4 tours, on utilise l'algorithme greedy pour les derniers tours.
-   **graph** : cette méthode n'est pas utilisée dans `solve`. Elle donne le nombre de coups déterminé en calculant le chemin le plus court vers le noeud le plus éloigné (déterminé grâce à un graphe, l'algorithme BFS pour le plus éloigné puis l'algorithme de Dijkstra pour trouver un chemin optimal) puis en utilisant l'algorithme Greedy pour compléter les cases restantes. Nous utilisons plusieurs modélisations de graphes une première grâce à la bibliothèque networkx. La seconde est un dictionnaire dont les clés sont les sommets et valeurs sont les listes de ses voisins. L'algorithme BFS est utilisé avec la seconde méthode alors que l'algorithme de Dijkstra fonctionne avec la 1ère. Nous utilisons une fonction pour passer d'une modélisation à une autre.

## Bibliothèques utilisées

-   _Tkinter_ : interface graphique ([documentation](https://docs.python.org/3/library/tkinter.html))
-   _random_ : aléatoire ([documentation](https://docs.python.org/3/library/random.html))
-   _time_ : gestion du temps ([documentation](https://docs.python.org/3/library/time.html))
-   _enum_ : couleurs possibles ([documentation](https://docs.python.org/3/library/enum.html))
-   _networkx_ : graphes ([documentation](https://networkx.github.io/documentation/stable/index.html))

## À faire

-   [x] Programmer une interface graphique pour le jeu _Flood-It_
-   [x] Créer des heuristiques de résolution du jeu

## Liste des fichiers

-   `flood-it.py` : Éxécutable python, contient le code pour le bouton Recommencer, le bouton pour générer une nouvelle grille et la fenêtre principale. Invoque une GMatrix, regénérée à chaque appui sur Nouvelle grille et remise à zéro à chaque appui sur recommencer
-   `square.py` : Contient la classe Square (héritant de la classe Canvas de TKinter) : carrés contenant une couleur, connaissant leur matrice parent et leur position, joue un coup sur la matrice parent à l'évènement clic
-   `possibleColor.py` : Contient la classe PossibleColor qui est une énumération contenant toutes les couleurs possibles
-   `solve.py` : Contient la classe Solve (ne contient que des méthodes statiques) qui contient toutes les méthodes de résolution ainsi que toutes les méthodes nécessaires à leur fonctionnement
-   `Gmatrix.py` : Contient la classe GMatrix qui est une matrice de Squares, met à jour le plateau selon une couleur jouée, vérifie les conditions de victoire, affiche les éléments de manière graphique et peut les détruire (quand une grille est regénérée)
