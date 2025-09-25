from ..tree import Tree
from .evaluate import evaluate
from .simplify import simplify

def derivate(tree: Tree, var: str) -> Tree:
    """
    :pre: tree est un arbre syntaxique valide et non vide
    :return: un arbre correspondant à la dérivée (symbolique) de l'arbre original,
             par rapport à la variable `var`.
    :post: l'arbre original n'est *pas* modifié, un nouvel arbre (dérivé) est renvoyé.
    """
    import copy
    tree = copy.deepcopy(tree)
    
    def recursive(tree, var):
        if tree.is_leaf():
            return Tree(1.0) if tree.value == var else Tree(0.0)
        elif tree.is_operation():
            if tree.value in ["+", "-"]: tree = Tree(tree.value, [recursive(tree.children[0], var), recursive(tree.children[1], var)])   
            elif tree.value == "*": tree = Tree("+", [Tree("*", [tree.children[0], recursive(tree.children[1], var)]), Tree("*", [recursive(tree.children[0], var), tree.children[1]])])
            elif tree.value == "/": tree = Tree("/", [Tree("-", [Tree("*", [tree.children[1], recursive(tree.children[0], var)]), Tree("*", [tree.children[0], recursive(tree.children[1], var)])]), Tree("**", [tree.children[1], Tree(2.0)])])
            elif tree.value == "**": tree = Tree("*", [Tree("*", [tree.children[1], Tree("**", [tree.children[0], Tree(tree.children[1].value - 1)])]), recursive(tree.children[0], var)])
            elif tree.value == "log": tree = Tree("*", [Tree("/", [Tree(1.0), tree.children[0]]), recursive(tree.children[0], var)])
            elif tree.value == "exp": tree = Tree("*", [Tree("exp", [tree.children[0]]), recursive(tree.children[0], var)])
            elif tree.value == "neg": tree = Tree("neg", [recursive(tree.children[0], var)])

        return tree

    return recursive(tree, var)