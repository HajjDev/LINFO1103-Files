from Tree import BinaryTree

def has_duplicate_values(tree: BinaryTree) -> bool:
    """
    pre: tree est un BinaryTree
    post: retourne True si l’arbre contient au moins une valeur répétée, False sinon
    """

# Exemple :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 1
# has_duplicate_values(arbre) → True