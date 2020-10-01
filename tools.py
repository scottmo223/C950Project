# Robert S Morales 000954923

import csv
import hashTable

def readCSVFile(file, makeArray = False):
    with open(file, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        
        if makeArray == True:
            newObject = []
            for row in csvReader:
                newObject.append(row)
            return newObject
        else:
            newObject = hashTable.HashTable()
            next(csvReader) #this grabs the header row and gets it out of the way
            for row in csvReader:
                newObject.addItem(row[0],row)
            return newObject

def findShortestDistance(options): # I had (location, options) with the intent of having the address relevant somehow
    shortestDistance = float(options[1])
    shortestDistanceIndex = 1
    for index, distance in enumerate(options[1:], start = 1):
        if distance != '' and float(distance) > 0 and float(distance) < shortestDistance:
            shortestDistance = float(distance)
            shortestDistanceIndex = index
    # print(shortestDistance, shortestDistanceIndex)
    return shortestDistanceIndex

def findLongestDistance(location, options):
    longestDistance = float(0)
    longestDistanceIndex = 1
    for index, distance in enumerate(options[1:], start = 1):
        if distance != '' and float(distance) > 0 and float(distance) > longestDistance:
            longestDistance = float(distance)
            longestDistanceIndex = index
    # print(longestDistance, longestDistanceIndex)
    return longestDistanceIndex

#testing
# location = '1060 Dalton Ave S'
# options = ['2300 Parkway Blvd', '8.6', '6.3', '4', '5.1', '4.3', '9', '0', '3.6', '8.8', '9.4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

# print(findLongestDistance(location, options))

def loadTruck1FirstPackage(distanceObject):
    firstColumnDistances = []
    for object in distanceObject:
        firstColumnDistances.append(object[1])
    shortestDistanceIndex = findShortestDistance(firstColumnDistances)
    
    return firstColumnDistances