from Tree import BinaryTree

def count_nodes_with_value(tree: BinaryTree, value: int) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds contenant la valeur donnée
    """
    if tree.is_empty(): return 0
    
    if tree.get_elem() == value: return 1 + count_nodes_with_value(tree.left(), value) + count_nodes_with_value(tree.right(), value)
    return count_nodes_with_value(tree.left(), value) + count_nodes_with_value(tree.right(), value)

# Test 1 - Arbre vide
tree = BinaryTree()
print(count_nodes_with_value(tree, 5))  # 0

# Test 2 - Un seul nœud avec la valeur recherchée
tree = BinaryTree(7)
print(count_nodes_with_value(tree, 7))  # 1

# Test 3 - Un seul nœud, valeur différente
tree = BinaryTree(3)
print(count_nodes_with_value(tree, 7))  # 0

# Test 4 - Plusieurs nœuds avec plusieurs occurrences
#        5
#       / \
#      7   5
#         / \
#        7   9
tree = BinaryTree(5)
tree.left_tree = BinaryTree(7)
tree.right_tree = BinaryTree(5)
tree.right().left_tree = BinaryTree(7)
tree.right().right_tree = BinaryTree(9)
print(count_nodes_with_value(tree, 7))  # 2

# Test 5 - Valeur absente
#        1
#       / \
#      2   3
tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)
print(count_nodes_with_value(tree, 4))  # 0

# Test 6 - Toutes valeurs identiques à la valeur recherchée
#       8
#      / \
#     8   8
tree = BinaryTree(8)
tree.left_tree = BinaryTree(8)
tree.right_tree = BinaryTree(8)
print(count_nodes_with_value(tree, 8))  # 3
