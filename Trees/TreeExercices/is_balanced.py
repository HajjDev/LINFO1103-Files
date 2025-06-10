from Tree import BinaryTree 

def is_balanced(tree: BinaryTree) -> bool:
    """
    pre: tree est un BinaryTree
    post: retourne True si l’arbre est équilibré (différence de hauteur ≤ 1 entre sous-arbres gauche et droit),
          False sinon
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# is_balanced(arbre) → True
# arbre.left().left().elem = 4
# arbre.left().left().left().elem = 5
# is_balanced(arbre) → False