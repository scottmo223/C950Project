# Robert S Morales 000954923
# Package Class

class Package:
    def __init__(self, id, address, city, zip, deadline, weight):
        """
        Initiallize Package class.
        """
        self.packageId = id
        self.deliveryAddress = address
        self.deliveryDeadline = deadline
        self.deliveryCity = city
        self.deliveryZipcode = zip
        self.packageWeight = weight
        self.deliveryStatus = 'At the hub'