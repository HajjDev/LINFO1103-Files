from Tree import BinaryTree

def search_parent(tree, key, res=None):
    """
    pre: `tree` est une instance de la classe BinaryTree, `key` est une valeur comparable aux éléments de l’arbre
    post: retourne le sous-arbre dont la racine est le parent de la première occurrence de `key` dans `tree`
          - retourne None si `key` est à la racine
          - retourne un arbre vide si `tree` est vide ou si `key` n’apparaît pas
    """

# Exemples d'utilisation de la fonction search_parent avec la classe BinaryTree :

# arbre = BinaryTree(1)
# arbre.left().elem = 2
# arbre.right().elem = 3
# arbre.left().left().elem = 4
# search_parent(arbre, 2) → retourne l’arbre racine avec 1
# search_parent(arbre, 4) → retourne le sous-arbre de racine 2
# search_parent(arbre, 1) → None
# search_parent(BinaryTree(), 42) → arbre vide
