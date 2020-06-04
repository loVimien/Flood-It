# Flood-It

**Lilian HIAULT et Loïc VIMIEN**

Projet Prep'ISIMA 2 proposé par L. Yon.

* * *

## Informations

Voici une implémentation du Flood-It en Python 3 réalisé grâce à la bibliothèque graphique Tkinter.  
Cliquez sur une case pour changer de couleur et remplissez la grille d'une même couleur pour gagner. Le but est de remplir la grille en un nombre de coups minimums. Plusieurs indications sont données par ordre de difficulté :

-   aléatoire : nombre de coups en jouant aléatoirement
-   greedy : nombre de coups en maximisant le remplissage à chaque tour
-   graph : nombre de coups déterminé en calculant le chemin le plus court vers le noeud le plus difficile à atteindre (déterminé grâce à un graphe, l'algorithme BFS et l'algorithme de Dijkstra) puis en utilisant l'algorithme Greedy pour compléter les cases restantes
-   plusieurs tours de projection : nombre de coups en maximisant le remplissage sur plusieurs coups

## Bibliothèques utilisées

-   Tkinter : interface graphique
-   random : aléatoire
-   time : gestion du temps
-   enum : couleurs possibles
-   networkx : graphes

## À faire

-   [x] Programmer une interface graphique pour le jeu _Flood-It_
-   [x] Créer des heuristiques de résolution du jeu

## Contenu

-   `flood-it.py` : Éxécutable python, contient le code pour le bouton Recommencer, le bouton pour générer une nouvelle grille et la fenêtre principale. Invoque une GMatrix, regénérée à chaque appui sur Nouvelle grille et remise à zéro à chaque appui sur recommencer
-   `square.py` : Contient la classe Square (héritant de la classe Canvas de TKinter) : carrés contenant une couleur, connaissant leur matrice parent et leur position, joue un coup sur la matrice parent à l'évènement clic
-   `possibleColor.py` : Contient la classe PossibleColor qui est une énumération contenant toutes les couleurs possibles
-   `solve.py` : Contient la classe Solve (ne contient que des méthodes statiques) qui contient toutes les méthodes de résolution ainsi que toutes les méthodes nécessaires à leur fonctionnement
-   `Gmatrix.py` : Contient la classe GMatrix qui est une matrice de Squares, met à jour le plateau selon une couleur jouée, vérifie les conditions de victoire, affiche les éléments de manière graphique et peut les détruire (quand une grille est regénérée)
