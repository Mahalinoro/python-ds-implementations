# Doubly-linked list class 


# The Node class with a prev reference
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

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

    # Method which returns the prev node
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def getPrev(self):
        return self.prev

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
    
    # Method which set the prev node value to a new value
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def setPrev(self, newval):
        self.prev = newval

# The Doubly Linked List class with a tail reference
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Method returning all the nodes within the Linked List
    # Time Complexity => O(n)
    # Space Complexity => O(n)
    def __str__(self):
        values = []

        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return " => ".join(map(str, values))

    # Method checking whether the linked list is empty or not
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def isEmpty(self):
        return self.head == None

    # Method transforming the value as the tail and the current tail become the 2nd last node
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def append(self, value):
        newNode = Node(value)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            currentNode = self.tail
            currentNode.next = newNode
            newNode.prev = currentNode
            self.tail = newNode            

    # Method transforming the value as the head and the current head as the 2nd node
    # Time Complexity => O(1)
    # Space Complexity => o(1)
    def prepend(self, value):
        newNode = Node(value)

        if self.isEmpty():
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode

        self.head = newNode

    # insert(node, prevNode) - insert node after prevNode
    # Time Complexity => O(n) 
    # Space Complexity => O(1)
    def insert(self, prevNode, node): # Edge cases: Not Considering the tail and head [Not working]
        newNode = Node(node)
        currentNode = self.head

        if self.isEmpty():
            self.head = newNode

        else:
            while currentNode:
                if currentNode.next.getValue() == prevNode:
                    previousNode = currentNode.next
                    nextNode = previousNode.next
                    previousNode.next = newNode
                    newNode.next = nextNode
                    newNode.prev = previousNode
                    return
                else:
                    currentNode = currentNode.next

    # delete(node) - delete node from doubly-linked list
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def delete(self, node): # Edge cases: Not Considering the tail and head [Not working]
        currentNode = self.head 

        while currentNode:
            if currentNode.next.getValue() == node:
                previousNode = currentNode
                nextNode = currentNode.next.next
                previousNode.next = nextNode
                # nextNode.prev = previousNode
                return
            else:
                currentNode = currentNode.next



