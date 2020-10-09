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
 
def checkPackageStatus(packageHashTable):
    packageId = input('\nEnter the package ID: ')
    package = packageHashTable.getItem(packageId)
    
    print('\nid: '.ljust(11, ' '), package.packageId)
    print('address: '.ljust(11, ' '), package.deliveryAddress)
    print('city: '.ljust(11, ' '), package.deliveryCity)
    print('zip: '.ljust(11, ' '), package.deliveryZipcode)
    print('weight: '.ljust(11, ' '), package.packageWeight)
    print('status: '.ljust(11, ' '), package.deliveryStatus)
    print('departed:'.ljust(11, ' '), package.departureTime)
    print('delivered:'.ljust(11, ' '), package.deliveryTime)
    print('deadline: '.ljust(11, ' '), package.deliveryDeadline)

def autoPackageLoading(truck, packageHashTable):
    packagesToLoad = packageHashTable.packagesAtHub
    truckCapacity = truck.truckCapacity - len(truck.packagesOnTruck)
    nextPackagesToLoad = packagesToLoad[:truckCapacity]
    truck.loadPackages(nextPackagesToLoad,packageHashTable)
    print(f'\n\nPackages on Truck {truck.truckId} : ', truck.packagesOnTruck)
    return truck, packageHashTable

def mainMenu(packageHashTable):
    userInput = '1'
    while userInput in ['1','2','3']:
        print('''
        
        Choose an option:
            1 Current detailed status of a package
            2 Current status of all packages
            3 Status check at a given time
            0 Quit the application
        ''')
        userInput = input()

        if userInput == '1':
            checkPackageStatus(packageHashTable)
        elif userInput == '2':
            tools.statusOfAllPackages(packageHashTable)
        elif userInput == '3':
            tools.statusOfAllPackagesAtGivenTime(packageHashTable)