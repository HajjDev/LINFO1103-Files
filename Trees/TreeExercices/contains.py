from Tree import BinaryTree

def contains(tree: BinaryTree, value: int) -> bool:
    """
    pre: `tree` est une instance de la classe BinaryTree, `value` est un entier
    post: retourne True si `value` est présent dans au moins un nœud de `tree`, False sinon
    """
    if tree.is_empty(): return False
    
    if tree.get_elem() == value: return True
    return contains(tree.left(), value) or contains(tree.right(), value)
    

# Test 1 - Arbre vide
tree = BinaryTree()
print(contains(tree, 5))  # False

# Test 2 - Valeur présente à la racine
tree = BinaryTree(10)
print(contains(tree, 10))  # True

# Test 3 - Valeur présente dans un sous-arbre
#       5
#      / \
#     3   8
tree = BinaryTree(5)
tree.left_tree = BinaryTree(3)
tree.right_tree = BinaryTree(8)
print(contains(tree, 3))  # True
print(contains(tree, 8))  # True
print(contains(tree, 7))  # False

# Test 4 - Valeur présente en profondeur
#        1
#         \
#          2
#           \
#            3
tree = BinaryTree(1)
tree.right_tree = BinaryTree(2)
tree.right().right_tree = BinaryTree(3)
print(contains(tree, 3))  # True
print(contains(tree, 4))  # False

# Test 5 - Plusieurs occurrences
#        4
#       / \
#      2   4
tree = BinaryTree(4)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(4)
print(contains(tree, 4))  # True
print(contains(tree, 2))  # True
print(contains(tree, 5))  # False

