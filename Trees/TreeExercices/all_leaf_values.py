from Tree import BinaryTree

def all_leaf_values(tree: BinaryTree) -> list:
    """
    pre: tree est un BinaryTree
    post: retourne une liste contenant les valeurs de toutes les feuilles
    """
    def all_leaf_values_rec(tree, leaves):
        if tree.is_empty():
            return leaves
        
        if tree.left().is_empty() and tree.right().is_empty():
            leaves.append(tree.get_elem())
            return leaves
        
        all_leaf_values_rec(tree.left(), leaves)
        all_leaf_values_rec(tree.right(), leaves)
        return leaves
    
    return all_leaf_values_rec(tree, [])

empty_tree = BinaryTree()
print(all_leaf_values(empty_tree))  # Attendu: []

single_node = BinaryTree(1)
print(all_leaf_values(single_node))  # Attendu: [1]

one_child = BinaryTree(1)
one_child.right_tree = BinaryTree(2)
print(all_leaf_values(one_child))  # Attendu: [2]

tree = BinaryTree(10)
tree.left_tree = BinaryTree(5)
tree.right_tree = BinaryTree(15)
tree.left_tree.left_tree = BinaryTree(2)
tree.left_tree.right_tree = BinaryTree(7)
tree.right_tree.left_tree = BinaryTree(12)
tree.right_tree.right_tree = BinaryTree(20)
print(all_leaf_values(tree))  # Attendu: [2, 7, 12, 20]

unbalanced = BinaryTree(1)
unbalanced.left_tree = BinaryTree(2)
unbalanced.left_tree.left_tree = BinaryTree(3)
print(all_leaf_values(unbalanced))  # Attendu: [3]