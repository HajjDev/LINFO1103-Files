from Tree import BinaryTree

def are_trees_identical(tree1: BinaryTree, tree2: BinaryTree) -> bool:
    """
    pre: `tree1` et `tree2` sont des instances de la classe BinaryTree
    post: retourne True si les deux arbres sont identiques, c’est-à-dire :
          - même structure (organisation des nœuds)
          - mêmes valeurs dans les mêmes positions
          retourne False sinon
    """
    if tree1.is_empty() and tree2.is_empty(): return True
    elif tree1.is_empty() or tree2.is_empty(): return False
    
    if tree1.get_elem() == tree2.get_elem():
        return are_trees_identical(tree1.left(), tree2.left()) and are_trees_identical(tree1.right(), tree2.right())
    
    return False


arbre1 = BinaryTree(1)
arbre1.left_tree = BinaryTree(2)
arbre1.right_tree = BinaryTree(3)

arbre2 = BinaryTree(1)
arbre2.left_tree = BinaryTree(2)
arbre2.right_tree = BinaryTree(3)

arbre3 = BinaryTree(1)
arbre3.left_tree = BinaryTree(3)  # Différent de arbre1 et arbre2
arbre3.right_tree = BinaryTree(2)

print(are_trees_identical(arbre1, arbre2))  # True
print(are_trees_identical(arbre1, arbre3))  # False