from question_one import SimpleArray

# subclass Dynamic Array of the Simple Array
class DynamicArray(SimpleArray):
    def __init__(self):
        self.arr = []              

    # .add method which adds an element at the end of the array
    # Using append method since the dynamic array here is a list
    def add(self, val):
        # Time Complexity => O(1)
        # Appending a value at the end takes constant time
        # Space Complexity => n+1 since we add a new element 
        self.arr.append(val)
        return self.arr

    # .delete method which removes the latest element of the array
    # Using pop method to define delete
    def delete(self):
        # Time Complexity => O(1)
        # Space Complexity => n-1 since we deleted an element from the array
        self.arr.pop()
        return self.arr


