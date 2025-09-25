from typing import Dict
from ..tree import Tree

def evaluate(tree: Tree, var_values: Dict[str, float], digits: int = -1) -> float:
    """
        :pre: tree est un arbre syntaxique valide et non vide,
              var_values contient en clé toutes les variables présentes dans l'arbre
        :return: le résultat de l'évaluation de l'arbre
        :post: Les valeurs pour les variables sont prises dans var_values,
               var_values["x"] est donc la valeur (float) de la variable x.
               Toutes les valeurs numériques sont arrondies à 'digits' décimales,
               sauf si 'digits' est négatif (pas d'arrondi).
    """
    from math import log, exp
    variables = var_values
    variables["log"] = log
    variables["exp"] = exp

    def evaluate_tree(tree: Tree, variables, digits):
        tree_values = ""
        def recursive(tree: Tree, tree_values, variables, digits):
            
            if len(tree.children) == 0:
                if tree.value in variables:
                    return str(eval(str(tree.value), variables))
                else:
                    return str(tree.value)
            
            if digits > 0:
                if len(tree.children) == 2:
                    tree_values += '(' + str(round(eval(str(recursive(tree.children[0], tree_values, variables, digits)) + tree.value + str(recursive(tree.children[1], tree_values, variables, digits)), variables), digits)) + ')'
                else:
                    if "log" in tree.value or "exp" in tree.value:
                        tree_values += '(' + str(round(eval(tree.value + '(' + str(recursive(tree.children[0], tree_values, variables, digits)) + ')', variables), digits)) + ')'
                    elif "neg" in tree.value:
                        tree_values += '(' + str(round(eval('-' + str(recursive(tree.children[0], tree_values, variables, digits)), variables), digits)) + ')'
            else:
                if len(tree.children) == 2:
                    tree_values += '(' + str(eval(str(recursive(tree.children[0], tree_values, variables, digits)) + tree.value + str(recursive(tree.children[1], tree_values, variables, digits)), variables)) + ')'
                else:
                    if "log" in tree.value or "exp" in tree.value:
                        tree_values += '(' + str(eval(tree.value + '(' + str(recursive(tree.children[0], tree_values, variables, digits)) + ')', variables)) + ')'
                    elif "neg" in tree.value:
                        tree_values += '(' + str(eval('-' + str(recursive(tree.children[0], tree_values, variables, digits)), variables)) + ')'
                
                        
            return tree_values
        
        tree_values = recursive(tree, tree_values, variables, digits)
        if '(' in tree_values:
            return float(tree_values.split('(')[1][:-1])
        else:
            return tree_values

    variables = var_values
    operations = float(evaluate_tree(tree, variables, digits))

    return operations