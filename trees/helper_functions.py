# Function that inputs a list of lists 
# Returns True if it can form a tree with the root as the first element of the list and each other element a subtree.
# Returns False, otherwise

# Time Complexity => O(n) because it has to go through each list within the list
# Space Complexity => O(n) because all is going to store a list of boolean value everytime it checks each lists
def formTree(llist):
    if type(llist) is not list:
        return False

    if type(llist[0]) is list:
        return False

    else:
        return all(formTree(llist) for llist in llist[1:])

# Function that inputs a list of integers and outputs a Binary Search Tree. 
# Confirm that this works by inputting your BST:
# applying the in-order traversal and seeing that you get back a sorted list of the same integers.

# Time complexity => O(n log n) because we iterate through each element in the list then insert the nodes to the new binary search tree which is log n
# Space complexity => O(n)
def listIntoBinarySearchTree(intlist, llist):
    bst = BinarySearchTree(intlist[0])
    nList = intlist[1:]

    for i in range(len(nList)):
        bst.insert(bst.root, nList[i])
        
    bst.inOrderTraversal(bst.root, llist)


# Algorithm to compute the height of the binary tree.

def height_recursive(binaryTree): # Root of the binary tree
    # If the root of the binary tree is none then return 0
    # Else, find the height recursively for the left subtree
    # Then, find the height recursively for the right subtree
    # Finally, compare the height value of each subtree then return the greatest + 1 [the root]
    if binaryTree is None:
        return 0
    
    else:
        hLeft = height_recursive(binaryTree.left)
        hRight = height_recursive(binaryTree.right)

        if hLeft > hRight:
            return hLeft + 1
        else:
            return hRight + 1
            
# Time complexity => O(n) because it has to check each subtree recursively
# Space complexity => O(1) 

# Following 3 traversal methods (using recursion): 
# Pre-order traversal
# In-order traversal
# Post-order traversal

# Time Complexity => O(n)
# Space Complexity => O(n)
def preOrderTraversal(binaryTree, ilist): # Inputing the root of the binary tree and an empty list to store the values
    if binaryTree != None:
        # root - left - right
        ilist.append(binaryTree.getValue()) 
        preOrderTraversal(binaryTree.left,ilist)
        preOrderTraversal(binaryTree.right, ilist)

# Time Complexity => O(n)
# Space Complexity => O(n)
def inOrderTraversal(binaryTree, ilist): # Inputing the root of the binary tree and an empty list to store the values
    if binaryTree:
        # left - root - right
        inOrderTraversal(binaryTree.left, ilist)
        ilist.append(binaryTree.getValue())
        inOrderTraversal(binaryTree.right, ilist)

# Time Complexity => O(n)
# Space Complexity => O(n)
def postOrderTraversal(binaryTree, ilist): # Inputing the root of the binary tree and an empty list to store the values
    if binaryTree:
        # left - right - root
        postOrderTraversal(binaryTree.left, ilist)
        postOrderTraversal(binaryTree.right, ilist)
        ilist.append(binaryTree.getValue())