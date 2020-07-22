# contains function which returns True if the value is in the array, return False otherwise
# First, the function loops through the range of the length of the array
# Then, comparing the value to each value of the elements using .get method
# Return True if it matches any value within the array, it will return False otherwise
def contains(array, val):
    # Time Complexity => O(n)
    # Space Complexity => O(1)
    for i in range(array.len()):
        if val == array.get(i):
            return True
    return False

# reverse function which reverses the entire array and output a new array
# First, it loops through a range which starts from the end of the array
# Then, using .add and .get methods to add the values to a new array
def reverse(array, new_array):
    # Time Complexity => O(n)
    # Space Complexity => O(n)
    for i in range(array.len()-1, -1, -1):
        new_array.add(array.get(i))
    return new_array.__str__()


# insert function which inserts a value at a given index i
# First, with .get and .add methods, it will fetch the value of the current element into a new array
# Then, with .set, the current value will be updated to the new value
# After, it loops through the inital array starting from the position after the index until the end of the array and add the values into the new array
# This time, within the same range with the initial array, the delete method will delete all the values in the initial array
# Finally. looping again through the new array then add the values back to the initial array
def insert(array, new_array, val, i):
    # Time Complexity => O(n)
    # Space Complexity => O(n)
    current_value = array.get(i)
    new_array.add(current_value)

    array.set(val, i)

    for x in range(i+1, array.len()):
        new_array.add(array.get(x))

    for j in range(i+1, array.len()):
        array.delete()

    for n in range(new_array.len()):
        array.add(new_array.get(n))

    return array.__str__()



