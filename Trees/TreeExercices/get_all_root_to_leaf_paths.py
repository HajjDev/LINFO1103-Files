from Tree import BinaryTree

def get_all_root_to_leaf_paths(tree: BinaryTree) -> list:
    """
    pre: tree est un BinaryTree
    post: retourne une liste de listes, chaque sous-liste représentant un chemin de la racine à une feuille
    """
    def get_all_root_to_leaf_paths_rec(tree, current_path, all_paths):
        if tree.is_empty(): return all_paths
        
        if tree.left().is_empty() and tree.right().is_empty():
            all_paths.append(current_path[:] + [tree.get_elem()])
            return all_paths
        
        current_path.append(tree.get_elem())
        get_all_root_to_leaf_paths_rec(tree.left(), current_path, all_paths)
        get_all_root_to_leaf_paths_rec(tree.right(), current_path, all_paths)
        current_path.pop()
        return all_paths
    
    return get_all_root_to_leaf_paths_rec(tree, [], [])
    

# Test 1 – Arbre vide
# []
print(get_all_root_to_leaf_paths(BinaryTree()))  # []

# Test 2 – Un seul nœud
#    10
single = BinaryTree(10)
print(get_all_root_to_leaf_paths(single))  # [[10]]

# Test 3 – Deux niveaux
#      1
#     / \
#    2   3
root2 = BinaryTree(1)
root2.left_tree = BinaryTree(2)
root2.right_tree = BinaryTree(3)
print(get_all_root_to_leaf_paths(root2))  # [[1, 2], [1, 3]]

# Test 4 – Trois niveaux, un seul chemin complet
#      1
#     /
#    2
#   /
#  3
root3 = BinaryTree(1)
root3.left_tree = BinaryTree(2)
root3.left().left_tree = BinaryTree(3)
print(get_all_root_to_leaf_paths(root3))  # [[1, 2, 3]]

# Test 5 – Trois niveaux, deux feuilles différentes
#        5
#       / \
#      4   6
#         /
#        7
root5 = BinaryTree(5)
root5.left_tree = BinaryTree(4)
root5.right_tree = BinaryTree(6)
root5.right().left_tree = BinaryTree(7)
print(get_all_root_to_leaf_paths(root5))  # [[5, 4], [5, 6, 7]]

# Test 6 – Arbre complet 3 niveaux
#         8
#        / \
#       3   10
#      / \  / \
#     1  6 9  14
root6 = BinaryTree(8)
root6.left_tree = BinaryTree(3)
root6.right_tree = BinaryTree(10)
root6.left().left_tree = BinaryTree(1)
root6.left().right_tree = BinaryTree(6)
root6.right().left_tree = BinaryTree(9)
root6.right().right_tree = BinaryTree(14)
print(get_all_root_to_leaf_paths(root6))  
# [[8, 3, 1], [8, 3, 6], [8, 10, 9], [8, 10, 14]]

# Test 7 – Arbre déséquilibré 4 niveaux
#        2
#         \
#          5
#         / \
#        7   9
#           /
#          11
root7 = BinaryTree(2)
root7.right_tree = BinaryTree(5)
root7.right().left_tree = BinaryTree(7)
root7.right().right_tree = BinaryTree(9)
root7.right().right().left_tree = BinaryTree(11)
print(get_all_root_to_leaf_paths(root7))  # [[2, 5, 7], [2, 5, 9, 11]]
