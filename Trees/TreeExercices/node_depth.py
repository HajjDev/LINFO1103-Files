from Tree import BinaryTree

def node_depth(tree: BinaryTree, value: int) -> int:
    """
    pre: `tree` est une instance de la classe BinaryTree, `value` est un entier
    post: retourne la profondeur du premier nœud contenant `value` dans `tree`
          - la racine a une profondeur de 0
          - retourne -1 si la valeur n'est pas trouvée dans l’arbre
    """

# Exemples d'utilisation de la fonction node_depth avec la classe BinaryTree :

# arbre = BinaryTree(10)
# arbre.left().elem = 5
# arbre.right().elem = 15
# arbre.left().left().elem = 2
# node_depth(arbre, 10) → 0
# node_depth(arbre, 5) → 1
# node_depth(arbre, 2) → 2
# node_depth(arbre, 99) → -1

# arbre_vide = BinaryTree()
# node_depth(arbre_vide, 42) → -1
