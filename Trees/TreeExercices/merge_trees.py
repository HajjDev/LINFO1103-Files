from Tree import BinaryTree

def merge_trees(tree1: BinaryTree, tree2: BinaryTree) -> BinaryTree:
    """
    pre: tree1 et tree2 sont des BinaryTree
    post: retourne un nouvel arbre résultant de la fusion de tree1 et tree2,
          chaque nœud est la somme des valeurs correspondantes dans tree1 et tree2
    """

# Exemples :
# arbre1 = BinaryTree(1)
# arbre1.left().elem = 2
# arbre2 = BinaryTree(3)
# arbre2.right().elem = 4
# merged = merge_trees(arbre1, arbre2)
# preorder(merged) → [4, 2, 4]