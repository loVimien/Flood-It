# Flood-It

**Lilian HIAULT et Loïc VIMIEN**

Projet Prep'ISIMA 2 proposé par L. Yon.

---

## Informations

Nous allons programmer en Python 3 en utilisant la bibliothèque graphique Tkinter.

## À faire

- [x] Programmer une interface graphique pour le jeu *Flood-It*
- [ ] Créer des heuristiques de résolution du jeu

## Contenu

- flood-it.py : Éxécutable python, contient le code pour le bouton Recommencer et la fenêtre principale. Invoque une GMatrix, regénérée à chaque appui sur recommencer
- square.py : Contient la classe Square (héritant de la classe Canvas de TKinter) : carrés contenant une couleur, connaissant leur matrice parent et leur position, joue un coup sur la matrice parent à l'évènement clic
- possibleColor.py : Énumération contenant toutes les couleurs possibles
- solve.py : Contient la classe Solve qui contient une référence vers une matrice et ayant comme méthodes les différents algorithmes de résolution
- Gmatrix.py : Contient la classe GMatrix qui est une matrice de Squares, met à jour le plateau selon une couleur jouée, vérifie les conditions de victoire, affiche les éléments de manière graphique et peut les détruire (quand une grille est regénérée)