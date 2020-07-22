# Implementation of a Queue class

class Queue:
    def __init__(self):
        self.queue = []
        # The front is the first element
        # The rear is the last element

    def __str__(self):
        return self.queue

    # Method which checks whether the queue is empty or not
    # Time Complexity => O(1) 
    # Space Complexity => Same as the initial queue since there is no new introduced variable
    def isEmpty(self):
        if self.queue == []:
            return True
        else:
            return False

    # Method which adds a new value/item at the rear of the queue
    # Time Complexity => O(1)
    # Space Complexity => +1 to the initial size of the queue  (n+1)
    def enqueue(self, val):
        self.queue.append(val)
        return self.queue

    # Method which removes the front of the queue
    # Time Complexity => O(1) since pop is removing the element at the very beginning
    # Space Complexity => -1 to the initial size of the queue (n-1) 
    def dequeue(self):
        return self.queue.pop(0)

    # Method returning the size of the queue
    # Time Complexity => O(n) depending on the size of the queue
    # Space Complexity => O(1) since the size of the queue is unchanged
    def size(self):
        return len(self.queue)

    # Method which returns the value at the front of the queue
    # Time Complexity => O(1) since it returns the value at the first index
    # Space Complexity => O(1) since the size of the queue is unchanged
    def peek(self):
        return self.queue[0]

    # Method which returns the value of a specific index 
    # Time Complexity => O(1) 
    # Space Complexity => O(1) queue size is unchanged
    def access(self, index):
        return self.queue[index]


# Function that returns True if an item is in the queue, False otherwise
# Time Complexity => O(n) since the worst case is if the queue is not empty and the item may not be in the queue
# Space Complexity => O(1) - the size of the queue is unchanged
def search(queue, item):
    if queue.isEmpty() == False:
        for i in range(queue.size()):
            if queue.access(i) == item:
                return True
        return False
    else:
        return "The queue is empty"


# Function that reverses the queue
# Time Complexity => O(n) since it depends on the size of the queue if it is not empty
# Space Complexity => O(n) - a new queue has been introduced to stores the reversed queue
def reverse(queue, newQueue):
    if queue.isEmpty() == False:
        for i in range(queue.size()-1, -1, -1): # It loops through the queue starting from the rear and ends at the front
            newQueue.enqueue(queue.access(i))
        return newQueue.__str__()
    else:
        return "The queue is empty"


# Function that inserts an item in a specific index in the queue
# Time Complexity => O(n) 
# Space Complexity => O(n) - a new queue is used to store the values of the initial queue
def insert(queue, newQueue, item, index):
    if queue.isEmpty() == False:
        for i in range(0, index): # The loop starts from the front until the index location
            newQueue.enqueue(queue.access(i)) # Then, adds those values in the new list
            
        for j in range(0, index): # The same loop again, then dequeue the elements from 0 to index
            queue.dequeue()  # Putting this queue.dequeue in the first loop will give us an unexpected output

        newQueue.enqueue(item) # Then, adds with enqueue method the new item to the new queue

        for n in range(queue.size()): # This loop through the rest of the element in the initial queue
            newQueue.enqueue(queue.access(n)) # Then, enqueue the rest of the elements to the new queue
        
        return newQueue.__str__()
    else:
        return "The queue is empty"

    
# Function that deletes an item in a specific index in the queue
# Time Complexity => O(n) 
# Space Complexity => O(n) - a new queue is used to store the values of the initial queue
# It follows the same principle as insert but the difference is the operation after the second loop
def delete(queue, newQueue, index):
    if queue.isEmpty() == False:
        for i in range(0, index):
            newQueue.enqueue(queue.access(i))

        for j in range(0, index):
            queue.dequeue()

        queue.dequeue() 

        for n in range(queue.size()):
            newQueue.enqueue(queue.access(n))
        
        return newQueue.__str__()
    else:
        return "The queue is empty"

