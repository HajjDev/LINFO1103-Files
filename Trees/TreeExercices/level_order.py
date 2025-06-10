from Tree import BinaryTree

def level_order(tree: BinaryTree) -> list:
    """
    pre: tree est un BinaryTree
    post: retourne la liste des éléments parcourus en largeur (par niveau)
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# level_order(arbre) → [1, 2, 3]