from Tree import BinaryTree

def mirror_tree(tree: BinaryTree) -> BinaryTree:
    """
    pre: tree est un BinaryTree
    post: retourne un nouvel arbre miroir de tree, sans modifier l’arbre original
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# mirrored = mirror_tree(arbre)
# preorder(mirrored) → [1, 3, 2]