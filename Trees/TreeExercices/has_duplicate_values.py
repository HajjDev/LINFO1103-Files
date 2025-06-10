from Tree import BinaryTree

def has_duplicate_values(tree: BinaryTree) -> bool:
    """
    pre: tree est un BinaryTree
    post: retourne True si l’arbre contient au moins une valeur répétée, False sinon
    """
    def get_values(tree, values):
        if tree.is_empty(): return values
        
        values.append(tree.get_elem())
        get_values(tree.left(), values)
        get_values(tree.right(), values)
        
        return values
    
    values = get_values(tree, [])
    return len(values) != len(set(values))

# Test 1 – Arbre vide
# []
print(has_duplicate_values(BinaryTree()))  # False

# Test 2 – Un seul nœud
#    5
single = BinaryTree(5)
print(has_duplicate_values(single))  # False

# Test 3 – Deux nœuds identiques
#   5
#  / \
# 5   None
dup1 = BinaryTree(5)
dup1.left_tree = BinaryTree(5)
print(has_duplicate_values(dup1))  # True

# Test 4 – Trois nœuds, deux duplicata non-adjacents
#      10
#     /  \
#    5    15
#         /
#        5
dup2 = BinaryTree(10)
dup2.left_tree = BinaryTree(5)
dup2.right_tree = BinaryTree(15)
dup2.right().left_tree = BinaryTree(5)
print(has_duplicate_values(dup2))  # True

# Test 5 – Plusieurs nœuds, aucune duplication
#      8
#     / \
#    3   12
#   / \    \
#  1   5    15
unique = BinaryTree(8)
unique.left_tree = BinaryTree(3)
unique.right_tree = BinaryTree(12)
unique.left().left_tree = BinaryTree(1)
unique.left().right_tree = BinaryTree(5)
unique.right().right_tree = BinaryTree(15)
print(has_duplicate_values(unique))  # False

# Test 6 – Tous les nœuds égaux
#    7
#   / \
#  7   7
all_same = BinaryTree(7)
all_same.left_tree = BinaryTree(7)
all_same.right_tree = BinaryTree(7)
print(has_duplicate_values(all_same))  # True

# Test 7 – Arbre plus profond avec duplicata profond
#         20
#        /  \
#      10    30
#     /  \     \
#    5   15     10
deep_dup = BinaryTree(20)
deep_dup.left_tree = BinaryTree(10)
deep_dup.right_tree = BinaryTree(30)
deep_dup.left().left_tree = BinaryTree(5)
deep_dup.left().right_tree = BinaryTree(15)
deep_dup.right().right_tree = BinaryTree(10)
print(has_duplicate_values(deep_dup))  # True
