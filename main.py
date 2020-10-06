# Robert S Morales 000954923

import hashTable
import tools
import Truck
import ui
from datetime import timedelta

packageFile = 'WGUPS Package File.csv'
distanceTable = 'WGUPS Distance Table.csv'

packageHashTable = tools.readCSVFile(packageFile) # This loads the data csv file into a hash object
distanceObject = tools.readCSVFile(distanceTable, True) # This loads the distance csv file into a hash object

truck1 = Truck.Truck(1)
firstPackageIds = packageHashTable.getItemsByAddress(tools.initialAddress(distanceObject))
truck1.loadPackages(firstPackageIds, packageHashTable)

#WELCOME SCREEN
userInput = ui.welcomeScreen(truck1)
if userInput != '1':
    raise SystemExit(0)

#MANUALLY LOAD TRUCK
loadingType = input('\n** Press 1 to auto-load, press 2 to manually load packages **')
if loadingType == '1':
    truck1, packageHashTable = ui.autoPackageLoading(truck1, packageHashTable)
else:
    runManualPackageLoading = True
    while runManualPackageLoading:
        truck1, packageHashTable, runManualPackageLoading = ui.manualPackageLoading(truck1, packageHashTable)


#SET TIME FOR DEPARTURE
hour, minute = ui.setTruckDepartingTime()
packageHashTable.runningTime = timedelta(hours = hour, minutes = minute)

#DELIVER PACKAGES
print('About to deliver packages: ', truck1.packagesOnTruck) # delivering packages here
tools.deliverPackage(truck1, packageHashTable)

#GO TO MAIN MENU
# userInput = ui.mainMenu()
# if userInput == '1':
    # ui.manualPackageLoading(truck1, packageHashTable)




# print('delivered package id: ',truck1.deliverPackage())
# print(truck1.deliverPackage())

#NO WORKY - GET THE NEXT CLOSEST ADDRESS FROM GIVEN ADDRESS 
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
# print('Address of shortest initial address: ',(shortestAddress))
# print('Address of longest initial address: ',(longestAddress))

#THIS WORKS - PRINTS THE STATUS OF A PACKAGE (uses the variables shortestAddress and longestAddress above)
# print(tools.checkPackageStatus(packageHashTable, packageHashTable.getItemsByAddress(longestAddress)[0]))

#NOTES TO SELF
# print(distanceObject.addressDistanceMatrix) #2 dim array - array[searches down][searches across]
# print(distanceObject.addressDistanceMatrix[4][0]) #This gives the ADDRESS of the 4th row
# distanceObject.addressVisited(4)
# print('\nvisitied address 4')
# print('address not visited: ',distanceObject.addressesNotVisited)
# print('address visited',distanceObject.addressesVisited)
# print('index/address map',distanceObject.indexAddressMap)

#THIS WORKS - PRINTS THE INDEX OF THE SHORTEST (SMALLEST NUMBER) IN AN ARRAY
# print(distanceObject[5])
# print(tools.findShortestDistance(distanceObject[5]))
