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
        self.truckCapacity = capacity
        self.mileage = 0

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

    def deliverPackage(self):
        """
        Removes a package from the front of the queue and returns the package key.
        """
        return self.packagesOnTruck.pop(0)