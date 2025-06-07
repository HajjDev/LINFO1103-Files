from Tree import BinaryTree

def search_parent_bst(tree, key, res=None):
    """
    pre: 'tree' une instance de BinaryTree vérifiant l'invariant d'un ABR
         'key' une clé présente ou pas dans l'ABR
         'res' mémorise un résultat temporaire, initialisé à None par défaut
    post: renvoie le (sous-)arbre enraciné au noeud parent de la première occurrence de 'key' dans 'tree', renvoie un arbre vide si 'key' n'appartient pas à 'tree'.
          renvoie None si la première occurrence de 'key' est à la racine et n'a donc pas de parent.
          La complexité temporelle de cette méthode doit être en O(h) où h est la hauteur de l'ABR.
          L'arbre `tree`, passé en argument, ne peut *pas* être modifié.
    """
    if tree.get_elem() == key: return None
    def rec(tree, key, res):
        if tree.is_empty(): return tree
        
        if tree.get_elem() == key:
            return res
        elif tree.get_elem() > key:
            return rec(tree.left(), key, tree)
        
        return rec(tree.right(), key, tree)