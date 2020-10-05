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
    nextPackagesToLoad = [package for package in input('\nEnter package numbers separated by a space and then press Enter.\n').split()]
    #check if any entered package is not at the hub
    for package in nextPackagesToLoad:
        if packageHashTable.packagesAtHub.count(package) == 0:
            print('\n!!! You entered a package not at the hub!\n')
            manualPackageLoading(truck, packageHashTable)
        if nextPackagesToLoad.count(package) > 1:
            print('\n!!! You enetered the same package twice!\n')
            manualPackageLoading(truck, packageHashTable)

    truck.loadPackages(nextPackagesToLoad,packageHashTable)
    print('\n\nTruck1 packages: ', truck.packagesOnTruck)
    print('\nPackages left to load: ', packageHashTable.packagesAtHub)
    spaceInTruck1 = truck.truckCapacity - len(truck.packagesOnTruck)
    print(f'\nTruck1 can hold {spaceInTruck1} more packages. Load more?')

    keepLoading = input('Type y to load more or n to move on.\n')
    if keepLoading == 'y':
        manualPackageLoading(truck, packageHashTable)
    else:
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
    



