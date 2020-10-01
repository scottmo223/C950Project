# Robert S Morales 000954923
# This is the csvReader

import csv
import hashTable

def csvReader(file, makeArray = False):
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