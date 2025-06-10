from Tree import BinaryTree

def count_nodes_at_depth(tree: BinaryTree, target_depth: int) -> int:
    """
    pre: `tree` est une instance de la classe BinaryTree, `target_depth` est un entier ≥ 0
    post: retourne le nombre de nœuds présents exactement à la profondeur `target_depth` dans `tree`
          - la racine est à la profondeur 0
          - retourne 0 si l’arbre est vide ou si aucun nœud ne se trouve à cette profondeur
    """
    def count_nodes_at_depth_rec(tree, actual_depth, target_depth):
        if tree.is_empty(): return 0
        
        if actual_depth == target_depth: return 1 + count_nodes_at_depth_rec(tree.left(), actual_depth + 1, target_depth) + count_nodes_at_depth_rec(tree.right(), actual_depth + 1, target_depth)
        return count_nodes_at_depth_rec(tree.left(), actual_depth + 1, target_depth) + count_nodes_at_depth_rec(tree.right(), actual_depth + 1, target_depth)

    return count_nodes_at_depth_rec(tree, 0, target_depth)


# Arbre vide
# depth 0 -> 0
print(count_nodes_at_depth(BinaryTree(), 0))  # 0

# Arbre avec un seul nœud (racine)
root = BinaryTree(1)
print(count_nodes_at_depth(root, 0))  # 1
print(count_nodes_at_depth(root, 1))  # 0

# Arbre 2 niveaux
#      1
#     / \
#    2   3
root.left_tree = BinaryTree(2)
root.right_tree = BinaryTree(3)
print(count_nodes_at_depth(root, 0))  # 1
print(count_nodes_at_depth(root, 1))  # 2
print(count_nodes_at_depth(root, 2))  # 0

# Arbre 3 niveaux
#       1
#      / \
#     2   3
#    /
#   4
root.left().left_tree = BinaryTree(4)
print(count_nodes_at_depth(root, 0))  # 1
print(count_nodes_at_depth(root, 1))  # 2
print(count_nodes_at_depth(root, 2))  # 1
print(count_nodes_at_depth(root, 3))  # 0
