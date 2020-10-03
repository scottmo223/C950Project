# Robert S Morales 000954923

import csv
import hashTable
import Package
import AddressDistances

def readCSVFile(file, distanceTable = False):
    with open(file, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        
        if distanceTable == True:
            newObject = AddressDistances.AddressDistances()
            for row in csvReader:
                newObject.addRow(row)
            return newObject
        else:
            newObject = hashTable.HashTable()
            next(csvReader) #grab header row and get it out of the way
            for row in csvReader:
                newPackage = Package.Package(row[0],row[1],row[2],row[4],row[5],row[6])
                newObject.addItem(newPackage)
            return newObject

def findShortestDistance(options, initialAddress = False):
    """
    Finds the shortest distance in an array of numbers. 
    Returns the index of the lowest number - not starting 
    from 0, but from 1.
    If this is the inital address list, set initialAddress = True.
    """
    if initialAddress == True:
        shortestDistance = float(options[2])    
    else:    
        shortestDistance = float(options[1])
    shortestDistanceIndex = 1
    for index, distance in enumerate(options[1:], start = 1):
        if distance != '' and float(distance) > 0 and float(distance) < shortestDistance:
            shortestDistance = float(distance)
            shortestDistanceIndex = index
    return shortestDistanceIndex

def findLongestDistance(options):
    """
    Finds the longest distance in an array of numbers. 
    Returns the index of the highest number - not starting 
    from 0, but from 1.
    """
    longestDistance = float(0)
    longestDistanceIndex = 1
    for index, distance in enumerate(options[1:], start = 1):
        if distance != '' and float(distance) > 0 and float(distance) > longestDistance:
            longestDistance = float(distance)
            longestDistanceIndex = index
    return longestDistanceIndex

def initialAddress(distanceObject, shortestDistance = True):
    """
    Returns the address of recommended starting package in the
    distanceObject matrix. If shortestDistance = True (default) then 
    returns the closest address, otherwise it will return the 
    longest.
    """
    firstColumnDistances = []
    for object in distanceObject.addressDistanceMatrix:
        firstColumnDistances.append(object[1])
    if shortestDistance == True:
        distanceIndex = findShortestDistance(firstColumnDistances, True)
    else:
        distanceIndex = findLongestDistance(firstColumnDistances)
    return distanceObject.indexAddressMap.get(distanceIndex)

def nextAddress(distanceObject, lastAddress):
    """
    Returns the address of the next shortest distance package delivery.
    Requires the distanceObject table and the last loaded address.
    """
    lastAddressDistances = None
    for i in distanceObject:
        if i[0] == lastAddress.deliveryAddress:
            lastAddressDistances = i
            break
    distanceIndex = findShortestDistance(lastAddressDistances)
    return distanceObject[distanceIndex][0]

def checkPackageStatus(packageHashTable, passedId):
    """
    Printout of a package's status. passedId should be a string like '4'
    """
    currentPackage = packageHashTable.getItem(passedId)
    print()
    print('id: '.ljust(11, ' '), currentPackage.packageId)
    print('address: '.ljust(11, ' '), currentPackage.deliveryAddress)
    print('city: '.ljust(11, ' '), currentPackage.deliveryCity)
    print('zip: '.ljust(11, ' '), currentPackage.deliveryZipcode)
    print('weight: '.ljust(11, ' '), currentPackage.packageWeight)
    print('status: '.ljust(11, ' '), currentPackage.deliveryStatus)
    print('deadline: '.ljust(11, ' '), currentPackage.deliveryDeadline)

def statusOfAllPackages(packageHashTable):
    #numberPackages = packageHashTable.keyAddressMap.count()
    print()
    print('ID'.ljust(3, ' '),'Status'.ljust(11, ' '), 'Address')
    for package in packageHashTable.keyAddressMap: 
        currentPackage = packageHashTable.getItem(package[0]) 
        packageId = currentPackage.packageId
        deliveryStatus = currentPackage.deliveryStatus
        deliveryAddress = currentPackage.deliveryAddress
        print(packageId.ljust(3, ' '), deliveryStatus.ljust(11, ' '), deliveryAddress)
    print()
        