#! /usr/bin/python3

class List:
    def __init__(self, elem=None):
        """
        pre:  -
        post: initialize a new List with `elem` as first element,
              if `elem` is None, this is interpreted as an empty List
        """
        self.first_elem = elem   # Element in first position
        if elem is not None:
            self.tail_list = List()  # Tail list of the current List
        else:
            self.tail_list = None

    def head(self):
        """
        pre: current List is not empty
        post: return the first element of the current List
        """
        if self.is_empty():
            raise RuntimeError('Cannot get first element from an empty List')
        return self.first_elem

    def tail(self):
        """
        pre: current List is not empty
        post: return the tail List of the current List
        """
        if self.is_empty():
            raise RuntimeError('Cannot get tail List from an empty List')
        return self.tail_list

    def is_empty(self):
        """
        pre: -
        post: return True if the List is empty, False otherwise
        """
        return self.first_elem is None

    def concat(self, elem):
        """
        pre: `elem` is not None
        post: return a new List with `elem` in first position
              and the current List as tail
        """
        if elem is None:
            raise RuntimeError('Cannot concat a None element')
        newlist = List(elem=elem)
        newlist.tail_list = self
        return newlist

    def __str__(self):
        """
        pre: -
        post: return the List content as a string
        """
        if self.is_empty():
            return '[]'
        return '['+ str(self.head()) + str(self.tail()) +']'


def cum_sum_rec(l: List):
    """
    Calcule la liste des sommes cumulées des éléments de `l`
    par récursion
    pre: -
    post: retourne une liste dont le `i`^ième élément est la somme
        des `i` premiers éléments de `l`
    """
    def aux_sum_rec(ls, cumul = 0):
        if ls.is_empty():
            return List()
        
        cumul += ls.head()
        return aux_sum_rec(ls.tail(), cumul).concat(cumul)

    return aux_sum_rec(l)




#Exemple de test:
l = List()
l = l.concat(5)
l = l.concat(4)
l = l.concat(3)
l = l.concat(2)
l = l.concat(1)
cm = cum_sum_rec(l)
if not isinstance(cm, List):
    print("Erreur avec cum_sum : doit renvoyer une List")
elif cm.is_empty():
    print("Erreur avec cum_cum : la List ne devrait pas être vide")
else:
    if not cm.head() == 1:
        print("Erreur avec cum_sum. Le premier élement devrait être 1.")
    if not cm.tail().head() == 3:
        print("Erreur avec cum_sum. Le second élément devrait être 3.")

