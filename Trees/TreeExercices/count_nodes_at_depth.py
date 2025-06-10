from Tree import BinaryTree

def count_nodes_at_depth(tree: BinaryTree, target_depth: int) -> int:
    """
    pre: `tree` est une instance de la classe BinaryTree, `target_depth` est un entier ≥ 0
    post: retourne le nombre de nœuds présents exactement à la profondeur `target_depth` dans `tree`
          - la racine est à la profondeur 0
          - retourne 0 si l’arbre est vide ou si aucun nœud ne se trouve à cette profondeur
    """

# Exemples d'utilisation de la fonction count_nodes_at_depth avec la classe BinaryTree :

# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# arbre.right().left().elem = 5

# count_nodes_at_depth(arbre, 0) → 1   (racine)
# count_nodes_at_depth(arbre, 1) → 2   (2 et 3)
# count_nodes_at_depth(arbre, 2) → 2   (4 et 5)
# count_nodes_at_depth(arbre, 3) → 0

# arbre_vide = BinaryTree()
# count_nodes_at_depth(arbre_vide, 0) → 0
