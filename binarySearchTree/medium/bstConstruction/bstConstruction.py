# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 13.06.2023

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int):
        """ insert value in tree at
            correct position use the 
            property of the bst that
            the left child is smaller
            and the right child is bigger
        Args:
            param1(int): vakue
        Return: self
        """
        if value > self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        
        return self

    def contains(self, value: int):
        """ check if value is in tree  
        if  yes return True else False 
        Args:
            param1(int): value
        """

        if value == self.value:
            return True
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
    


    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self




if __name__ == "__main__":
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    insert = root.insert(12)
    contains = root.contains(15)
    import pdb; pdb.set_trace()
    # root.right.left.left.value == 12)