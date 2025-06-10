from Tree import BinaryTree

def min_height(tree: BinaryTree) -> int:
    """
    pre: `tree` est une instance de la classe BinaryTree
    post: retourne la hauteur minimale de `tree`, c’est-à-dire la longueur du plus court chemin
          de la racine jusqu’à une feuille ; retourne -1 si l’arbre est vide
    """

# Exemples d'utilisation de la fonction min_height avec la classe BinaryTree :

# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# min_height(arbre) → 1

# arbre2 = BinaryTree(10)
# min_height(arbre2) → 0

# arbre_vide = BinaryTree()
# min_height(arbre_vide) → -1

# arbre3 = BinaryTree(5)
# arbre3.left().elem = 7
# arbre3.left().left().elem = 8
# arbre3.left().left().left().elem = 9
# min_height(arbre3) → 3
