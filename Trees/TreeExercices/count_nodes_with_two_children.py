from Tree import BinaryTree

def count_nodes_with_two_children(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds avec exactement deux enfants
    """

# Exemple :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# count_nodes_with_two_children(arbre) → 1