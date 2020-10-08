# Robert S Morales 000954923
# This is the User Interface

import tools

def welcomeScreen():
    print('''



    Hello,

    Welcome to the WGUPS application by Robert Morales.
    
    
    * Type 1 to get started
    * Type anything else to quit the application

    ''')
    return input()
 
def manualPackageLoading(truck, packageHashTable):
    if len(packageHashTable.packagesAtHub) < 1:
        print('There are no more packages left to load.')
        return truck, packageHashTable, False
    if truck.truckCapacity - len(truck.packagesOnTruck) < 1:
        print('There is no more room on the truck.')
        return truck, packageHashTable, False

    print('\nPackages left to load:\n', packageHashTable.packagesAtHub)
def checkPackageStatus(packageHashTable):
    packageId = input('\nEnter the package ID: ')
    print('\nPlease use 24Hr time in this format: ####    ex: 1346')
    package = packageHashTable.getItem(packageId)
    
    print()
    print('id: '.ljust(11, ' '), package.packageId)
    print('address: '.ljust(11, ' '), package.deliveryAddress)
    print('city: '.ljust(11, ' '), package.deliveryCity)
    print('zip: '.ljust(11, ' '), package.deliveryZipcode)
    print('weight: '.ljust(11, ' '), package.packageWeight)
    print('status: '.ljust(11, ' '), package.deliveryStatus)
    print('deadline: '.ljust(11, ' '), package.deliveryDeadline)
    print('delivered:'.ljust(11, ' '), package.deliveryTime)

# def manualPackageLoading(truck, packageHashTable):
#     if len(packageHashTable.packagesAtHub) < 1:
#         print('There are no more packages left to load.')
#         return truck, packageHashTable, False
#     if truck.truckCapacity - len(truck.packagesOnTruck) < 1:
#         print('There is no more room on the truck.')
#         return truck, packageHashTable, False

#     print('\nPackages left to load:\n', packageHashTable.packagesAtHub)
    
#     nextPackagesToLoad = [package for package in input('\nEnter package numbers separated by a space and then press Enter.\n').split()]
#     packagesNowOnTruck = len(nextPackagesToLoad) + len(truck.packagesOnTruck)
#     if packagesNowOnTruck > truck.truckCapacity:
#         numPackagesToRemove = packagesNowOnTruck - truck.truckCapacity
#         nextPackagesToLoad = nextPackagesToLoad[:len(nextPackagesToLoad)-numPackagesToRemove]
#         print(f'\n\n\n\n### Too many packages, I took off {numPackagesToRemove} packages for you. ###\n')
#     for package in nextPackagesToLoad:
#         if packageHashTable.packagesAtHub.count(package) == 0:
#             print('\n\n\n\n!!! You entered a package not at the hub!\n')
#             return truck, packageHashTable, True
#         if nextPackagesToLoad.count(package) > 1:
#             print('\n\n\n\n!!! You entered the same package twice!\n')
#             return truck, packageHashTable, True

#     truck.loadPackages(nextPackagesToLoad,packageHashTable)
#     print('\n\nTruck 1 packages: ', truck.packagesOnTruck)
#     print('\nPackages left to load: ', packageHashTable.packagesAtHub)
#     spaceInTruck1 = truck.truckCapacity - len(truck.packagesOnTruck)
#     print(f'\nTruck 1 can hold {spaceInTruck1} more packages. Load more?')

#     keepLoading = input('Type y to load more or n to move on.\n')
#     if keepLoading == 'y':
#         return truck, packageHashTable, True
#     else:
#         return truck, packageHashTable, False

def autoPackageLoading(truck, packageHashTable):
    packagesToLoad = packageHashTable.packagesAtHub
    truckCapacity = truck.truckCapacity - len(truck.packagesOnTruck)
    nextPackagesToLoad = packagesToLoad[:truckCapacity]
    truck.loadPackages(nextPackagesToLoad,packageHashTable)
    print(f'\n\nPackages on Truck {truck.truckId} : ', truck.packagesOnTruck)
    # print('\nPackages left to load: ', packageHashTable.packagesAtHub)  #!!!! Can delete this!!!
    return truck, packageHashTable

def mainMenu(packageHashTable):
    userInput = '1'
    while userInput in ['1','2','3']:
        print('''
        
        Choose an option:
            1 Detailed status of a package
            2 Status of all packages
            3 Choose time to check package statuses
            0 Quit the application
        ''')
        userInput = input()

        if userInput == '1':
            checkPackageStatus(packageHashTable)
        elif userInput == '2':
            tools.statusOfAllPackages(packageHashTable)
        elif userInput == '3':
            pass
    
def setTruckDepartingTime():
    print('\n\nWhat time should the truck depart?')
    print('Please use 24Hr time in this format: ####    ex: 1346')
    userDepartureTime = input()
    hour = int(userDepartureTime[:2])
    minute = int(userDepartureTime[2:])
    return hour, minute


