# Robert S Morales 000954923

import csv
import hashTable
import Package
import AddressDistances
from datetime import timedelta

def readCSVFile(file, distanceTable = False):
    '''
    Takes csv file data for packages or city distance matrix and creates either a
    package hash table or a distance matrix class to hold the data.
    '''
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
    Returns the index of the lowest number.
    """
    shortestDistance = float(options[0])
    shortestDistanceIndex = 0
    
    for index, distance in enumerate(options):
        if distance != '' and float(distance) < shortestDistance:
            shortestDistance = float(distance)
            shortestDistanceIndex = index
    
    return shortestDistanceIndex

def statusOfAllPackages(packageHashTable):
    '''
    Prints out the end status of all packages in the package hash table.
    '''
    print('\nID'.ljust(4, ' '),'Status'.ljust(11, ' '),'Delivered'.ljust(10,' '),'Deadline'.ljust(10,' '), 'Address')
    
    for package in packageHashTable.keyAddressMap: 
        currentPackage = packageHashTable.getItem(package[0]) 
        packageId = currentPackage.packageId
        deliveryStatus = currentPackage.deliveryStatus
        deliveryTime = str(currentPackage.deliveryTime)
        deadline = currentPackage.deliveryDeadline
        deliveryAddress = currentPackage.deliveryAddress
        print(packageId.ljust(3, ' '), deliveryStatus.ljust(11, ' '), deliveryTime.ljust(10,' '), deadline.ljust(10,' '), deliveryAddress)
    print()

def statusOfAllPackagesAtGivenTime(packageHashTable):
    '''
    User selects a time to display data snapshot for all packages in the package hash table at the given time.
    '''
    print('\nEnter a time - use 24 hour format ####      Example: 1340')
    userInput = input()
    hour = int(userInput[:2])
    minute = int(userInput[2:])
    userInputTime = timedelta(hours = hour, minutes = minute)
    
    print(f'\n\t--- Status of all packages at {userInput} ---')
    print('\nID'.ljust(4, ' '),'Status'.ljust(12, ' '),'Delivered'.ljust(10,' '),'Deadline'.ljust(10,' '), 'Address')
    
    for package in packageHashTable.keyAddressMap: 
        currentPackage = packageHashTable.getItem(package[0]) 
        packageId = currentPackage.packageId
        deliveryStatus = currentPackage.deliveryStatus
        deliveryTime = currentPackage.deliveryTime
        departureTime = currentPackage.departureTime
        deadline = currentPackage.deliveryDeadline
        deliveryAddress = currentPackage.deliveryAddress
        
        if userInputTime < departureTime :
            deliveryStatus = 'At the hub'
            deliveryTime = ''
        elif userInputTime >= departureTime and userInputTime < deliveryTime:
            deliveryStatus = 'En-route'
            deliveryTime = ''
        
        print(packageId.ljust(3, ' '), deliveryStatus.ljust(12, ' '), str(deliveryTime).ljust(10,' '), deadline.ljust(10,' '), deliveryAddress)
    print()

def deliverPackage(truck, packageHashTable, distanceObject):
    '''
    Takes an array of packages and delivers them sequentially, starting from the beginning
    of the list (index 0). After all the packages have been delivered, the truck returns
    to the hub.
    '''
    packageCounter = len(truck.packagesOnTruck)
    
    while packageCounter > 0:
        packageKey = truck.packagesOnTruck[0]
        deliveredPackage = packageHashTable.getItem(packageKey)
        packageAddress = packageHashTable.getItem(packageKey).deliveryAddress
        lastAddressIndex = truck.addressesVisited[-1]
        currentAddressIndex = distanceObject.indexAddressMap.index(packageAddress)
        # Need the longest distance to be the first index of distance matrix
        if currentAddressIndex < lastAddressIndex:
            distanceTraveled = float(distanceObject.addressDistanceMatrix[lastAddressIndex][currentAddressIndex])
        else:
            distanceTraveled = float(distanceObject.addressDistanceMatrix[currentAddressIndex][lastAddressIndex])
        
        time = calculateTime(truck.mph, distanceTraveled)

        packageHashTable.deliverPackage(packageKey)
        truck.deliverPackage(currentAddressIndex, time, distanceTraveled, deliveredPackage)
        packageCounter -= 1

    #Return to hub logic
    lastAddressIndex = truck.addressesVisited[-1]
    distanceTraveled = float(distanceObject.addressDistanceMatrix[lastAddressIndex][1])
    time = calculateTime(truck.mph, distanceTraveled)
    truck.mileage += distanceTraveled
    truck.runningTime += time

    return truck, packageHashTable, distanceObject

def sortPackagesOnTruck(truck, packageHashTable, distanceObject):
    '''
    Sorts the packages on a given truck using a nearest neighbor algorithm, starting from the hub.
    '''
    sortedPackagesList = []
    distancesFromStartAddress = []
    packagesOnTruck = truck.packagesOnTruck
    startAddressKey = truck.addressesVisited[0] 
    nextAddressKey = startAddressKey
    
    #Find shortest distance from hub
    for packageKey in packagesOnTruck:
        packageAddress = packageHashTable.getItem(packageKey).deliveryAddress
        currentAddressIndex = distanceObject.indexAddressMap.index(packageAddress)
        distancesFromStartAddress.append(float(distanceObject.addressDistanceMatrix[currentAddressIndex][1]))
    
    tempPackageListIndex = findShortestDistance(distancesFromStartAddress)
    sortedPackagesList.append(packagesOnTruck[tempPackageListIndex])
    startPackageKey = packagesOnTruck.pop(tempPackageListIndex)
    
    #Sort the rest of the packages
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
    '''
    Returns the time traveled for a given distance and speed.
    '''
    timeInHours = distance/mph
    time = timedelta(hours = timeInHours)
    
    return time

def setDepartureTime(truck, packageHashTable, time):
    '''
    Sets the departure time from the hub for all packages on a given truck.
    '''
    truck.setDepartureTime(time)
    for packageKey in truck.packagesOnTruck:
        package = packageHashTable.getItem(packageKey)
        package.departureTime = time