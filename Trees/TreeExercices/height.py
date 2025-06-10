from Tree import BinaryTree

'GDR'
def height(tree: BinaryTree) -> list:
    '''
    '''
    if tree.is_empty():
        return -1

    return 1 + max(height(tree.left()), height(tree.right()))

tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)

print(height(tree))