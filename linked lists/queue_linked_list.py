# Using a linked list to implement a queue class
# Import LinkedList class
from question_one import LinkedList

# The Queue class
class Queue:
    def __init__(self):
        self.queue = LinkedList()
        # The front is the head of the queue
        # The rear is the tail of the queue
    
    # Time Complexity => O(n)
    # Space Complexity => O(n)
    def __str__(self):
        return self.queue.__str__()

    # Method which checks whether the queue is empty or not
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def isEmpty(self):
        return self.queue.isEmpty()
    
    # Method which adds a new value/item at the rear of the queue
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def enqueue(self, item):
        self.queue.append(item)
    
    # Method which removes the front of the queue
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def dequeue(self):
        self.queue.popFirst()

    # Method returning the size of the queue
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def size(self):
        return self.queue.size()
    
    # Method which returns the value at the front of the queue
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def peek(self):
        return self.queue.headNode()
    
    # Method which returns the value of a specific index 
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def access(self, i):
        return self.queue.index(i)
    
    # Method that returns True if an item is in the queue, False otherwise
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def search(self, item):
        return self.queue.search(item)
    
    # Method that inserts an item in a specific index in the queue
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def insert(self, item, i):
        self.queue.insert(item, i)
    
    # Method that deletes an item in a specific index in the queue
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    def delete(self, item):
        self.queue.delete(item)