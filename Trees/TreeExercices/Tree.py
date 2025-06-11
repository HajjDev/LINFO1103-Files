class BinaryTree:
    def __init__(self, elem: int = None):
        """
        pre:  -
        post: initialize a new Binary Tree with "elem" stored at the root node,
              when "elem" is None, this is interpreted as an empty BinaryTree
        """
        self.elem = elem   # A value at the root of the current tree
        if elem is not None:
            self.left_tree = BinaryTree()   # A reference to the left subtree
            self.right_tree = BinaryTree()  # A reference to the right subtree
        else:
            self.left_tree = None
            self.right_tree = None

    def is_empty(self):
        """
        pre: -
        post: return a boolean True if the BinaryTree is empty, False otherwise
        """
        return self.elem is None

    def get_elem(self):
        """
        pre: current Tree is not empty
        post: return the elem stored at the root of the current Tree
        """
        if self.is_empty():
            raise RuntimeError('Cannot get the root elem from an empty tree')
        return self.elem

    def left(self):
        """
        pre: current Tree is not empty
        post: return the left subtree of the current BinaryTree
        """
        if self.is_empty():
            raise RuntimeError('Cannot get the left subtree of an empty tree')
        return self.left_tree

    def right(self):
        """
        pre: current Tree is not empty
        post: return the right subtree of the current BinaryTree
        """
        if self.is_empty():
            raise RuntimeError('Cannot get the right subtree of an empty tree')
        return self.right_tree
    
    def setelem(self, elem):
        """
        pre: elem is not None
        post: the root element of the current BinaryTree is set to elem
        """
        if elem is None:
            raise RuntimeError('setelem requires "elem" to be different from None')
        self.root_elem = elem
        
    def setright(self, tree):
        """
        pre: -
        post: the right subtree of the current BinaryTree is set to "tree"
        """
        if not isinstance(tree, BinaryTree):
            raise RuntimeError('setright requires "tree" to be a BinaryTree')
        self.right_tree = tree
    
    def setleft(self, tree):
        """
        pre: -
        post: the left subtree of the current BinaryTree is set to "tree"
        """
        if not isinstance(tree, BinaryTree):
            raise RuntimeError('setleft requires "tree" to be a BinaryTree')
        self.left_tree = tree