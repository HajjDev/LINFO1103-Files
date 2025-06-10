from Tree import BinaryTree

def find_path(tree: BinaryTree, value: int) -> list:
    """
    pre: tree est un BinaryTree, value est un int
    post: retourne la liste des valeurs du chemin de la racine au premier nœud contenant value,
          [] si value non trouvé
    """
    def find_path_rec(tree, value, ancestors):
        if tree.is_empty(): return False
        
        if tree.get_elem() == value: ancestors.append(tree.get_elem()); return True
        if find_path_rec(tree.left(), value, ancestors) or find_path_rec(tree.right(), value, ancestors): ancestors.append(tree.get_elem())
        return ancestors
    
    ancestors = find_path_rec(tree, value, [])
    if ancestors != True and ancestors != False: return ancestors[::-1]
    elif ancestors == True: return [tree.get_elem()]
    else: return []

# Test 1 : Arbre simple, value = racine
#        10
# Chemin attendu: [10]
root1 = BinaryTree(10)

# Test 2 : Arbre avec deux niveaux, value = feuille gauche
#        10
#       /  \
#      5    15
# Chemin attendu: [10, 5]
root2 = BinaryTree(10)
root2.left_tree = BinaryTree(5)
root2.right_tree = BinaryTree(15)

# Test 3 : Arbre avec trois niveaux, value = feuille droite droite
#          10
#         /  \
#        5    15
#             / \
#            12  20
# Chemin attendu: [10, 15, 20]
root3 = BinaryTree(10)
root3.left_tree = BinaryTree(5)
root3.right_tree = BinaryTree(15)
root3.right().left_tree = BinaryTree(12)
root3.right().right_tree = BinaryTree(20)

# Test 4 : Value non présente dans l'arbre
#        10
#       /  \
#      5    15
# Recherche de 100 (non présent)
# Chemin attendu: []
root4 = root2  # réutilise root2

# Test 5 : Arbre vide
# Chemin attendu: []
root5 = BinaryTree()

# Test 6 : Value au milieu gauche
#          8
#         / \
#        3   10
#       / \
#      1   6
#          /
#         4
# Chemin attendu: [8, 3, 6, 4]
root6 = BinaryTree(8)
root6.left_tree = BinaryTree(3)
root6.right_tree = BinaryTree(10)
root6.left().left_tree = BinaryTree(1)
root6.left().right_tree = BinaryTree(6)
root6.left().right().left_tree = BinaryTree(4)

# Test 7 : Value à la racine d’un arbre plus grand
# Chemin attendu: [8]
root7 = root6

# --- Exemple d'appel de la fonction avec affichage ---

print(find_path(root1, 10))  # [10]
print(find_path(root2, 5))   # [10, 5]
print(find_path(root3, 20))  # [10, 15, 20]
print(find_path(root4, 100)) # []
print(find_path(root5, 1))   # []
print(find_path(root6, 4))   # [8, 3, 6, 4]
print(find_path(root7, 8))   # [8]
