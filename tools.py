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

def findShortestDistance(options):
    """
    Finds the shortest distance in an array of numbers. 
    Returns the index of the lowest number - not starting 
    from 0, but from 1.
    If this is the inital address list, set initialAddress = True.
    """
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

def statusOfAllPackages(packageHashTable):
    print('\nID'.ljust(3, ' '),'Status'.ljust(11, ' '),'Delivered'.ljust(10,' '), 'Address')
    for package in packageHashTable.keyAddressMap: 
        currentPackage = packageHashTable.getItem(package[0]) 
        packageId = currentPackage.packageId
        deliveryStatus = currentPackage.deliveryStatus
        deliveryTime = str(currentPackage.deliveryTime)
        deliveryAddress = currentPackage.deliveryAddress
        print(packageId.ljust(3, ' '), deliveryStatus.ljust(11, ' '), deliveryTime.ljust(10,' '),deliveryAddress)
    print()

def deliverPackage(truck, packageHashTable, distanceObject):
    packageCounter = len(truck.packagesOnTruck)
    
    while packageCounter > 0:
        packageKey = truck.packagesOnTruck[0]
        deliveredPackage = packageHashTable.getItem(packageKey)
        packageAddress = packageHashTable.getItem(packageKey).deliveryAddress
        lastAddressIndex = truck.addressesVisited[-1]
        currentAddressIndex = distanceObject.indexAddressMap.index(packageAddress)
        # Need the longest distance to be the first index
        if currentAddressIndex < lastAddressIndex:
            distanceTraveled = float(distanceObject.addressDistanceMatrix[lastAddressIndex][currentAddressIndex])
        else:
            distanceTraveled = float(distanceObject.addressDistanceMatrix[currentAddressIndex][lastAddressIndex])
        
        time = calculateTime(truck.mph, distanceTraveled)

        packageHashTable.deliverPackage(packageKey)
        truck.deliverPackage(currentAddressIndex, time, distanceTraveled, deliveredPackage)
        packageCounter -= 1
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
    #Truck 2 will start from the farthest distance
    # if truck.truckId == 2:
        # tempPackageListIndex = findLongestDistance(distancesFromStartAddress)
    # else:
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
    print('sorted list: ',truck.packagesOnTruck)
    return truck

def calculateTime(mph, distance):
    timeInHours = distance/mph
    time = timedelta(hours = timeInHours)
    return time

def setDepartureTime(truck, packageHashTable, time):
    truck.setDepartureTime(time)
    for packageKey in truck.packagesOnTruck:
        package = packageHashTable.getItem(packageKey)
        package.departureTime = time