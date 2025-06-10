from Tree import BinaryTree

def preoder(tree: BinaryTree) -> list:
    '''
    '''
    def pre_order_rec(tree, liste=[]):
        if tree.is_empty(): 
            return None
        
        liste.append(tree.get_elem())
        pre_order_rec(tree.left(), liste)
        pre_order_rec(tree.right(), liste)
        
        return liste
    
    return pre_order_rec(tree)

tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)

print(preoder(tree))