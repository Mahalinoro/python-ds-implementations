# importing array
import array 

# Simple Array class containing only integer
class SimpleArray:
    # __init__ method is creating the array containing only integer
    # the initializer parameter is the array 
    # "i" is the parameter that array method take to create an array containing only integer
    def __init__(self, initializer):
        self.initializer = initializer
        self.arr = array.array('i', initializer)

    def __str__(self):
        return self.arr

    # .len method which outputs the length of the array
    # First, it loops through each element within the array
    # Initialize a variable count then it adds 1 to the count each time it loops through the array
    def len(self):   
        # Time Complexity => O(n)
        # The worst case O(n) because the loop will depend on the size of the array
        # Space Complexity => O(n)
        # The space complexity is just the updated number of count and will increase as the size of array is big
        count = 0
        for i in self.arr:
            count += 1
        return count

    # .get method which outputs the value at a given index i
    # Using indexing to fetch the value of the element
    def get(self, i):
        # Time Complexity => O(1)
        # It is because it accessed the value directly
        # Space Complexity => O(1)
       value = self.arr[i]
       return value

    # .set method which replaces the actual value at index i to a new value
    # Using index to fetch the value of the element then assign it to the new value
    def set(self, val, i):
        # Time Complexity => O(1)
        # Assigning the value to the index is constant time
        # Space Complexity => O(1)
        self.arr[i] = val
        return self.arr[i]
