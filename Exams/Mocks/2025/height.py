def height(tree):
    """
    pre: `tree` est un `BinaryTree`
    post: renvoie la hauteur de l'arbre,
          renvoie '-1' si l'arbre est vide.
          L'arbre `tree`, passé en argument, ne peut *pas* être modifié.
    """
    if tree.is_empty(): return -1

    right = height(tree.right())
    left = height(tree.left())

    return 1 + max(right, left)