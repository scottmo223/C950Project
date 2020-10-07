# Robert S Morales 000954923
# This is the User Interface

def checkPackageStatus():
    packageId = input('\nEnter the package ID: ')
    print('\nPlease use 24Hr time in this format: ####    ex: 1346')
    time = input('Enter the time: ')

    print(f'\nYou entered Package ID: {packageId}')
    print(f'You entered Time: {time}\n\n')

def welcomeScreen(truck):
    print('''



    Hello,

    Welcome to the WGUPS application by Robert Morales.
    
    
    I loaded your first package for you...
    ''')
    print('\tTruck 1 packages: ', truck.packagesOnTruck)

    print('''
    Now it\'s your turn.
    Get to work.
    
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
    
    nextPackagesToLoad = [package for package in input('\nEnter package numbers separated by a space and then press Enter.\n').split()]
    packagesNowOnTruck = len(nextPackagesToLoad) + len(truck.packagesOnTruck)
    if packagesNowOnTruck > truck.truckCapacity:
        numPackagesToRemove = packagesNowOnTruck - truck.truckCapacity
        nextPackagesToLoad = nextPackagesToLoad[:len(nextPackagesToLoad)-numPackagesToRemove]
        print(f'\n\n\n\n### Too many packages, I took off {numPackagesToRemove} packages for you. ###\n')
    for package in nextPackagesToLoad:
        if packageHashTable.packagesAtHub.count(package) == 0:
            print('\n\n\n\n!!! You entered a package not at the hub!\n')
            return truck, packageHashTable, True
        if nextPackagesToLoad.count(package) > 1:
            print('\n\n\n\n!!! You entered the same package twice!\n')
            return truck, packageHashTable, True

    truck.loadPackages(nextPackagesToLoad,packageHashTable)
    print('\n\nTruck 1 packages: ', truck.packagesOnTruck)
    print('\nPackages left to load: ', packageHashTable.packagesAtHub)
    spaceInTruck1 = truck.truckCapacity - len(truck.packagesOnTruck)
    print(f'\nTruck 1 can hold {spaceInTruck1} more packages. Load more?')

    keepLoading = input('Type y to load more or n to move on.\n')
    if keepLoading == 'y':
        return truck, packageHashTable, True
    else:
        return truck, packageHashTable, False

def autoPackageLoading(truck, packageHashTable):
    packagesToLoad = packageHashTable.packagesAtHub
    truckCapacity = truck.truckCapacity - len(truck.packagesOnTruck)
    nextPackagesToLoad = packagesToLoad[:truckCapacity]
    truck.loadPackages(nextPackagesToLoad,packageHashTable)
    print('\n\nTruck 1 packages: ', truck.packagesOnTruck)
    print('\nPackages left to load: ', packageHashTable.packagesAtHub)
    return truck, packageHashTable

def mainMenu():
    print('''
    
    Choose an option:
      1 Load packages onto truck 1
      2 Load packages onto truck 2
      3 Set time to send truck 1
      4 Set time to send truck 2
      5 Send trucks
      6 Detailed status of a package
      7 Status of all packages
      0 Quit the application
    ''')
    return input()
    
def setTruckDepartingTime():
    print('\n\nWhat time should the truck depart?')
    print('Please use 24Hr time in this format: ####    ex: 1346')
    userDepartureTime = input()
    hour = int(userDepartureTime[:2])
    minute = int(userDepartureTime[2:])
    return hour, minute


