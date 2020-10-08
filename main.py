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
truck1 = Truck.Truck(1,14) #used to be only 13 packages
requiredPackages = ['1','29','30','31','34','40','13','14','15','16','19','20','21','37'] # must go out for delivery on the same truck at the same time
truck1.loadPackages(requiredPackages, packageHashTable)

#CREATE TRUCK 2
truck2 = Truck.Truck(2,13)
requiredPackages = ['3','18','36','38','6','25','26','28','32','33'] # can only be loaded on truck 2; cannot leave the hub before 9:05am
truck2.loadPackages(requiredPackages, packageHashTable)

#CREATE TRUCK 3
truck3 = Truck.Truck(3)
requiredPackages = ['8','9'] # cannot leave until 10:20
truck3.loadPackages(requiredPackages, packageHashTable)

#AUTO LOAD REST OF PACKAGES ON TRUCKS
truck1, packageHashTable = ui.autoPackageLoading(truck1, packageHashTable)
truck2, packageHashTable = ui.autoPackageLoading(truck2, packageHashTable)
truck3, packageHashTable = ui.autoPackageLoading(truck3, packageHashTable)

#SORT PACKAGES FOR OPTIMIZED DELIVERY ROUTE
truck1 = tools.sortPackagesOnTruck(truck1, packageHashTable, distanceObject)
truck2 = tools.sortPackagesOnTruck(truck2, packageHashTable, distanceObject)
truck3 = tools.sortPackagesOnTruck(truck3, packageHashTable, distanceObject)

# SET TIME FOR DEPARTURE
tools.setDepartureTime(truck1, packageHashTable, timedelta(hours = 8, minutes = 0))
tools.setDepartureTime(truck2, packageHashTable, timedelta(hours = 9, minutes = 5))
tools.setDepartureTime(truck3, packageHashTable, timedelta(hours = 10, minutes = 20))

#DELIVER PACKAGES
truck1, packageHashTable, distanceObject = tools.deliverPackage(truck1, packageHashTable, distanceObject)
truck2, packageHashTable, distanceObject = tools.deliverPackage(truck2, packageHashTable, distanceObject)
truck3, packageHashTable, distanceObject = tools.deliverPackage(truck3, packageHashTable, distanceObject)

#PRINT THE DELIVERY DETAILS
print('\n\n\nTruck 1 left at ',truck1.timeLeftHub,' and finished delivery at: ',truck1.runningTime)
print('Truck 1 mileage: ',round(truck1.mileage,1))
print('\nTruck 2 left at ',truck2.timeLeftHub,' and finished delivery at: ',truck2.runningTime)
print('Truck 2 mileage: ',round(truck2.mileage,1))
print('\nTruck 3 left at ',truck3.timeLeftHub,' and finished delivery at: ',truck3.runningTime)
print('Truck 3 mileage: ',round(truck3.mileage,1))
print('\nTotal Mileage: ', round((truck1.mileage+truck2.mileage+truck3.mileage),1))

#GO TO MAIN MENU
ui.mainMenu(packageHashTable)

raise SystemExit(0)





