from Tree import BinaryTree

def sum_values(tree: BinaryTree) -> int:
    """
    pre: `tree` est une instance de la classe BinaryTree, contenant des entiers
    post: retourne la somme de toutes les valeurs stockées dans les nœuds de `tree` ;
          retourne 0 si l’arbre est vide
    """
    if tree.is_empty(): return 0
    return tree.get_elem() + sum_values(tree.left()) + sum_values(tree.right())

# Test 1 – Arbre vide
# []
print(sum_values(BinaryTree()))  # 0

# Test 2 – Un seul nœud
#    5
t1 = BinaryTree(5)
print(sum_values(t1))  # 5

# Test 3 – Deux niveaux, deux nœuds
#      10
#     /  \
#    3    7
t2 = BinaryTree(10)
t2.left_tree  = BinaryTree(3)
t2.right_tree = BinaryTree(7)
print(sum_values(t2))  # 20

# Test 4 – Trois niveaux, sous-arbre gauche plus profond
#         8
#        / \
#       4   6
#      /
#     2
t3 = BinaryTree(8)
t3.left_tree              = BinaryTree(4)
t3.right_tree             = BinaryTree(6)
t3.left().left_tree       = BinaryTree(2)
print(sum_values(t3))  # 20 (8+4+6+2)

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
print(sum_values(t4))  # 28

# Test 6 – Arbre déséquilibré à droite
#    9
#     \
#      5
#       \
#        1
t5 = BinaryTree(9)
t5.right_tree             = BinaryTree(5)
t5.right().right_tree     = BinaryTree(1)
print(sum_values(t5))  # 15

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
print(sum_values(t6))  # 0 (0 -3 +4 -2 +1)

