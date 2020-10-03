# Robert S Morales 000954923

import hashTable
import tools
import Truck

packageFile = 'WGUPS Package File.csv'
distanceTable = 'WGUPS Distance Table.csv'

packageHashTable = tools.readCSVFile(packageFile) # This loads the data csv file into a hash object
distanceObject = tools.readCSVFile(distanceTable, True) # This loads the distance csv file into a hash object
packagesInHub = [i[0] for i in packageHashTable.keyAddressMap]

#LETS START LOADING TRUCK 1
truck1 = Truck.Truck(1, packagesInHub)
firstPackageIds = packageHashTable.getItemsByAddress(tools.initialAddress(distanceObject))
truck1.loadPackages(firstPackageIds, packageHashTable)
print('I loaded your first package for you.')
print('Truck1 packages: ', truck1.packagesOnTruck)
print('Packages at hub: ', packageHashTable.packagesAtHub)
print('Packages on trucks: ', packageHashTable.packagesOnTruck)
print('Packages delivered: ', packageHashTable.packagesDelivered)

# print('\nNow it\'s your turn. These are the packages left to load: ')
# print(truck1.packagesLeftToLoad)
# print('\nGet to work.')
# nextPackagesToLoad = input('Enter a package number and press Enter. When done type "stop"',)

# print('delivered package id: ',truck1.deliverPackage())
# print(truck1.deliverPackage())

#NO WORKY - GET THE NEXT CLOSEST ADDRESS FROM GIVEN ADDRESS (I don't think I can use this)
# print(tools.nextAddress(distanceObject, packageHashTable.getItem('14')))

#THIS WORKS - GET ALL PACKAGES WITH MATCHING ADDRESS
# print('list of packages that match')
# packageList = packageHashTable.getItemByAddress('4580 S 2300 E')
# print(packageList)

#THIS WORKS - PRINTOUT LIST OF ALL PACKAGE STATUSES
# tools.statusOfAllPackages(packageHashTable)

#THIS WORKS - PRINTS THE ADDRESS OF THE INITIAL PACKAGE, SHORTEST OR LONGEST
# shortestAddress = tools.initialAddress(distanceObject)
# longestAddress = tools.initialAddress(distanceObject,False)
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
