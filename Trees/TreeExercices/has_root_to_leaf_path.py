from Tree import BinaryTree

def has_root_to_leaf_path(tree: BinaryTree, path: list) -> bool:
    """
    pre: tree est un BinaryTree, path est une liste d'entiers
    post: retourne True si la séquence path correspond à un chemin de la racine à une feuille
    """
    def get_all_root_to_leaf_paths(tree, current_path, all_paths):
        if tree.is_empty(): return all_paths
        
        if tree.left().is_empty() and tree.right().is_empty():
            all_paths.append(current_path[:] + [tree.get_elem()])
            return all_paths
        
        current_path.append(tree.get_elem())
        get_all_root_to_leaf_paths(tree.left(), current_path, all_paths)
        get_all_root_to_leaf_paths(tree.right(), current_path, all_paths)
        current_path.pop()
        return all_paths
    
    all_paths = get_all_root_to_leaf_paths(tree, [], [])
    return path in all_paths or path == all_paths

# ——— Tests ———

# 1) Arbre vide
print(has_root_to_leaf_path(BinaryTree(), []))        # True (le chemin vide correspond à l'arbre vide)
print(has_root_to_leaf_path(BinaryTree(), [1]))       # False

# 2) Racine seule
t1 = BinaryTree(5)
print(has_root_to_leaf_path(t1, [5]))                 # True
print(has_root_to_leaf_path(t1, []))                  # False

# 3) Deux niveaux
#       1
#      / \
#     2   3
t2 = BinaryTree(1)
t2.left_tree  = BinaryTree(2)
t2.right_tree = BinaryTree(3)
print(has_root_to_leaf_path(t2, [1, 2]))              # True
print(has_root_to_leaf_path(t2, [1, 3]))              # True
print(has_root_to_leaf_path(t2, [1, 4]))              # False

# 4) Trois niveaux, chemin valide & invalide
#         10
#        /  \
#       5    8
#      / \
#     3   7
t3 = BinaryTree(10)
t3.left_tree  = BinaryTree(5)
t3.right_tree = BinaryTree(8)
t3.left().left_tree  = BinaryTree(3)
t3.left().right_tree = BinaryTree(7)
print(has_root_to_leaf_path(t3, [10, 5, 7]))          # True
print(has_root_to_leaf_path(t3, [10, 8]))             # True
print(has_root_to_leaf_path(t3, [10, 5]))             # False (5 n'est pas une feuille)
print(has_root_to_leaf_path(t3, [10, 5, 4]))          # False

# 5) Arbre déséquilibré
#    1
#     \
#      2
#       \
#        3
t4 = BinaryTree(1)
t4.right_tree          = BinaryTree(2)
t4.right().right_tree  = BinaryTree(3)
print(has_root_to_leaf_path(t4, [1, 2, 3]))           # True
print(has_root_to_leaf_path(t4, [1, 3]))   