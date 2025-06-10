from Tree import BinaryTree

def is_perfect_binary_tree(tree: BinaryTree) -> bool:
    """
    pre: tree est un BinaryTree
    post: retourne True si l’arbre est parfait (tous les niveaux sont complètement remplis),
          False sinon
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# arbre.left().right().elem = 5
# arbre.right().left().elem = 6
# arbre.right().right().elem = 7
# is_perfect_binary_tree(arbre) → True