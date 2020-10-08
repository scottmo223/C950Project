# Robert S Morales 000954923
# Truck Class

import hashTable

class Truck:
    def __init__(self, truckId, capacity = 16):
        """
        Initialized truck class.
        """
        self.truckId = truckId
        self.packagesOnTruck = []
        self.packagesDelivered = []
        self.truckCapacity = capacity
        self.mph = 18
        self.mileage = 0
        self.addressesVisited = [1]
        self.timeLeftHub = None

    def loadPackages(self, packageIds, packageHashTable):
        """
        Add a list of packages to the delivery queue. Will add package to
        packagesOnTruck and remove package from packagesAtHub on the package
        hash table.
        """
        for packageId in packageIds:
            self.packagesOnTruck.append(packageId)
            packageHashTable.packagesOnTruck.append(packageId)
            packageHashTable.packagesAtHub.remove(packageId)
        return packageHashTable

    def deliverPackage(self, addressIndex):
        """
        Removes a package from the front of the queue and returns the package key.
        """
        if self.addressesVisited.count(addressIndex) > 0:   
            #if already at this address, do nothing
            pass
        else:
            self.addressesVisited.append(int(addressIndex))
            self.packagesDelivered.append(self.packagesOnTruck[0])
        return self.packagesOnTruck.pop(0)