from Tree import BinaryTree

def sum_values(tree: BinaryTree) -> int:
    """
    pre: `tree` est une instance de la classe BinaryTree, contenant des entiers
    post: retourne la somme de toutes les valeurs stockées dans les nœuds de `tree` ;
          retourne 0 si l’arbre est vide
    """

# Exemples d'utilisation de la fonction sum_values avec la classe BinaryTree :

# arbre = BinaryTree(10)
# arbre.left().elem = 5
# arbre.right().elem = 15
# sum_values(arbre) → 30

# arbre_vide = BinaryTree()
# sum_values(arbre_vide) → 0

# arbre2 = BinaryTree(1)
# arbre2.left().elem = 2
# arbre2.left().left().elem = 3
# sum_values(arbre2) → 6
