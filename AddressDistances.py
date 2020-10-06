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
        self.counter = 0 #This is for indexAddressMap creation

    def addRow(self, data):
        self.addressDistanceMatrix.append(data)
        self.indexAddressMap[self.counter] = self.addressDistanceMatrix[-1][0]
        if self.counter != 0:
            self.addressesNotVisited.append(self.counter)
        self.counter += 1

    def deliverPackage(self, addressIndex):
        if self.addressesVisited.count(addressIndex) > 0:   #not sure why i'd need to display this - consider deleting
            print("\n\n*** Already Visited This one ***\n\n") 
        else:
            self.addressesVisited.append(int(addressIndex))
            self.addressesNotVisited.remove(int(addressIndex))
            print('addresses visited: ', self.addressesVisited)

    