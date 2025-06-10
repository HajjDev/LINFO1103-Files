from Tree import BinaryTree

def count_prime_nodes(tree: BinaryTree) -> int:
    """
    pre: tree est un BinaryTree
    post: retourne le nombre de nœuds dont la valeur est un nombre premier
    """
    def is_prime(number):
        if number == 1: return False
        
        for i in range(2, number):
            if number % i == 0: return False
            
        return True
    
    def count_prime_nodes_rec(tree):
        if tree.is_empty(): return 0
        
        if is_prime(tree.get_elem()): return 1 + count_prime_nodes_rec(tree.left()) + count_prime_nodes_rec(tree.right())
        return count_prime_nodes_rec(tree.left()) + count_prime_nodes_rec(tree.right())
    
    return count_prime_nodes_rec(tree)

# Test 1 - Arbre vide
tree = BinaryTree()
print(count_prime_nodes(tree))  # 0

# Test 2 - Un seul nœud premier
tree = BinaryTree(7)
print(count_prime_nodes(tree))  # 1

# Test 3 - Un seul nœud non premier
tree = BinaryTree(10)
print(count_prime_nodes(tree))  # 0

# Test 4 - Plusieurs nœuds avec plusieurs premiers
#        11
#       /  \
#      4    17
#          /  \
#         6    5
tree = BinaryTree(11)
tree.left_tree = BinaryTree(4)
tree.right_tree = BinaryTree(17)
tree.right().left_tree = BinaryTree(6)
tree.right().right_tree = BinaryTree(5)
print(count_prime_nodes(tree))  # 3 (11, 17, 5)

# Test 5 - Tous les nœuds sont premiers
#        2
#       / \
#      3   5
tree = BinaryTree(2)
tree.left_tree = BinaryTree(3)
tree.right_tree = BinaryTree(5)
print(count_prime_nodes(tree))  # 3

# Test 6 - Aucun nœud premier
#        1
#       / \
#      4   6
tree = BinaryTree(1)
tree.left_tree = BinaryTree(4)
tree.right_tree = BinaryTree(6)
print(count_prime_nodes(tree))  # 0
