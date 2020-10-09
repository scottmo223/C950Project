# Robert S Morales 000954923

class Package:
    def __init__(self, packageId, address, city, zipcode, deadline, weight):
        """
        Initiallize Package class.
        """
        self.packageId = packageId
        self.deliveryAddress = address
        self.deliveryDeadline = deadline
        self.deliveryCity = city
        self.deliveryZipcode = zipcode
        self.packageWeight = weight
        self.deliveryTime = None
        self.departureTime = None
        self.deliveryStatus = 'At the hub'
