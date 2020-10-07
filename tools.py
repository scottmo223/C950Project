# Robert S Morales 000954923

import csv
import hashTable
import Package
import AddressDistances
from datetime import timedelta

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
    shortestDistanceIndex = 0
    for index, distance in enumerate(options):
        if distance != '' and float(distance) < shortestDistance:
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

def initialAddress(distances, shortestDistance = True):
    """
    Returns the address of recommended starting package in the
    distances matrix. If shortestDistance = True (default) then 
    returns the closest address, otherwise it will return the 
    longest.
    """
    firstColumnDistances = []
    for i in distances:
        firstColumnDistances.append(i[1])
    if shortestDistance == True:
        distanceIndex = findShortestDistance(firstColumnDistances, True)
    else:
        distanceIndex = findLongestDistance(firstColumnDistances)
    return distances.indexAddressMap[distanceIndex]

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
    print('delivered:'.ljust(11, ' '), currentPackage.deliveryTime)

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

def deliverPackage(truck, packageHashTable, distanceObject):
    packageCounter = len(truck.packagesOnTruck)
    
    for i in range(0, packageCounter):
        packageKey = truck.packagesOnTruck[0]
        packageAddress = packageHashTable.getItem(packageKey).deliveryAddress
        lastAddressIndex = truck.addressesVisited[-1]
        currentAddressIndex = distanceObject.indexAddressMap.index(packageAddress)
        print(f'last address: {lastAddressIndex} current Address: {currentAddressIndex}')
        # Need the longest distance to be the first index
        if currentAddressIndex < lastAddressIndex:
            distanceTraveled = float(distanceObject.addressDistanceMatrix[lastAddressIndex][currentAddressIndex])
        else:
            distanceTraveled = float(distanceObject.addressDistanceMatrix[currentAddressIndex][lastAddressIndex])
        time = calculateTime(truck.mph, distanceTraveled)

        packageHashTable.deliverPackage(packageKey, time)
        truck.deliverPackage(currentAddressIndex)
        # distanceObject.deliverPackage(currentAddressIndex)
        truck.mileage += distanceTraveled

    return truck, packageHashTable, distanceObject
        

def sortPackagesOnTruck(truck, packageHashTable, distanceObject):
    sortedPackagesList = []
    distancesFromStartAddress = []
    packagesOnTruck = truck.packagesOnTruck
    startAddressKey = truck.addressesVisited[0] 
    nextAddressKey = startAddressKey
    #find shortest distance from hub
    for packageKey in packagesOnTruck:
        packageAddress = packageHashTable.getItem(packageKey).deliveryAddress
        currentAddressIndex = distanceObject.indexAddressMap.index(packageAddress)
        distancesFromStartAddress.append(float(distanceObject.addressDistanceMatrix[currentAddressIndex][1]))
    tempPackageListIndex = findShortestDistance(distancesFromStartAddress)
    sortedPackagesList.append(packagesOnTruck[tempPackageListIndex])
    startPackageKey = packagesOnTruck.pop(tempPackageListIndex)
    #Now the rest of the packages
    while len(packagesOnTruck) > 1:
        distancesFromStartAddress.clear()
        startPackageAddress = packageHashTable.getItem(startPackageKey).deliveryAddress
        startPackageAddressIndex = distanceObject.indexAddressMap.index(startPackageAddress)
        for packageKey in packagesOnTruck:
            packageAddress = packageHashTable.getItem(packageKey).deliveryAddress
            currentAddressIndex = distanceObject.indexAddressMap.index(packageAddress)
            if currentAddressIndex < startPackageAddressIndex:
                distancesFromStartAddress.append(float(distanceObject.addressDistanceMatrix[startPackageAddressIndex][currentAddressIndex]))
            else:
                distancesFromStartAddress.append(float(distanceObject.addressDistanceMatrix[currentAddressIndex][startPackageAddressIndex]))

        tempPackageListIndex = findShortestDistance(distancesFromStartAddress)
        sortedPackagesList.append(packagesOnTruck[tempPackageListIndex])
        startPackageKey = packagesOnTruck.pop(tempPackageListIndex)
        startAddressKey = nextAddressKey
    sortedPackagesList.append(packagesOnTruck[0])
    truck.packagesOnTruck = sortedPackagesList
    return truck

def calculateTime(mph, distance):
    timeInHours = distance/mph
    time = timedelta(hours = timeInHours)
    return time