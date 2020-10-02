# Robert S Morales 000954923
# This is the hash table

class HashTable():
    """
    A Custom hash table. The default length is 1000, but
    this can be changed for future growth.
    """

    def __init__(self, length=1000):
        self.array = [None] * length

    def addItem(self, data):
        index = self.getIndex(data.packageId)
        if self.array[index] is None:
            self.array[index] = []
        self.array[index].append(data)        

    def getItem(self, key):
        index = self.getIndex(key)
        if self.array[index] is None:
            return print('no worky')
        for i in self.array[index]:
            if i.packageId == key:
                return i

    #indexing an int just gives the int - should pass it in as a string.
    def getIndex(self, key): 
        index = hash(str(key)) % len(self.array)
        return index