# Robert S Morales 000954923

class AddressDistances():
    """
    Contains matrix of address distances, an index to address map, the indexes of 
    visited addresses, and the indexes of not visited addresses.
    """
    def __init__(self):
        self.addressDistanceMatrix = []
        self.indexAddressMap = {}
        self.addressesVisited = []
        self.addressesNotVisited = []
        self.counter = 0

    def addRow(self, data):
        self.addressDistanceMatrix.append(data)
        self.indexAddressMap[self.counter] = self.addressDistanceMatrix[-1][0]
        if self.counter != 0:
            self.addressesNotVisited.append(self.counter)
        self.counter += 1

    def addressVisited(self, addressIndex):
        self.addressesVisited.append(int(addressIndex))
        self.addressesNotVisited.remove(int(addressIndex))