from Tree import BinaryTree

def count_prime_nodes(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds dont la valeur est un nombre premier
    """

# Exemple :
# arbre = BinaryTree(7)
# arbre.left().elem = 4
# arbre.right().elem = 3
# count_prime_nodes(arbre) → 2