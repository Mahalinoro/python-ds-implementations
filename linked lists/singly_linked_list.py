# Linked Lists (with a tail reference) + relevant primary methods

# Node Class
class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = None

    # Method which returns the value of a node
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def getValue(self):
        return self.value

    # Method which returns the next node
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def getNext(self):
        return self.next

    # Method which set a new value to the current node value
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def setValue(self, newval):
        self.value = newval

    # Method which set the next node value to a new value
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def setNext(self, newval):
        self.next = newval

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Method returning the head node
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def headNode(self):
        if self.head == None:
            return None
        else:
            return self.head.getValue()

    # Method returning the tail node
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def tailNode(self):
        if self.tail == None:
            return None
        else:
            return self.tail.getValue()

    # Method checking whether the linked list is empty or not
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def isEmpty(self):
        return self.head == None

    # Method returning all the nodes within the Linked List
    # Time Complexity => O(n) because the worst case implies traversing each elements depending on the size of the linked list
    # Space Complexity => O(n) because it stores the nodes into a list values which can be n size
    def __str__(self):
        values = []

        currentNode = self.head
        while currentNode:
            values.append(currentNode.value)
            currentNode = currentNode.getNext()
        return " => ".join(map(str, values))

    # Method transforming the value as the head and the current head as the 2nd node
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def prepend(self, value): 
        newNode = Node(value)
        currentNode = self.head

        if self.head == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    # Method transforming the value as the tail and the current tail become the 2nd last node
    # Time Complexity => O(n) since we don't know the previous node, it needs to traverse through each node
    # Space Complexity => O(1)
    def append(self, value):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = newNode
        self.tail = newNode                       
                
    
    # Method transforming the 2nd node to become the head
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def popFirst(self):
        currentHead = self.head
        self.head = currentHead.getNext()

    # Method transforming the 2nd last node to become the tail
    # Time Complexity => O(n) since the previous node is now know, it has to traverse until it reaches the tail
    # Space Complexity => O(1)
    def pop(self):
        previousNode = None
        currentNode = self.head
        while currentNode.next:
            previousNode = currentNode
            currentNode = currentNode.next
        self.tail = previousNode

        previousNode.next = None
        currentNode = None

    # Method returning the size of the Linked List
    # Time Complexity => O(n) because it has to traverse untill it reaches the tail
    # Space Complexity => O(1) because it is only a simple variable
    def size(self):
        currentNode = self.head
        size = 0
        while currentNode != None:
            size += 1
            currentNode = currentNode.getNext()

        return size
    
    # Method accessing the value of a specific index in the Linked List
    # Time Complexity => O(n) if the index is out of reach
    # Space Complexity => O(1)
    def index(self, index):
        currentNode = self.head
        count = 0

        while currentNode:
            count += 1
            if count == index:
                return currentNode.getValue()
            else:
                currentNode = currentNode.getNext()
        
    # Method checking wether a value is in the Linked List or not, returning True if found, false otherwise
    # Iterative Method
    # Time Complexity => O(n) if the node is not in the linked list
    # Space Complexity => O(1)
    def search(self, value):
        currentNode = self.head
        found = False

        while currentNode is not None and not found:
            if currentNode.getValue() == value:
                found = True
                return found
            else:
                currentNode = currentNode.getNext()
        if not found:
            return 'Value not present in the List'     

    # Method checking wether a value is in the Linked List or not, returning True if found, false otherwise
    # Recursive Method
    # Time Complexity => O(n)
    # Space Complexity => O(n)
    def searchR(self, head, value):
        if head == None:
            return False
        
        elif head.getValue() == value:
            return True

        return self.searchR(head.next, value)     


    # Method inserting a value at a specific index
    # Time Complexity => O(n) if it has to traverse until the tail and we do not know about the previous Node
    # Space Complexity => O(1)
    def insert(self, value, index):
        newNode = Node(value)
        currentNode = self.head
        previousNode = None
        count = 0

        if self.head == None:
            self.head = newNode         

        elif index == 0 or index == 1:
            newNode.setNext(self.head)
            self.head = newNode

        else:
            while currentNode:
                count += 1              

                if count == index - 1:
                    previousNode = currentNode
                    nextNode = previousNode.next
                    currentNode.next = newNode
                    newNode.next = nextNode
                    return count
                else:
                    currentNode = currentNode.getNext()    

    # Method deleting a value in the Linked List
    # Time Complexity => O(n) since the previous Node is unknown, it has to traverse through the linked list
    # Space Complexity => O(1)
    def delete(self, value):
        currentNode = self.head
        previousNode = None
        found = False

        while not found:
            if currentNode.getValue() == value:
                found = True
            else:
                previousNode = currentNode
                currentNode = currentNode.getNext()

        if previousNode == None:
            self.head = currentNode.getNext()
        else:
            previousNode.setNext(currentNode.getNext())          
