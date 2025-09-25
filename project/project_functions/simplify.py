from ..tree import Tree
from .evaluate import evaluate
from .unserialize import unserialize

def simplify(tree: Tree, digits: int = -1) -> Tree:
    """
    :pre: tree est un arbre syntaxique valide
    :return: un arbre syntaxique valide, équivalent au premier
    :post: l'arbre renvoyé (et ses sous-arbres, par récursion) est soit réduit à une feuille,
        soit contient un opérateur à sa racine, qui a dans sa descendance au moins une variable.
        l'arbre original passé en paramètre n'est *pas* modifié, un nouvel arbre (simplifié) est renvoyé.
        Les valeurs numériques dans l'arbre simplifié sont arrondies à 'digits' décimales,
        sauf si 'digits' est négatif (le cas par défaut).
    """
    import copy
    simplified_tree = copy.deepcopy(tree)

    def recursive(simplified_tree, digits, left_tree="", right_tree = "", single_value=""):
        if len(simplified_tree.children) == 0: 
            try: simplified_tree.value = round(float(simplified_tree.value), digits) if digits > 0 else float(simplified_tree.value)
            except: pass
            return simplified_tree
        
        if len(simplified_tree.children) == 2:
            try: left_tree = round(float(recursive(simplified_tree.children[0], digits)), digits) if digits > 0 else float(recursive(simplified_tree.children[0]))
            except: left_tree = recursive(simplified_tree.children[0], digits)
            try: right_tree = round(float(recursive(simplified_tree.children[1], digits)), digits) if digits > 0 else float(recursive(simplified_tree.children[1]))
            except: right_tree = recursive(simplified_tree.children[1], digits)
        else:
            single_value = recursive(simplified_tree.children[0], digits)

        if "neg" in simplified_tree.value:
            try: 
                if str(int(simplified_tree.children[0].value)).isdigit(): simplified_tree.value = round(float("-" +  str(simplified_tree.children[0].value)), digits) if digits > 0 else float("-" +  str(simplified_tree.children[0].value)); simplified_tree.children = []
            except: pass
        try:
            left_tree.value = float(left_tree.value)
            right_tree.value = float(right_tree.value)
            simplified_tree.value = evaluate(simplified_tree, {}, digits) if digits > 0 else evaluate(simplified_tree, {})
            simplified_tree.children = []
        except: pass
        
        try:
            single_value.value = float(single_value.value)
            simplified_tree.value = evaluate(simplified_tree, {}, digits) if digits > 0 else evaluate(simplified_tree, {})
            simplified_tree.children = []
        except: pass
        
        if len(simplified_tree.children) == 2:
            if left_tree.value == 0.0 or right_tree.value == 0.0:
                if left_tree.value == 0.0:
                    if simplified_tree.value == "-":
                        simplified_tree.value = "neg"
                        try:
                            if digits > 0: right_tree.value = round(float(right_tree.value), digits)
                            else: right_tree.value = float(right_tree.value)
                            simplified_tree.children = [right_tree]
                        except: 
                            simplified_tree.children = [right_tree]
                    elif simplified_tree.value == "*" or simplified_tree.value == "/": simplified_tree.value = 0.0; simplified_tree.children = []
                    elif simplified_tree.value == "**": simplified_tree.value = 1.0; simplified_tree.children = []
                    else: simplified_tree.value = right_tree; simplified_tree.children = []
                elif right_tree.value == 0.0:
                    if simplified_tree.value == "-": 
                        simplified_tree.value = left_tree; simplified_tree.children = []
        
                    elif simplified_tree.value == "*" or simplified_tree.value == "/": simplified_tree.value = 0.0; simplified_tree.children = []
                    elif simplified_tree.value == "**": simplified_tree.value = 1.0; simplified_tree.children = []
                    else:
                        simplified_tree.value = left_tree; simplified_tree.children = []
            
            elif left_tree.value == 1.0 or right_tree.value == 1.0:
                if left_tree.value == 1.0: 
                    if simplified_tree.value == "*": 
                        try: simplified_tree.value = round(float(right_tree), digits) if digits > 0 else float(right_tree); simplified_tree.children = []
                        except: simplified_tree.value = right_tree; simplified_tree.children = []
                    elif simplified_tree.value == "**":
                        try: simplified_tree.value = round(float(right_tree), digits) if digits > 0 else float(right_tree); simplified_tree.children = []
                        except: simplified_tree.value = right_tree; simplified_tree.children = []
                elif right_tree.value == 1.0: 
                    if simplified_tree.value == "*":
                        try: simplified_tree.value = round(float(left_tree), digits) if digits > 0 else float(left_tree); simplified_tree.children = []
                        except: simplified_tree.value = left_tree; simplified_tree.children = []
                    elif simplified_tree.value == "**":
                        try: simplified_tree.value = round(float(left_tree), digits) if digits > 0 else float(left_tree); simplified_tree.children = []
                        except: simplified_tree.value = left_tree; simplified_tree.children = []
        
        return simplified_tree

    return recursive(simplified_tree, digits)