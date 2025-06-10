from Tree import BinaryTree

def sum_left_leaves(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne la somme des valeurs des feuilles qui sont des fils gauche
    """

# Exemple :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.left().left().elem = 4
# arbre.right().elem = 3
# sum_left_leaves(arbre) → 4