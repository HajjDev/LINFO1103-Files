from Tree import BinaryTree

def get_all_root_to_leaf_paths(tree: BinaryTree) -> list:
    """
    pre: tree est un BinaryTree
    post: retourne une liste de listes, chaque sous-liste représentant un chemin de la racine à une feuille
    """

# Exemple :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# get_all_root_to_leaf_paths(arbre) → [[1, 2, 4], [1, 3]]