from Tree import BinaryTree

def count_single_child_nodes(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds ayant exactement un enfant
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.left().left().elem = 3
# count_single_child_nodes(arbre) → 2