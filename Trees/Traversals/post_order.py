from Tree import BinaryTree

'GDR'
def post_order(tree: BinaryTree) -> list:
    '''
    '''
    def post_order_rec(tree, liste=[]):
        if tree.is_empty():
            return None
        
        post_order_rec(tree.left(), liste)
        post_order_rec(tree.right(), liste)
        liste.append(tree.get_elem())
        
        return liste
    
    return post_order_rec(tree)

tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)

print(post_order(tree))