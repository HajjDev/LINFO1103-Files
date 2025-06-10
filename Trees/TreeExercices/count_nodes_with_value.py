from Tree import BinaryTree

def count_nodes_with_value(tree: BinaryTree, value: int) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds contenant la valeur donnée
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 1
# arbre.right().elem = 2
# count_nodes_with_value(arbre, 1) → 2