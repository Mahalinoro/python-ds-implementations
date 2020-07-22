# Association List class
class AssociativeList:
    def __init__(self):
        self.alist = []

    def __str__(self):
        return self.alist

    # .add method which adds the key/value to the alist at the end
    # It loops through the alist elements then access the key with x[0] and compare it if it is equal to the key
    # It will return 'Element already in the list' if there is a key with the same value
    # Otherwise, it will append the key/value pair in the alist
    def add(self, key, value):
        # Time Complexity => O(n)
        # Space Complexity => O(n)
        for x in self.alist:
            if x[0] == key:
                return 'Element already in the list'
        self.alist.append((key, value))
        return self.alist

    # .remove method which removes a key/value pair at a given key
    # It loops through the alist elements, then compare the key with x[0] which access the key within the alist
    # Then, if it matches the element then it will remove the key/value pair
    def remove(self, key):
        # Time Complexity => O(n)
        # Space Complexity => O(n)
        for x in self.alist:
            if x[0] == key:
                self.alist.remove(x)
        return self.alist

    # .modify method which updates the value of the key/value pair with a new value
    # The same principle as the methods above with the loop
    # Then, using remove methods, it will remove the key/value pair
    # Then using append, it will add the key/value pair at the end of the alist since the key/value is a tuple, it is immutable
    def modify(self, key, newvalue):
        # Time Complexity => O(n)
        # Space Complexity => O(n)
        for x in self.alist:
            if x[0] == key:
                self.alist.remove(x) # This is the typical remove not the method above
                self.alist.append((key, newvalue))
        return self.alist

    # .lookup method which will look for a given key and return its value
    # The same principle as the above methods
    # This time it will return the value of the specified key which is x[1]
    def lookup(self, key):
        # Time Complexity => O(n)
        # Space Complexity => O(1)
        for x in self.alist:
            if x[0] == key:
                return x[1]





