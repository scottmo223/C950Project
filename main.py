# Robert S Morales 000954923

import hashTable
import tools
import Truck

packageFile = 'WGUPS Package File.csv'
distanceTable = 'WGUPS Distance Table.csv'

packageHashTable = tools.readCSVFile(packageFile) # This loads the data csv file into a hash object
distanceObject = tools.readCSVFile(distanceTable, True) # This loads the distance csv file into a hash object




# truck1 = Truck.Truck(1)
# firstPackageId = packageHashTable.getItemByAddress(tools.initialPackage(distanceObject))
# truck1.loadPackage(firstPackageId[0])
# print('delivered package id: ',truck1.deliverPackage())
# print(truck1.deliverPackage())


#THIS WORKS - GET ALL PACKAGES WITH MATCHING ADDRESS
# print('list of packages that match')
# packageList = packageHashTable.getItemByAddress('4580 S 2300 E')
# print(packageList)

#THIS WORKS - PRINTOUT LIST OF ALL PACKAGE STATUSES
# tools.statusOfAllPackages(packageHashTable)

#THIS WORKS - PRINTS THE ADDRESS OF THE INITIAL PACKAGE, SHORTEST OR LONGEST
# shortestAddress = tools.initialPackage(distanceObject)
# longestAddress = tools.initialPackage(distanceObject,False)
# print(packageHashTable.getItemsByAddress(shortestAddress))
# print(packageHashTable.getItemsByAddress(longestAddress))

#THIS WORKS - PRINTS THE STATUS OF A PACKAGE (uses the variables shortestAddress and longestAddress above)
# print(tools.checkPackageStatus(packageHashTable, packageHashTable.getItemsByAddress(longestAddress)[0]))

#NOTES TO SELF
# print(distanceObject) #2 dim array - array[searches down][searches across]
# print(distanceObject[4][0]) #This gives the ADDRESS of the 4th row

#THIS WORKS - PRINTS THE INDEX OF THE SHORTEST (SMALLEST NUMBER) IN AN ARRAY
# print(distanceObject[5])
# print(tools.findShortestDistance(distanceObject[5]))
