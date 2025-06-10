from Tree import BinaryTree

def find_max_root_to_leaf_path_sum(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne la somme maximale des valeurs sur un chemin de la racine à une feuille,
          0 si arbre vide
    """
    def find_max_root_to_leaf_path_sum(tree, path, max_path_sum):
        if tree.is_empty(): return max_path_sum
        
        if tree.left().is_empty() and tree.right().is_empty():
            complete_sum = sum(path[:] + [tree.get_elem()])
            if complete_sum > max_path_sum: max_path_sum = complete_sum
            return max_path_sum
        
        path.append(tree.get_elem())
        left = find_max_root_to_leaf_path_sum(tree.left(), path, max_path_sum)
        right = find_max_root_to_leaf_path_sum(tree.right(), path, max_path_sum)
        path.pop()
        return max(left, right)
    
    return find_max_root_to_leaf_path_sum(tree, [], 0)
        
# Test 1 – Arbre vide
# []
print(find_max_root_to_leaf_path_sum(BinaryTree()))  # 0

# Test 2 – Un seul nœud
#    5
t1 = BinaryTree(5)
print(find_max_root_to_leaf_path_sum(t1))  # 5

# Test 3 – Deux niveaux
#      10
#     /  \
#    3    7
t2 = BinaryTree(10)
t2.left_tree  = BinaryTree(3)
t2.right_tree = BinaryTree(7)
# Chemins : [10+3, 10+7] → [13, 17]
print(find_max_root_to_leaf_path_sum(t2))  # 17

# Test 4 – Trois niveaux, gauche plus profond
#         8
#        / \
#       4   6
#      /
#     2
t3 = BinaryTree(8)
t3.left_tree              = BinaryTree(4)
t3.right_tree             = BinaryTree(6)
t3.left().left_tree       = BinaryTree(2)
# Chemins : [8+4+2, 8+6] → [14, 14]
print(find_max_root_to_leaf_path_sum(t3))  # 14

# Test 5 – Arbre complet 3 niveaux
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
t4 = BinaryTree(1)
t4.left_tree              = BinaryTree(2)
t4.right_tree             = BinaryTree(3)
t4.left().left_tree       = BinaryTree(4)
t4.left().right_tree      = BinaryTree(5)
t4.right().left_tree      = BinaryTree(6)
t4.right().right_tree     = BinaryTree(7)
# Chemins sums: [1+2+4,1+2+5,1+3+6,1+3+7] → [7,8,10,11]
print(find_max_root_to_leaf_path_sum(t4))  # 11

# Test 6 – Arbre déséquilibré à droite
#    9
#     \
#      5
#       \
#        1
t5 = BinaryTree(9)
t5.right_tree             = BinaryTree(5)
t5.right().right_tree     = BinaryTree(1)
# Chemin : [9+5+1] → 15
print(find_max_root_to_leaf_path_sum(t5))  # 15

# Test 7 – Mélange de valeurs négatives et positives
#        0
#       / \
#     -3   4
#     / \
#   -2   1
t6 = BinaryTree(0)
t6.left_tree              = BinaryTree(-3)
t6.right_tree             = BinaryTree(4)
t6.left().left_tree       = BinaryTree(-2)
t6.left().right_tree      = BinaryTree(1)
# Chemins : [0-3-2, 0-3+1, 0+4] → [-5, -2, 4]
print(find_max_root_to_leaf_path_sum(t6))  # 4
