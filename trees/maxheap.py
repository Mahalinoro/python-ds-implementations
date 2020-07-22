# ToMaxHeap function swaps elements in place such that the childs are always smaller than its parent
# Same principle as for ToMinHeap function, the only change is the operators 
# Time Complexity => O(log n)
# Space Complexity => O(1)
def ToMaxHeap(intList, index, size):
    leftChild = 2*index 
    rightChild = 2*index + 1
    maxNode = 0

    if leftChild < size and intList[leftChild] > intList[index]:
        maxNode = leftChild
    else:
        maxNode = index

    if rightChild < size and intList[rightChild] > intList[maxNode]:
        maxNode = rightChild
        
    if maxNode != index:
        intList[index], intList[maxNode] = intList[maxNode], intList[index]
        ToMaxHeap(intList, maxNode, size)

# BuildMaxHeap takes a list of integers as input. Then swaps elements in place using the helper function ToMaxHeap.
# The function will stop until the list is a max heap
# Time Complexity => O(n Log n)
# Space Complexity => O(n) because of the use of a variable to store the newly created heap
def BuildMaxHeap(intList):
    intList = [0] + intList
    index = len(intList) // 2 
    size = len(intList) 
    while index >= 1:
        ToMaxHeap(intList, index, size)
        index -= 1

    return intList

# HeapSort function that sort an array in ascending order
# Time Complexity => O(n log n) because of ToMaxHeap helper function which O(Log n) and N times until the array is sorted
# Space Complexity => O(n) because of use of a variable to store the newly created heap
def HeapSort(arr):
    heap = BuildMaxHeap(arr)
    size = len(heap) - 1

    while size >= (len(heap) - size - 2):
        heap[1], heap[size] = heap[size], heap[1]
        size -= 1
        ToMaxHeap(heap, 1, size)
    
    return heap[1:]


