from Tree import BinaryTree

def count_nodes_with_value_greater_than(tree: BinaryTree, threshold: int) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds avec une valeur strictement supérieure à threshold
    """

# Exemples :
# arbre = BinaryTree(5)
# arbre.left().elem = 10
# arbre.right().elem = 2
# count_nodes_with_value_greater_than(arbre, 4) → 2