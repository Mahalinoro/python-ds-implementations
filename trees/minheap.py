# minHeapCheck function takes a list of integers as input
# It returns True if it is a min heap (parents are always less than children) and False if not. 
# Time Complexity =>
# Space Complexity => 

def minHeapCheck(intList, index=1):
    # Check if it has only one node, if yes, then returns true
    if (2*index) > (len(intList) - 1):
        return True
    
    # Check if the root as a left child then check if it is a min heap
    left = (intList[index] <= intList[2*index]) and minHeapCheck(intList, 2*index)
    # Check if the root as a right child then check if it is a min heap
    right = ((2*index + 1) == (len(intList))) or ((intList[index] <= intList[2*index + 1]) and minHeapCheck(intList, 2*index + 1))

    # Returns the result from left and right, whether it is true or false
    return left and right 

# MinHeap class initialised by a list of integers
# Here, it starts with 0 as the first element
class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    # GetMinimum() - outputs the minimum value in the heap.
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def GetMinimum(self):
        return self.heap[1]

    # ExtractMinimum() - removes minimum from the heap (and returns the min)
    # Time Complexity => O(Log n) because of the time complexity of ToMinHeap function
    # Space Complexity => O(1) used only one temp variable delMin
    def ExtractMinimum(self):
        delMin = self.heap[1]
        self.heap[1] = self.heap[self.size] # Setting the last element as the first element
        self.size -= 1
        self.heap.pop() # Popping the last element in the list 
        ToMinHeap(self.heap, 1) # Re-constructing the heap to be a min heap again 
        return delMin

    # Insert(val) - inserts value into the heap (at the last place)
    # Time Complexity => O(Log n)
    # Space Complexity => O(1) no use of temp variable 
    def Insert(self, val):
        self.heap.append(val) # Appending the new value to the end of the list
        self.size += 1
        i = self.size
        while i // 2 > 0 and self.heap[i] < self.heap[i//2]: # Re-constructing the heap to be a min heap again
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i//2

    # Delete(index) - deletes value at a specific index from the heap.
    # Time Complexity => O(Log n)
    # Space Complexity => O(1)
    def Delete(self, index):
        self.heap.pop(index) 
        self.size -= 1
        i = self.size
        while i // 2 > 0 and self.heap[i] < self.heap[i//2]: # Re-constructing the heap to be a min heap again 
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i//2


