from Tree import BinaryTree

def are_trees_identical(tree1: BinaryTree, tree2: BinaryTree) -> bool:
    """
    pre: `tree1` et `tree2` sont des instances de la classe BinaryTree
    post: retourne True si les deux arbres sont identiques, c’est-à-dire :
          - même structure (organisation des nœuds)
          - mêmes valeurs dans les mêmes positions
          retourne False sinon
    """

# Exemples d'utilisation de la fonction are_trees_identical :

# arbre1 = BinaryTree(1)
# arbre1.left().elem = 2
# arbre1.right().elem = 3

# arbre2 = BinaryTree(1)
# arbre2.left().elem = 2
# arbre2.right().elem = 3

# are_trees_identical(arbre1, arbre2) → True

# arbre3 = BinaryTree(1)
# arbre3.left().elem = 2

# are_trees_identical(arbre1, arbre3) → False

# arbre_vide1 = BinaryTree()
# arbre_vide2 = BinaryTree()
# are_trees_identical(arbre_vide1, arbre_vide2) → True
