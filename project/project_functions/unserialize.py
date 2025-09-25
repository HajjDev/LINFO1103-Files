from ..tree import Tree
from ..defined_functions.serialize import serialize

def unserialize(parent_expr) -> Tree:
    """
    :pre: parent_expr est une expression parenthésée en sortie de serialize
    :return: l'arbre qui a été donné à serialize
    :post: pour tout arbre X, on doit avoir que X == unserialize(serialize(X)).
    """
    def to_list(expr) -> list:
        from re import findall
        token_list = expr.replace(' ', '').split(',')
        token_list = [item for tok in token_list for item in findall(r'[()]|[^()]+', tok)]
        
        return token_list

    def create_tree(token_list, index=0) -> Tree:
        tree = Tree()
        index += 1
        tree.value = token_list[index]
        index += 1
        
        while index < len(token_list):
            token = token_list[index]
            if token == '(':
                children, index = create_tree(token_list, index)
                tree.children.append(children)
            elif token == ')':
                index += 1
                return tree, index
            else:
                tree.children.append(Tree(float(token) if not token.isalpha() else token))
                index += 1
        
        return tree, index

    token_list = to_list(parent_expr)
    tree = Tree()
    if len(token_list) == 0:
            return tree
    elif len(token_list) == 1:
        tree.value = float(token_list[0]) if not token_list[0].isalpha() else token_list[0]
        return tree
    else:
        tree, index = create_tree(to_list(parent_expr))
            
    return tree
