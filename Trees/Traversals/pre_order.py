from Tree import BinaryTree

def preoder(tree: BinaryTree) -> list:
    '''
    '''
    def viens_la_mon_gars(tree, liste=[]):
        if tree.is_empty(): 
            return None
        
        liste.append(tree.get_elem())
        viens_la_mon_gars(tree.left(), liste)
        viens_la_mon_gars(tree.right(), liste)
        
        return liste
    
    return viens_la_mon_gars(tree)

tree = BinaryTree(1)
tree.left_tree = BinaryTree(2)
tree.right_tree = BinaryTree(3)

print(preoder(tree))