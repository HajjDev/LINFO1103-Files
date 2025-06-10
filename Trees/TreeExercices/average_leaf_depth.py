from Tree import BinaryTree

def average_leaf_depth(tree: BinaryTree) -> float:
    """
    pre: tree est un BinaryTree
    post: retourne la moyenne des profondeurs des feuilles, 0 si arbre vide
    """
    def get_leaves_depths(tree, depths_list, depth):
        if tree.is_empty():
            return
        
        if tree.right().is_empty() and tree.left().is_empty():
            depths_list.append(depth)
            return depths_list
        
        get_leaves_depths(tree.left(), depths_list, depth + 1)
        get_leaves_depths(tree.right(), depths_list, depth + 1)
        return depths_list
    
    depths =  get_leaves_depths(tree, [], 0)
    return sum(depths) / len(depths)


#       1
#        \
#         2
#          \
#           3

# Feuille : 3 (depth=2)

tree = BinaryTree(1)
tree.right_tree = BinaryTree(2)
tree.right().right_tree = BinaryTree(3)

print(average_leaf_depth(tree))  # 2.0

#        5
#       / \
#      3   7

tree = BinaryTree(5)
tree.left_tree = BinaryTree(3)
tree.right_tree = BinaryTree(7)

print(average_leaf_depth(tree))  # (1 + 1) / 2 = 1.0

#           1
#         /   \
#        2     3
#       / \     \
#      4   5     6
#                 \
#                  7

# Feuilles : 4 (depth=2), 5 (2), 7 (3)

tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)
tree.left().left_tree = BinaryTree(4)
tree.left().right_tree = BinaryTree(5)
tree.right().right_tree = BinaryTree(6)
tree.right().right().right_tree = BinaryTree(7)

print(average_leaf_depth(tree))  # (2 + 2 + 3) / 3 = 2.33

