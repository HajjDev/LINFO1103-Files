from Tree import BinaryTree

def max_width(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne la largeur maximale (nombre maximal de nœuds sur un même niveau)
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# max_width(arbre) → 2