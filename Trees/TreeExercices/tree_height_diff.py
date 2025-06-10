from Tree import BinaryTree

def tree_height_diff(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne la différence entre la hauteur maximale et minimale parmi tous les chemins racine-feuille
    """

# Exemple :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# arbre.left().left().left().elem = 5
# tree_height_diff(arbre) → 2