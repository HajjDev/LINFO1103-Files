from Tree import BinaryTree

def are_levels_sum_equal(tree1: BinaryTree, tree2: BinaryTree) -> bool:
    """
    pre: tree1 et tree2 sont des BinaryTree
    post: retourne True si la somme des valeurs de chaque niveau est identique entre les deux arbres
    """

# Exemple :
# arbre1 = BinaryTree(1)
# arbre1.left().elem = 2
# arbre1.right().elem = 3
# arbre2 = BinaryTree(1)
# arbre2.left().elem = 3
# arbre2.right().elem = 2
# are_levels_sum_equal(arbre1, arbre2) → True