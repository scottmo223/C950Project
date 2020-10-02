# Robert S Morales 000954923
# Truck Class

class Truck:
    def __init__(self, truckId, packages, capacity = 14):
        """
        Initialized truck class.
        """
        self.truckId = truckId
        self.packages = packages
        self.truckCapacity = capacity
