from Tree import BinaryTree

def inorder(tree: BinaryTree) -> list:
    '''
    '''
    def inorder_rec(tree, liste=[]):
        if tree.is_empty():
            return
        
        inorder_rec(tree.left(), liste)
        liste.append(tree.get_elem())
        inorder_rec(tree.right(), liste)
        
        return liste
    
    return inorder_rec(tree)

tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)

print(inorder(tree))