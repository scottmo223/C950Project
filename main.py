# Robert S Morales 000954923

import hashTable
import tools
import Truck
import ui
from datetime import timedelta

packageFile = 'WGUPS Package File.csv'
distanceTable = 'WGUPS Distance Table.csv'

#LOAD CSV FILES
packageHashTable = tools.readCSVFile(packageFile)
distanceObject = tools.readCSVFile(distanceTable, True) 

#WELCOME SCREEN
userInput = ui.welcomeScreen()
if userInput != '1':
    raise SystemExit(0)


#CREATE TRUCK 1
truck1 = Truck.Truck(1,13)
requiredPackages = ['1','29','30','31','34','40','13','14','15','16','19','20','21'] # must go out for delivery on the same truck at the same time
truck1.loadPackages(requiredPackages, packageHashTable)

#CREATE TRUCK 2
truck2 = Truck.Truck(2)
requiredPackages = ['3','18','36','37','38','6','25','26','28','32','33'] # can only be loaded on truck 2; cannot leave the hub before 9:05am
truck2.loadPackages(requiredPackages, packageHashTable)

#CREATE TRUCK 3
truck3 = Truck.Truck(3)
requiredPackages = ['8','9'] # cannot leave until 10:20
truck3.loadPackages(requiredPackages, packageHashTable)


#AUTO LOAD REST OF PACKAGES ON TRUCKS
truck1, packageHashTable = ui.autoPackageLoading(truck1, packageHashTable)
truck2, packageHashTable = ui.autoPackageLoading(truck2, packageHashTable)
truck3, packageHashTable = ui.autoPackageLoading(truck3, packageHashTable)
# print('packages on truck 1: ', truck1.packagesOnTruck) # !!! DELETE !!! these are already printed in the autoPackageLoading function
# print('packages on truck 2: ', truck2.packagesOnTruck)
# print('packages on truck 3: ', truck3.packagesOnTruck)

#SET TIME FOR DEPARTURE !!!! wont need this anymore !!!!
# hour, minute = ui.setTruckDepartingTime()
packageHashTable.runningTime = timedelta(hours = 8, minutes = 0)

#DELIVER PACKAGES
# print('About to deliver packages: ', truck1.packagesOnTruck) # delivering packages here
print('truck1')
truck1, packageHashTable, distanceObject = tools.deliverPackage(truck1, packageHashTable, distanceObject)
print('truck2')
truck2, packageHashTable, distanceObject = tools.deliverPackage(truck2, packageHashTable, distanceObject)
print('truck3')
truck3, packageHashTable, distanceObject = tools.deliverPackage(truck3, packageHashTable, distanceObject)

#PRINT THE DELIVERY DETAILS
print('\n\n\nStarted at 8am, ended at: ',packageHashTable.runningTime)
print('\nTruck 1 mileage: ',round(truck1.mileage,1))
print('Truck 2 mileage: ',round(truck2.mileage,1))
print('Truck 3 mileage: ',round(truck3.mileage,1))
print('\nTotal Mileage: ', round((truck1.mileage+truck2.mileage+truck3.mileage),1))

#GO TO MAIN MENU
userInput = ui.mainMenu()
if userInput == '1':
    ui.manualPackageLoading(truck1, packageHashTable)
elif userInput == '2':
    pass #this will be truck 2
elif userInput == '3':
    tools.checkPackageStatus(packageHashTable, '3')
elif userInput == '4':
    tools.statusOfAllPackages(packageHashTable)
else:
    raise SystemExit(0)





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
