from Tree import BinaryTree

def find_path(tree: BinaryTree, value: int) -> list:
    """
    pre: tree est un BinaryTree, value est un int
    post: retourne la liste des valeurs du chemin de la racine au premier nœud contenant value,
          [] si value non trouvé
    """

# Exemples :
# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.left().right().elem = 4
# find_path(arbre, 4) → [1, 2, 4]
# find_path(arbre, 5) → []