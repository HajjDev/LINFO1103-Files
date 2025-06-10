from Tree import BinaryTree

def sum_nodes_at_level(tree: BinaryTree, level: int) -> int:
    """
    pre: tree est un BinaryTree, level >= 0
    post: retourne la somme des valeurs des nœuds situés au niveau spécifié
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# sum_nodes_at_level(arbre, 1) → 5