from Tree import BinaryTree

def find_max_root_to_leaf_path_sum(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne la somme maximale des valeurs sur un chemin de la racine à une feuille,
          0 si arbre vide
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 10
# arbre.right().left().elem = 5
# find_max_root_to_leaf_path_sum(arbre) → 16 (1+10+5)