from Tree import BinaryTree

def count_single_child_nodes(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds ayant exactement un enfant
    """
    if tree.is_empty(): return 0
    
    if tree.left().is_empty() and tree.right().is_empty(): return count_single_child_nodes(tree.left()) + count_single_child_nodes(tree.right())
    else:
        if tree.left().is_empty(): return 1 + count_single_child_nodes(tree.left()) + count_single_child_nodes(tree.right())
        elif tree.right().is_empty(): return 1 + count_single_child_nodes(tree.left()) + count_single_child_nodes(tree.right())
        else: return count_single_child_nodes(tree.left()) + count_single_child_nodes(tree.right())

# Test 1 - Arbre vide
tree = BinaryTree()
print(count_single_child_nodes(tree))  # 0

# Test 2 - Un seul nœud
tree = BinaryTree(1)
print(count_single_child_nodes(tree))  # 0

# Test 3 - Racine avec un seul enfant gauche
tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
print(count_single_child_nodes(tree))  # 1

# Test 4 - Racine avec deux enfants
tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)
print(count_single_child_nodes(tree))  # 0

# Test 5 - Arbre avec plusieurs nœuds ayant un seul enfant
#         1
#        / 
#       2
#        \
#         3
#        /
#       4
tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.left().right_tree = BinaryTree(3)
tree.left().right().left_tree = BinaryTree(4)
print(count_single_child_nodes(tree))  # 3 (1 has 1 child, 2 has 1 child, 3 has 1 child)

# Test 6 - Arbre avec mélange de nœuds avec 0, 1 et 2 enfants
#         5
#        / \
#       3   8
#      /     \
#     1       9
tree = BinaryTree(5)
tree.left_tree = BinaryTree(3)
tree.right_tree = BinaryTree(8)
tree.left().left_tree = BinaryTree(1)
tree.right().right_tree = BinaryTree(9)
print(count_single_child_nodes(tree))  # 2 (3 and 8 have one child each)
