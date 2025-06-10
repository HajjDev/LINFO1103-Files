from Tree import BinaryTree

def count_nodes_with_odd_ancestors(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds qui ont un nombre impair d’ancêtres (profondeur impaire)
    """
    def count_nodes_with_odd_ancestors_rec(tree, ancestor_number):
        if tree.is_empty(): return 0
        
        if ancestor_number % 2 != 0: return 1 + count_nodes_with_odd_ancestors_rec(tree.left(), ancestor_number + 1) + count_nodes_with_odd_ancestors_rec(tree.right(), ancestor_number + 1)
        return count_nodes_with_odd_ancestors_rec(tree.left(), ancestor_number + 1) + count_nodes_with_odd_ancestors_rec(tree.right(), ancestor_number + 1)
    
    return count_nodes_with_odd_ancestors_rec(tree, 0)

# Test 1 : Arbre vide
# []
print(count_nodes_with_odd_ancestors(BinaryTree()))  # 0

# Test 2 : Arbre 1 niveau (racine seule)
#    10
root = BinaryTree(10)
print(count_nodes_with_odd_ancestors(root))  # 0 (profondeur racine = 0, pair)

# Test 3 : Arbre 2 niveaux
#      10
#     /  \
#   20    30
root.left_tree = BinaryTree(20)
root.right_tree = BinaryTree(30)
print(count_nodes_with_odd_ancestors(root))  # 2 (20 et 30 à profondeur 1, impair)

# Test 4 : Arbre 3 niveaux, gauche complet, droite partiel
#        10
#       /  \
#     20    30
#    /  \   /
#  40   50 60
root.left().left_tree = BinaryTree(40)
root.left().right_tree = BinaryTree(50)
root.right().left_tree = BinaryTree(60)
print(count_nodes_with_odd_ancestors(root))  # 2 (20 et 30 à profondeur 1)

# Test 5 : Arbre 3 niveaux complet
#        10
#       /  \
#     20    30
#    / \    / \
#  40  50  60 70
root.right().right_tree = BinaryTree(70)
print(count_nodes_with_odd_ancestors(root))  # 2 (20, 30, 40, 50, 60, 70 ? Attention!)

# Explication Test 5 :
# Profondeurs : 
# 10 (0) → pair → non compté
# 20, 30 (1) → impair → compté (2)
# 40, 50, 60, 70 (2) → pair → non compté
# Résultat attendu : 2

# Test 6 : Arbre 4 niveaux, mélange gauche/droite
#            10
#          /    \
#        20      30
#       /       /  \
#     40      60    70
#    / 
#  80
root.left().left().left_tree = BinaryTree(80)
print(count_nodes_with_odd_ancestors(root))  # 3 (20,30 à profondeur 1 et 80 à profondeur 3)

# Test 7 : Arbre uniquement à droite, profondeur 4
#  10
#    \
#     30
#       \
#        70
#          \
#           90
root = BinaryTree(10)
root.right_tree = BinaryTree(30)
root.right().right_tree = BinaryTree(70)
root.right().right().right_tree = BinaryTree(90)
print(count_nodes_with_odd_ancestors(root))  # 2 (30 à profondeur 1, 70 à profondeur 2 non compté, 90 à profondeur 3 compté)
