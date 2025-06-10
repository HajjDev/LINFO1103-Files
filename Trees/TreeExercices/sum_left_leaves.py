from Tree import BinaryTree

def sum_left_leaves(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne la somme des valeurs des feuilles qui sont des fils gauche
    """
    def sum_left_leaves_rec(tree, is_left = False):
        if tree.is_empty(): return 0
        
        if is_left and tree.right().is_empty() and tree.left().is_empty(): return tree.get_elem() + sum_left_leaves_rec(tree.left(), is_left = True) + sum_left_leaves_rec(tree.right(), is_left = False)
        else: return sum_left_leaves_rec(tree.left(), is_left = True) + sum_left_leaves_rec(tree.right(), is_left = False)
    
    return sum_left_leaves_rec(tree)

# Test 1 – Arbre vide
# []
print(sum_left_leaves(BinaryTree()))  # 0

# Test 2 – Racine seule (pas de fils)
#    5
t1 = BinaryTree(5)
print(sum_left_leaves(t1))  # 0

# Test 3 – Un seul fils gauche qui est une feuille
#    5
#   /
#  3
t2 = BinaryTree(5)
t2.left_tree = BinaryTree(3)
print(sum_left_leaves(t2))  # 3

# Test 4 – Un seul fils droit qui est une feuille
#    5
#     \
#      4
t3 = BinaryTree(5)
t3.right_tree = BinaryTree(4)
print(sum_left_leaves(t3))  # 0

# Test 5 – Plusieurs feuilles gauches et droites
#        10
#       /  \
#      2    8
#     / \    \
#    4   5    6
t4 = BinaryTree(10)
t4.left_tree = BinaryTree(2)
t4.right_tree = BinaryTree(8)
t4.left().left_tree = BinaryTree(4)
t4.left().right_tree = BinaryTree(5)
t4.right().right_tree = BinaryTree(6)
# Feuilles gauches: 4
print(sum_left_leaves(t4))  # 4

# Test 6 – Plusieurs fils gauches profonds
#           1
#          / \
#         2   3
#        /     \
#       4       5
#      / \
#     6   7
t5 = BinaryTree(1)
t5.left_tree = BinaryTree(2)
t5.right_tree = BinaryTree(3)
t5.left().left_tree = BinaryTree(4)
t5.right().right_tree = BinaryTree(5)
t5.left().left().left_tree = BinaryTree(6)
t5.left().left().right_tree = BinaryTree(7)
# Feuilles gauches: 6  (7 is right child of 4)
print(sum_left_leaves(t5))  # 6

# Test 7 – Arbre complet avec feuilles gauches multiples
#           7
#         /   \
#        3     9
#       / \   / \
#      1   4 8   10
t6 = BinaryTree(7)
t6.left_tree = BinaryTree(3)
t6.right_tree = BinaryTree(9)
t6.left().left_tree = BinaryTree(1)
t6.left().right_tree = BinaryTree(4)
t6.right().left_tree = BinaryTree(8)
t6.right().right_tree = BinaryTree(10)
# Feuilles gauches: 1, 8
print(sum_left_leaves(t6))  # 9
