from Tree import BinaryTree

def count_nodes_with_two_children(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds avec exactement deux enfants
    """
    if tree.is_empty(): return 0
    
    if tree.left().is_empty() and tree.right().is_empty(): return count_nodes_with_two_children(tree.left()) + count_nodes_with_two_children(tree.right())
    else:
        if tree.left().is_empty(): return count_nodes_with_two_children(tree.left()) + count_nodes_with_two_children(tree.right())
        elif tree.right().is_empty(): return count_nodes_with_two_children(tree.left()) + count_nodes_with_two_children(tree.right())
        else: return 1 + count_nodes_with_two_children(tree.left()) + count_nodes_with_two_children(tree.right())

# Test 1 - Arbre vide
tree = BinaryTree()
print(count_nodes_with_two_children(tree))  # 0

# Test 2 - Un seul nœud
tree = BinaryTree(1)
print(count_nodes_with_two_children(tree))  # 0

# Test 3 - Racine avec deux enfants
tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)
print(count_nodes_with_two_children(tree))  # 1 (le nœud 1)

# Test 4 - Arbre avec un seul enfant à chaque fois
#         1
#          \
#           2
#            \
#             3
tree = BinaryTree(1)
tree.right_tree = BinaryTree(2)
tree.right().right_tree = BinaryTree(3)
print(count_nodes_with_two_children(tree))  # 0

# Test 5 - Arbre avec plusieurs nœuds ayant deux enfants
#         10
#        /  \
#       5    15
#      / \     \
#     2   7     20
tree = BinaryTree(10)
tree.left_tree = BinaryTree(5)
tree.right_tree = BinaryTree(15)
tree.left().left_tree = BinaryTree(2)
tree.left().right_tree = BinaryTree(7)
tree.right().right_tree = BinaryTree(20)
print(count_nodes_with_two_children(tree))  # 2 (nœuds 10 et 5)

# Test 6 - Arbre plus profond avec deux nœuds complets
#           4
#         /   \
#        2     6
#       / \   / \
#      1   3 5   7
tree = BinaryTree(4)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(6)
tree.left().left_tree = BinaryTree(1)
tree.left().right_tree = BinaryTree(3)
tree.right().left_tree = BinaryTree(5)
tree.right().right_tree = BinaryTree(7)
print(count_nodes_with_two_children(tree))  # 3 (nœuds 4, 2, 6)
