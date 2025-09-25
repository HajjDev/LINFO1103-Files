from ..tree import Tree

def serialize(tree: Tree) -> str:
    """ Crée une représentation parenthésée de l'arbre, via un parcours préfixe
    :pre: tree est un Tree valide
    :return: une représentation parenthésée (préfixe) de l'arbre, avec ',' comme séparateur
    """
    if tree.is_empty():
        return ""
    out = ''
    if not tree.is_leaf():
        out += '('
    out += f'{tree.value}'
    for child in tree.children:
        out += ','
        out += serialize(child)
    if not tree.is_leaf():
        out += ')'
    return out
