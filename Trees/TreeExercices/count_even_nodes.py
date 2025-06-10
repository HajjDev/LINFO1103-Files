from Tree import BinaryTree

def count_even_nodes(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds avec valeur paire
    """
    if tree.is_empty(): return 0
    
    if tree.get_elem() % 2 == 0: return 1 + count_even_nodes(tree.left()) + count_even_nodes(tree.right())
    return count_even_nodes(tree.left()) + count_even_nodes(tree.right())

# Test 1 - Arbre vide
tree = BinaryTree()
print(count_even_nodes(tree))  # 0

# Test 2 - Un seul nœud pair
tree = BinaryTree(2)
print(count_even_nodes(tree))  # 1

# Test 3 - Un seul nœud impair
tree = BinaryTree(3)
print(count_even_nodes(tree))  # 0

# Test 4 - Arbre avec plusieurs nœuds pairs et impairs
#        4
#       / \
#      2   7
#     /
#    8
tree = BinaryTree(4)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(7)
tree.left().left_tree = BinaryTree(8)
print(count_even_nodes(tree))  # 3 (4, 2, 8)

# Test 5 - Arbre sans aucun nœud pair
#        1
#       / \
#      3   5
tree = BinaryTree(1)
tree.left_tree = BinaryTree(3)
tree.right_tree = BinaryTree(5)
print(count_even_nodes(tree))  # 0

# Test 6 - Arbre complet avec uniquement des nœuds pairs
#         6
#       /   \
#      2     4
#     / \   / \
#    8  10 12 14
tree = BinaryTree(6)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(4)
tree.left().left_tree = BinaryTree(8)
tree.left().right_tree = BinaryTree(10)
tree.right().left_tree = BinaryTree(12)
tree.right().right_tree = BinaryTree(14)
print(count_even_nodes(tree))  # 7
