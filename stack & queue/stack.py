# Implementation of a Stack class 

class Stack:
    def __init__(self):
        self.stack = []
        # The top = last element of the list
        # The base = first element of the list
    def __str__(self):
        return self.stack

    # Method which checks whether the stack is empty or not
    # Time Complexity => O(1) 
    # Space Complexity => O(1) since the stack is unchanged
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

    # Method which adds a new value/item at the top of the stack
    # Time Complexity => O(1)
    # Space Complexity => +1 to the initial size of the stack  (n+1)
    def push(self, item):
        self.stack.append(item)
        return self.stack

    # Method which removes the element at the top of the stack
    # Time Complexity => O(1) since pop() is removing the top/last element
    # Space Complexity => -1 to the initial size of the stack (n-1) 
    def pop(self):
        return self.stack.pop()
        

    # Method which returns the value at the top of the stack
    # Time Complexity => O(1) since it returns the value at the last index/the top
    # Space Complexity => O(1) since the size of the stack is unchanged
    def peek(self):
        return self.stack[-1]

    # Method returning the size of the stack
    # Time Complexity => O(n) depending on the size of the stack
    # Space Complexity => O(1) since the size of the stacl is unchanged
    def size(self):
        return len(self.stack)

    # Method which returns the value of a specific index 
    # Time Complexity => O(1) 
    # Space Complexity => O(1) - stack size is unchanged
    def access(self, index):
        return self.stack[index]



# Function that returns True if an item is in the stack, False otherwise
# Time Complexity => O(n) since the worst case is if the stack is not empty and the item may not be in the stack
# Space Complexity => O(1) - the size of the stack is unchanged
def search(stack, item):
    if stack.isEmpty() == False:
        for i in range(stack.size()):
            if stack.access(i) == item:
                return True
        return False
    else:
        return "The stack is empty"

# Function that reverses the stack
# Time Complexity => O(n) since it depends on the size of the stack if it is not empty
# Space Complexity => O(n) - a new stack has been introduced to stores the reversed stack
def reverse(stack, newStack):
    if stack.isEmpty() == False:
        for i in range(stack.size()-1, -1, -1): # Loop from the top of the stack, then add each element to the new stack
            newStack.push(stack.access(i))
        return newStack.__str__()
    else:
        return "The stack is empty"
    
# Function that inserts an item in a specific index in the stack
# Time Complexity => O(n) 
# Space Complexity => O(n) - a new stack is used to store the values of the initial stack
def insert(stack, item, index, newStack):
    for i in range(stack.size()-1, index-1, -1): # The loop is starting from the top until the element after the index
        newStack.push(stack.access(i)) # With push, those elements will be added to the new stack
        stack.pop() # Then, pop those elements in the initial stack

    stack.push(item) # Push the new item at the top of the stack

    for j in range(newStack.size()-1, -1, -1): # In the new stack, starting from the top and ends at the base of the stack
        stack.push(newStack.access(j)) # Then, pushes those elements in the stack 
        newStack.pop() # Empty the newStack
    
    return stack.__str__()

# Function that deletes an item in a specific index in the stack
# Time Complexity => O(n) 
# Space Complexity => O(n) - a new stack is used to store the values of the initial stack
# It follows the same principle as insert but the difference is in the first loop where it ends at the index and the pop operation 
def delete(stack, index, newStack):
    for i in range(stack.size()-1, index, -1):
        newStack.push(stack.access(i))
        stack.pop()

    stack.pop()

    for j in range(newStack.size()-1, -1, -1):
        stack.push(newStack.access(j))
        newStack.pop()
    return stack.__str__()




