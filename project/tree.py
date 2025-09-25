from typing import Union, List

class Tree:
    """ Un arbre syntaxique """
    OPERATORS_1 = {'log', 'exp', 'neg'}         # 1 opérande
    OPERATORS_2 = {'+', '-', '*', '/', '**'}    # 2 opérandes
    OPERATORS = OPERATORS_1 | OPERATORS_2

    def __init__(self, value: Union[str,float,int] = None, children: List["Tree"] = ()):
        """
        :pre: value est None, auquel cas l'arbre est vide (le cas par défaut),
              ou, sinon, value (à la racine) est un str, un float ou un int, et children est une liste de Tree.
        :post: l'arbre résultant est valide. si value est un int, elle est convertie en float.
        """
        if not children:
            children = []
        self.value = float(value) if isinstance(value, int) else value
        self.children = children
        assert self.is_valid(), "l'arbre courant est invalide"

    def is_empty(self):
        """
        :pre: -
        :return: True si l'arbre courant correspond à un arbre vide
        """
        return self.value is None

    def is_leaf(self):
        """
        :pre: -
        :return: True si l'arbre courant est une feuille. False sinon.
        """
        return len(self.children) == 0

    def is_variable(self):
        """
        :pre: -
        :return: True si l'arbre courant représente une variable. False sinon.
        """
        return self.is_leaf() and isinstance(self.value, str) and self.value.isalpha()

    def is_constant(self):
        """
        :pre: -
        :return: True si l'arbre courant représente une constante. False sinon.
        """
        return self.is_leaf() and isinstance(self.value, float)

    def is_operation(self):
        """
        :pre: -
        :return: True si l'arbre courant représente une opération valide. False sinon.
        """
        if self.value == '**':
            return (len(self.children) == 2
                    and self.children[1].is_constant())
        if len(self.children) == 1:
            return self.value in self.OPERATORS_1
        elif len(self.children) == 2:
            return self.value in self.OPERATORS_2
        else:
            return False

    def is_valid(self):
        """
        :pre: -
        :return: True si l'arbre courant (la racine et ses enfants, récursivement) est valide. False sinon.
        """
        if self.is_empty():
            # self.children doit être la liste vide si l'arbre courant est vide
            return not self.children
        if not self.is_variable() and not self.is_constant() and not self.is_operation():
            return False
        for child in self.children:
            if not child.is_valid():
                return False
        return True

    def __repr__(self):
        """ Donne une représentation textuelle et visuelle de l'arbre, pour le debugging """
        if self.is_empty():
            return ""
        out = f"{self.value}"
        for c in self.children:
            c_repr = repr(c).split("\n")
            out += "\n|> " + c_repr[0]
            if len(c_repr) > 1:
                out += "\n" + "\n".join(["|  " + l for l in c_repr[1:]])
        return out

    def __str__(self):
        """ Donne une représentation textuelle et visuelle de l'arbre, pour le debugging """
        return repr(self)

    def __eq__(self, other):
        """
        :return: True si self et other ont la même structure
        """
        if not isinstance(other, Tree):
            return False
        return self.value == other.value and self.children == other.children