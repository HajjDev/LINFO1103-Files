from Tree import BinaryTree

def contains(tree: BinaryTree, value: int) -> bool:
    """
    pre: `tree` est une instance de la classe BinaryTree, `value` est un entier
    post: retourne True si `value` est présent dans au moins un nœud de `tree`, False sinon
    """

# Exemples d'utilisation de la fonction contains avec la classe BinaryTree :

# arbre = BinaryTree(8)
# arbre.left().elem = 3
# arbre.right().elem = 10
# contains(arbre, 10) → True
# contains(arbre, 4) → False

# arbre_vide = BinaryTree()
# contains(arbre_vide, 1) → False

# arbre2 = BinaryTree(5)
# arbre2.left().elem = 2
# arbre2.right().elem = 9
# arbre2.left().right().elem = 3
# contains(arbre2, 3) → True
