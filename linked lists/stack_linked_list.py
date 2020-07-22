# Using linked list to implement a stack class
# importing the LinkedList class 
from question_one import LinkedList

# The Stack class 
class Stack:
    def __init__(self):
        self.stack = LinkedList()
        # The tail is the top of the stack
        # The head is the base of the stack

    # Time Complexity => O(n) following the time and space complexity of the Singly Linked List to print the nodes
    # Space Complexity => O(n)
    def __str__(self):        
        return self.stack.__str__()

    # Method which checks whether the stack is empty or not
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def isEmpty(self):
        return self.stack.isEmpty()

    # Method which adds a new value/item at the top of the stack 
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def push(self, item):
        self.stack.append(item)

    # Method which removes the element at the top of the stack 
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def pop(self):
        self.stack.pop()
    
     # Method which returns the value at the top of the stack
     # Time Complexity => O(1)
    # Space Complexity => O(1)
    def peek(self):
        return self.stack.tailNode()
    
    # Method returning the size of the stack
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def size(self):
        return self.stack.size()
    
    # Method which returns the value of a specific index
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def access(self, i):
        return self.stack.index(i)

    # Method returning True if an item is in the stack, False otherwise
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def search(self, item):
        return self.stack.search(item)
    
    # Method that inserts an item in a specific index in the stack
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def insert(self, item, i):
        self.stack.insert(item, i)
    
    # Method that deletes an item in a specific index in the stack
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def delete(self, item):
        self.stack.delete(item)

        
    
