from Tree import BinaryTree

def count_nodes_with_one_child(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds ayant exactement un seul enfant
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.left().left().elem = 3
# arbre.right().elem = 4
# count_nodes_with_one_child(arbre) → 1 (le nœud 2)