from Tree import BinaryTree

def count_nodes_with_value_multiple_of(tree: BinaryTree, k: int) -> int:
    """
    pre: tree est un BinaryTree, k > 0
    post: retourne le nombre de nœuds dont la valeur est un multiple de k
    """
    if tree.is_empty(): return 0
    
    if tree.get_elem() % k == 0: return 1 + count_nodes_with_value_multiple_of(tree.left(), k) + count_nodes_with_value_multiple_of(tree.right(), k)
    return count_nodes_with_value_multiple_of(tree.left(), k) + count_nodes_with_value_multiple_of(tree.right(), k)

# Test 1 - Arbre vide
tree = BinaryTree()
print(count_nodes_with_value_multiple_of(tree, 3))  # 0

# Test 2 - Un seul nœud multiple de k
tree = BinaryTree(9)
print(count_nodes_with_value_multiple_of(tree, 3))  # 1

# Test 3 - Un seul nœud non multiple de k
tree = BinaryTree(10)
print(count_nodes_with_value_multiple_of(tree, 3))  # 0

# Test 4 - Plusieurs nœuds, certains multiples de k
#        6
#       / \
#      3   8
#         / \
#        12  7
tree = BinaryTree(6)
tree.left_tree = BinaryTree(3)
tree.right_tree = BinaryTree(8)
tree.right().left_tree = BinaryTree(12)
tree.right().right_tree = BinaryTree(7)
print(count_nodes_with_value_multiple_of(tree, 3))  # 3 (6, 3, 12)

# Test 5 - Tous multiples de k
#        4
#       / \
#      8  12
tree = BinaryTree(4)
tree.left_tree = BinaryTree(8)
tree.right_tree = BinaryTree(12)
print(count_nodes_with_value_multiple_of(tree, 4))  # 3

# Test 6 - Aucun multiple de k
#        5
#       / \
#      7   11
tree = BinaryTree(5)
tree.left_tree = BinaryTree(7)
tree.right_tree = BinaryTree(11)
print(count_nodes_with_value_multiple_of(tree, 3))  # 0

# Test 7 - k = 1 (tous les nœuds comptent)
#        2
#       / \
#      4   5
tree = BinaryTree(2)
tree.left_tree = BinaryTree(4)
tree.right_tree = BinaryTree(5)
print(count_nodes_with_value_multiple_of(tree, 1))  # 3
