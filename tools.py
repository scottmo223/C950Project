# Robert S Morales 000954923

import csv
import hashTable
import Package

def readCSVFile(file, distanceTable = False):
    with open(file, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        
        if distanceTable == True:
            newObject = []
            for row in csvReader:
                newObject.append(row)
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
    """
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

def initialPackage(distanceObject, shortestDistance = True):
    """
    Returns the address of recommended starting package in the
    distanceObject Array. If shortestDistance = True (default) then 
    returns the closest address, otherwise it will return the 
    longest.
    """
    firstColumnDistances = []
    for object in distanceObject:
        firstColumnDistances.append(object[1])
    if shortestDistance == True:
        distanceIndex = findShortestDistance(firstColumnDistances)
    else:
        distanceIndex = findLongestDistance(firstColumnDistances)
    return distanceObject[distanceIndex][0]

def checkPackageStatus(packageHashTable, passedId):
    """
    Printout of a package's status. passedId should be a string like '4'
    """
    print()
    print('id: '.ljust(11, ' '), packageHashTable.getItem(passedId).packageId)
    print('address: '.ljust(11, ' '), packageHashTable.getItem(passedId).deliveryAddress)
    print('city: '.ljust(11, ' '), packageHashTable.getItem(passedId).deliveryCity)
    print('zip: '.ljust(11, ' '), packageHashTable.getItem(passedId).deliveryZipcode)
    print('weight: '.ljust(11, ' '), packageHashTable.getItem(passedId).packageWeight)
    print('status: '.ljust(11, ' '), packageHashTable.getItem(passedId).deliveryStatus)
    print('deadline: '.ljust(11, ' '), packageHashTable.getItem(passedId).deliveryDeadline)