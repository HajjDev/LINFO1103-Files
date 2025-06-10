from Tree import BinaryTree

def find_deepest_node(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree non vide
    post: retourne la valeur du nœud le plus profond dans l’arbre,
          en cas d’égalité retourne celui rencontré le plus à gauche
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.left().left().elem = 3
# find_deepest_node(arbre) → 3