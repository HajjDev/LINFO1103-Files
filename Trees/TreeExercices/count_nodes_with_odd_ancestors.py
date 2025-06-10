from Tree import BinaryTree

def count_nodes_with_odd_ancestors(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds qui ont un nombre impair d’ancêtres (profondeur impaire)
    """

# Exemple :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# count_nodes_with_odd_ancestors(arbre) → 2 (nœuds 2 et 4)