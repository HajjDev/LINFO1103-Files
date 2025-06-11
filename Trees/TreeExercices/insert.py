from Tree import BinaryTree

def insert(tree, val: int):
    """
    pre: -
    post: insère val dans l'arbre binaire de recherche (ABR) en respectant
          les propriétés d'un ABR (éléments strictement inférieurs à gauche,
          strictement supérieurs à droite). Si val est déjà présent, l'arbre
          reste inchangé.
    """
    if tree.is_empty():
        tree.setelem(val)
        tree.setright(BinaryTree())
        tree.setleft(BinaryTree())
        return tree
    
    if tree.get_elem() > val: insert(tree.left(), val)
    elif tree.get_elem() < val: insert(tree.right(), val)
    return tree
    
# Exemple 1
tree1 = BinaryTree()
insert(tree1, 10)
# Arbre :
#   10

# Exemple 2
tree2 = BinaryTree()
insert(tree2, 10)
insert(tree2, 5)
#     10
#    /
#   5

# Exemple 3
tree3 = BinaryTree()
insert(tree3, 10)
insert(tree3, 15)
#     10
#       \
#       15

# Exemple 4
tree4 = BinaryTree()
for v in [10, 5, 15, 3, 7, 12, 20]:
    insert(tree4, v)
#         10
#        /  \
#       5    15
#      / \   / \
#     3   7 12 20

# Exemple 5
tree5 = BinaryTree()
insert(tree5, 10)
insert(tree5, 5)
insert(tree5, 10)  # doublon ignoré
#     10
#    /
#   5

# Exemple 6 : croissant
tree6 = BinaryTree()
for v in [1, 2, 3, 4, 5]:
    insert(tree6, v)
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5

# Exemple 7 : décroissant
tree7 = BinaryTree()
for v in [5, 4, 3, 2, 1]:
    insert(tree7, v)
#     5
#    /
#   4
#  /
# 3
# ...
