# BinaryTreeNode and BinaryTree Classes including the primary methods.

class BinaryTreeNode:
    def __init__(self, data):
        self.key = data
        self.right = None
        self.left = None
    
    # Method which return the value of the node
    # Time complexity => O(1)
    # Space complexity => O(1)
    def getValue(self): 
        return self.key

    # Method which return the value of the right child of the parent node
    # Time complexity => O(1)
    # Space complexity => O(1)
    def getRightChild(self):
        return self.right

    # Method which return the value of the left child of the parent node
    # Time complexity => O(1)
    # Space complexity => O(1)
    def getLeftChild(self):
        return self.left

    # Method which set the value of a node to a new value
    # Time complexity => O(1)
    # Space complexity => O(1)
    def setValue(self, newValue):
        self.key = BinaryTreeNode(newValue)
    
    # Method which set the value of the right child to a new value
    # Time complexity => O(1)
    # Space complexity => O(1)
    def setRightChild(self, newRightValue):
        self.right = BinaryTreeNode(newRightValue)
    
    # Method which set the value of the left child to a new value
    # Time complexity => O(1)
    # Space complexity => O(1)
    def setLeftChild(self, newLeftValue):
        self.left = BinaryTreeNode(newLeftValue)  

    
class BinaryTree:
    def __init__(self, key):
        self.root = BinaryTreeNode(key)
    
    # Method which returns the value of the root node
    # Time complexity => O(1)
    # Space complexity => O(1)
    def getRoot(self):
        return self.root
    
    # Method which sets the value of the root node to a new Node
    # Time complexity => O(1)
    # Space complexity => O(1)
    def setRoot(self, newRoot):
        self.root = BinaryTreeNode(newRoot)

    # Method which returns the height of the tree
    # Time complexity => O(n)
    # Space complexity => O(1) with extra temp variables such as countleft and countright
    def height(self):
        countLeft = 0
        countRight = 0

        current = self.root
        # Root to Left
        while current:
            if current.getLeftChild() != None:
                countLeft += 1            
            current = current.getLeftChild()

        # Root to Right
        current = self.root
        while current:
            if current.getRightChild() != None:
                countRight += 1
            current = current.getRightChild()

        if countLeft > countRight:
            return countLeft + 1
        else:
            return countRight + 1