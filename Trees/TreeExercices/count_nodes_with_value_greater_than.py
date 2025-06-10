from Tree import BinaryTree

def count_nodes_with_value_greater_than(tree: BinaryTree, threshold: int) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds avec une valeur strictement supérieure à threshold
    """
    if tree.is_empty(): return 0
    
    if tree.get_elem() > threshold: return 1 + count_nodes_with_value_greater_than(tree.left(), threshold) + count_nodes_with_value_greater_than(tree.right(), threshold)
    return count_nodes_with_value_greater_than(tree.left(), threshold) + count_nodes_with_value_greater_than(tree.right(), threshold)

# Test 1 – Arbre vide
tree = BinaryTree()
print(count_nodes_with_value_greater_than(tree, 5))  # 0

# Test 2 – Un seul nœud, valeur > seuil
tree = BinaryTree(10)
print(count_nodes_with_value_greater_than(tree, 5))  # 1

# Test 3 – Un seul nœud, valeur <= seuil
tree = BinaryTree(3)
print(count_nodes_with_value_greater_than(tree, 5))  # 0

# Test 4 – Plusieurs nœuds avec différentes valeurs
#        8
#       / \
#      3   10
#         /  \
#        9   12
tree = BinaryTree(8)
tree.left_tree = BinaryTree(3)
tree.right_tree = BinaryTree(10)
tree.right().left_tree = BinaryTree(9)
tree.right().right_tree = BinaryTree(12)
print(count_nodes_with_value_greater_than(tree, 9))  # 2 (10 et 12)

# Test 5 – Toutes les valeurs < seuil
#       2
#      / \
#     1   0
tree = BinaryTree(2)
tree.left_tree = BinaryTree(1)
tree.right_tree = BinaryTree(0)
print(count_nodes_with_value_greater_than(tree, 5))  # 0

# Test 6 – Toutes les valeurs > seuil
#        20
#       /  \
#     15   25
tree = BinaryTree(20)
tree.left_tree = BinaryTree(15)
tree.right_tree = BinaryTree(25)
print(count_nodes_with_value_greater_than(tree, 10))  # 3

# Test 7 – Seuil négatif
#       4
#      / \
#    -3   7
tree = BinaryTree(4)
tree.left_tree = BinaryTree(-3)
tree.right_tree = BinaryTree(7)
print(count_nodes_with_value_greater_than(tree, -5))  # 3 (tous > -5)