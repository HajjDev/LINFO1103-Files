from Tree import BinaryTree 

def is_balanced(tree: BinaryTree) -> bool:
    """
    pre: tree est un BinaryTree
    post: retourne True si l’arbre est équilibré (différence de hauteur ≤ 1 entre sous-arbres gauche et droit),
          False sinon
    """
    def is_balanced_rec(tree):
        if tree.is_empty(): return [True, 0]
        
        left_subtree = is_balanced_rec(tree.left())
        right_subtree = is_balanced_rec(tree.right())
        is_balanced = left_subtree[0] and right_subtree[0] and abs(left_subtree[1] - right_subtree[1]) <= 1
        
        return [is_balanced, 1 + max(left_subtree[1], right_subtree[1])]

    return is_balanced_rec(tree)[0]

# Test 1 : arbre vide
t1 = BinaryTree()
print(is_balanced(t1))  # True

# Test 2 : un seul nœud
t2 = BinaryTree(10)
print(is_balanced(t2))  # True

# Test 3 : arbre équilibré de 3 nœuds
t3 = BinaryTree(10)
t3.setleft(BinaryTree(5))
t3.setright(BinaryTree(15))
print(is_balanced(t3))  # True

# Test 4 : arbre déséquilibré à droite (hauteur droite = 2, gauche = 0)
t4 = BinaryTree(10)
right = BinaryTree(15)
right.setright(BinaryTree(20))
t4.setright(right)
print(is_balanced(t4))  # False

# Test 5 : arbre déséquilibré à gauche (hauteur gauche = 3, droite = 0)
t5 = BinaryTree(10)
l1 = BinaryTree(8)
l2 = BinaryTree(6)
l3 = BinaryTree(4)
l2.setleft(l3)
l1.setleft(l2)
t5.setleft(l1)
print(is_balanced(t5))  # False

# Test 6 : arbre presque équilibré (hauteur gauche = 2, droite = 1)
t6 = BinaryTree(10)
gauche = BinaryTree(5)
gauche.setleft(BinaryTree(3))
t6.setleft(gauche)
t6.setright(BinaryTree(15))
print(is_balanced(t6))  # True

# Test 7 : arbre complètement déséquilibré (ligne droite)
t7 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n5 = BinaryTree(5)
n4.setright(n5)
n3.setright(n4)
n2.setright(n3)
t7.setright(n2)
print(is_balanced(t7))  # False
