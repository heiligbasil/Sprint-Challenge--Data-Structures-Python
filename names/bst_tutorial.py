# https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
class B_S_T:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = B_S_T(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = B_S_T(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # This method to compare the value with nodes
    def find_val(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return False # str(lkpval) + " Not Found"
            return self.left.find_val(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return False # str(lkpval) + " Not Found"
            return self.right.find_val(lkpval)
        else:
            return True # print(str(self.data) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()
