from Tree import BinaryTree

def has_path_sum(tree: BinaryTree, target_sum: int) -> bool:
    """
    pre: tree est un BinaryTree
    post: retourne True s’il existe un chemin racine-feuille dont la somme des valeurs est égale à target_sum,
          False sinon
    """
    def has_path_sum_rec(tree, current_path, target_sum):
        if tree.is_empty(): return False
        
        if tree.right().is_empty() and tree.left().is_empty():
            current_sum = sum(current_path[:] + [tree.get_elem()])
            if current_sum == target_sum: return True
            return False
        
        current_path.append(tree.get_elem())
        left = has_path_sum_rec(tree.left(), current_path, target_sum)
        right = has_path_sum_rec(tree.right(), current_path, target_sum)
        current_path.pop()
        return left or right
    
    return has_path_sum_rec(tree, [], target_sum)

# Test 1 – Arbre vide (aucun chemin)
# []
print(has_path_sum(BinaryTree(), 0))   # False
print(has_path_sum(BinaryTree(), 5))   # False

# Test 2 – Un seul nœud égal à target_sum
#    7
t1 = BinaryTree(7)
print(has_path_sum(t1, 7))             # True
print(has_path_sum(t1, 5))             # False

# Test 3 – Deux niveaux, chemin gauche
#      10
#     /
#    5
t2 = BinaryTree(10)
t2.left_tree = BinaryTree(5)
print(has_path_sum(t2, 15))            # True  (10+5)
print(has_path_sum(t2, 10))            # False (10 n’est pas une feuille)

# Test 4 – Deux niveaux, chemin droit
#      10
#        \
#         3
t3 = BinaryTree(10)
t3.right_tree = BinaryTree(3)
print(has_path_sum(t3, 13))            # True  (10+3)
print(has_path_sum(t3, 7))             # False

# Test 5 – Troisième niveau, plusieurs chemins
#         1
#        / \
#       2   3
#          /
#         4
t4 = BinaryTree(1)
t4.left_tree = BinaryTree(2)
t4.right_tree = BinaryTree(3)
t4.right().left_tree = BinaryTree(4)
# Chemins : [1+2=3], [1+3+4=8]
print(has_path_sum(t4, 3))             # True
print(has_path_sum(t4, 8))             # True
print(has_path_sum(t4, 5))             # False

# Test 6 – Valeurs négatives
#        -2
#          \
#           -3
t5 = BinaryTree(-2)
t5.right_tree = BinaryTree(-3)
# Chemin : -2 + -3 = -5
print(has_path_sum(t5, -5))            # True
print(has_path_sum(t5, -2))            # False

# Test 7 – Arbre complet 3 niveaux
#          5
#         / \
#        3   8
#       / \ / \
#      1  2 6  4
t6 = BinaryTree(5)
t6.left_tree = BinaryTree(3)
t6.right_tree = BinaryTree(8)
t6.left().left_tree = BinaryTree(1)
t6.left().right_tree = BinaryTree(2)
t6.right().left_tree = BinaryTree(6)
t6.right().right_tree = BinaryTree(4)
# Chemins sums: [5+3+1=9], [5+3+2=10], [5+8+6=19], [5+8+4=17]
print(has_path_sum(t6, 10))            # True
print(has_path_sum(t6, 17))            # True
print(has_path_sum(t6, 15))            # False
