class BinarySearchTree:
    """Binary Search Tree, is a node-based binary tree data structure which has the following properties: The left
    subtree of a node contains only nodes with keys lesser than the node’s key. The right subtree of a node contains
    only nodes with keys greater than the node’s key. The left and right subtree each must also be a binary search
    tree. There must be no duplicate nodes """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Insert the given value into the tree. Insert adds the input value
        to the binary search tree, adhering to the rules of the ordering of
        elements in a binary search tree"""
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        """This searches the binary search tree for the input value,
        returning a boolean indicating whether the value exists in the
        tree or not"""
        if self.value == target:
            return True
        if self.value > target:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if self.value <= target:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    def get_max(self):
        """This returns the maximum value in the binary search tree"""
        if self.right is None:
            # No more nodes to the right; found the largest value
            return self.value
        else:
            # Keep traversing the nodes to the right in search of the final one
            return self.right.get_max()
