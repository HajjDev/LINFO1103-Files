from Tree import BinaryTree

def is_full_binary_tree(tree: BinaryTree) -> bool:
    """
    pre: tree est un BinaryTree
    post: retourne True si l’arbre est un arbre binaire complet (chaque nœud a 0 ou 2 enfants),
          False sinon
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# is_full_binary_tree(arbre) → True
# arbre.left().left().elem = 4
# is_full_binary_tree(arbre) → False