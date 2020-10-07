# Robert S Morales 000954923

class AddressDistances():
    """
    Contains matrix of address distances, an index to address map, the indexes of 
    visited addresses, and the indexes of not visited addresses.
    """
    def __init__(self):
        self.addressDistanceMatrix = []
        self.indexAddressMap = []
        self.counter = 0 #This is for indexAddressMap creation

    def addRow(self, data):
        self.addressDistanceMatrix.append(data)
        self.indexAddressMap.append(self.addressDistanceMatrix[-1][0])
        self.counter += 1