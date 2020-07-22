# Class Binary Search Tree Node and Binary Search and primary methods
class BinarySearchTreeNode:
    def __init__(self, data):
        self.key = data
        self.right = None
        self.left = None
    
    def getValue(self): # method returning the value of the node
        return self.key

    def getRightChild(self):  # method returning the value of the right node
        return self.right

    def getLeftChild(self):  # method returning the value of the left node
        return self.left

    def setValue(self, newValue):  # method setting the value of the node to a new value
        self.key = newValue
    
    def setRightChild(self, newRightValue): # method setting the value of the right node to a new value
        self.right = newRightValue
    
    def setLeftChild(self, newLeftValue): # method setting the value of the left node to a new value
        self.left = newLeftValue  

class BinarySearchTree:
    def __init__(self, key):
        self.root = BinarySearchTreeNode(key)
    
    def getRoot(self): # method returning the value of the root node
        return self.root
    
    def setRoot(self, newRoot): # method setting the value of the root node to a new value
        self.root = newRoot

    def insert(self, root, key): # method inserting a new node to the tree
        if root is None:
            self.root = BinarySearchTreeNode(key)
        else:
            if root.getValue() < key:
                if root.right is None:
                    root.right = BinarySearchTreeNode(key)
                else:
                    self.insert(root.right, key)

            else:
                if root.left is None:
                    root.left = BinarySearchTreeNode(key)
                else:
                    self.insert(root.left, key)

    def inOrderTraversal(self, root, llist): # method for in order traversal 
        if root:
            self.inOrderTraversal(root.left, llist)
            llist.append(root.getValue())
            self.inOrderTraversal(root.right, llist)
