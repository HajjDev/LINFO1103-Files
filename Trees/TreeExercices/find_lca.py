from Tree import BinaryTree

def find_lca(tree: BinaryTree, val1: int, val2: int) -> int:
    """
    pre: tree est un BinaryTree, val1 et val2 sont présents dans tree
    post: retourne la valeur du plus bas ancêtre commun (LCA) des deux nœuds val1 et val2
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# find_lca(arbre, 4, 3) → 1
# find_lca(arbre, 4, 2) → 2