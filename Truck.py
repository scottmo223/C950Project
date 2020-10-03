# Robert S Morales 000954923
# Truck Class

class Truck:
    def __init__(self, truckId, capacity = 16):
        """
        Initialized truck class.
        """
        self.truckId = truckId
        self.packages = []
        self.truckCapacity = capacity
        self.mileage = 0

    def loadPackage(self, packageId):
        """
        Add a package to the delivery queue.
        """
        self.packages.append(packageId)

    def deliverPackage(self):
        """
        Removes a package from the front of the queue and returns the package key.
        """
        return self.packages.pop(0)