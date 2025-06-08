from Tree import BinaryTree

def inorder(tree: BinaryTree) -> list:
    '''
    '''
    def reste_la_mon_gars(tree, liste=[]):
        if tree.is_empty():
            return
        
        reste_la_mon_gars(tree.left(), liste)
        liste.append(tree.get_elem())
        reste_la_mon_gars(tree.right(), liste)
        
        return liste
    
    return reste_la_mon_gars(tree)

tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)

print(inorder(tree))