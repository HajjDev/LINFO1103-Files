from Tree import BinaryTree

def average_leaf_depth(tree: BinaryTree) -> float:
    """
    pre: tree est un BinaryTree
    post: retourne la moyenne des profondeurs des feuilles, 0 si arbre vide
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.left().left().elem = 3
# average_leaf_depth(arbre) → 1.5