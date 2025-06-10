from Tree import BinaryTree

def has_root_to_leaf_path(tree: BinaryTree, path: list) -> bool:
    """
    pre: tree est un BinaryTree, path est une liste d'entiers
    post: retourne True si la séquence path correspond à un chemin de la racine à une feuille
    """

# Exemple :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.left().right().elem = 3
# has_root_to_leaf_path(arbre, [1, 2, 3]) → True
# has_root_to_leaf_path(arbre, [1, 3]) → False