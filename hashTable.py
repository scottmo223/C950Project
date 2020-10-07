# Robert S Morales 000954923
# This is the hash table

from datetime import timedelta

class HashTable():
    """
    A Custom hash table. The default length is 1000, but
    this can be changed for future growth.
    """
    def __init__(self, length=1000):
        self.array = [None] * length
        self.keyAddressMap = []
        self.packagesAtHub = []
        self.packagesOnTruck = []
        self.packagesDelivered = []
        #MIGHT NEED A TIMEDELIVERED TRACKING HERE (NM THATS IN THE PACKAGE OBJECT)
        self.runningTime = None

    def addItem(self, data):
        index = self.getIndex(data.packageId)
        if self.array[index] is None:
            self.array[index] = []
        self.array[index].append(data)
        self.keyAddressMap.append([data.packageId,data.deliveryAddress])
        self.packagesAtHub.append(data.packageId)

    def getItem(self, key):
        index = self.getIndex(key)
        if self.array[index] is None:
            return print('no worky')
        for i in self.array[index]:
            if i.packageId == key:
                return i

    def getItemsByAddress(self, address):
        """
        Returns a list of package matching the given address.
        """
        matchingAddresses = []
        for i in self.keyAddressMap:
            if i[1] == address:
                matchingAddresses.append(self.getItem(i[0]))
        return matchingAddresses

    #indexing an int just gives the int - should pass it in as a string.
    def getIndex(self, key): 
        index = hash(str(key)) % len(self.array)
        return index

    def deliverPackage(self, key, time):
        self.packagesOnTruck.remove(key)
        self.packagesDelivered.append(key)
        self.runningTime += time
        self.getItem(key).deliveryTime = self.runningTime