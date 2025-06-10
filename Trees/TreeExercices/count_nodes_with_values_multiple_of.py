from Tree import BinaryTree

def count_nodes_with_value_multiple_of(tree: BinaryTree, k: int) -> int:
    """
    pre: tree est un BinaryTree, k > 0
    post: retourne le nombre de nœuds dont la valeur est un multiple de k
    """

# Exemple :
# arbre = BinaryTree(6)
# arbre.left().elem = 9
# arbre.right().elem = 12
# count_nodes_with_value_multiple_of(arbre, 3) → 3