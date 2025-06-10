from Tree import BinaryTree

def has_path_sum(tree: BinaryTree, target_sum: int) -> bool:
    """
    pre: tree est un BinaryTree
    post: retourne True s’il existe un chemin racine-feuille dont la somme des valeurs est égale à target_sum,
          False sinon
    """

# Exemples :
# arbre = BinaryTree(5)
# arbre.left().elem = 4
# arbre.right().elem = 8
# arbre.left().left().elem = 11
# has_path_sum(arbre, 20) → True (5+4+11)