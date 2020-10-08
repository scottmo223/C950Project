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

truck1 = tools.sortPackagesOnTruck(truck1, packageHashTable, distanceObject)
truck2 = tools.sortPackagesOnTruck(truck2, packageHashTable, distanceObject)
truck3 = tools.sortPackagesOnTruck(truck3, packageHashTable, distanceObject)
# print(truck1.packagesOnTruck) ###CAN DELETE THIS - FOR REFERENCE ONLY
# print(truck2.packagesOnTruck)
# print(truck3.packagesOnTruck)

# SET TIME FOR DEPARTURE
packageHashTable.runningTime = timedelta(hours = 8, minutes = 0)

#DELIVER PACKAGES
# print('About to deliver packages: ', truck1.packagesOnTruck) # delivering packages here
truck1, packageHashTable, distanceObject = tools.deliverPackage(truck1, packageHashTable, distanceObject)
truck2, packageHashTable, distanceObject = tools.deliverPackage(truck2, packageHashTable, distanceObject)
truck3, packageHashTable, distanceObject = tools.deliverPackage(truck3, packageHashTable, distanceObject)

#PRINT THE DELIVERY DETAILS
print('\n\n\nStarted at 8am, ended at: ',packageHashTable.runningTime)
print('\nTruck 1 mileage: ',round(truck1.mileage,1))
print('Truck 2 mileage: ',round(truck2.mileage,1))
print('Truck 3 mileage: ',round(truck3.mileage,1))
print('\nTotal Mileage: ', round((truck1.mileage+truck2.mileage+truck3.mileage),1))

#GO TO MAIN MENU
ui.mainMenu(packageHashTable)

raise SystemExit(0)





