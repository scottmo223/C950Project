# Robert S Morales 000954923
# This is the User Interface

def checkPackageStatus():
    packageId = input('\nEnter the package ID: ')
    print('\nPlease use 24Hr time in this format: ####    ex: 1346')
    time = input('Enter the time: ')

    print(f'\nYou entered Package ID: {packageId}')
    print(f'You entered Time: {time}\n\n')

print('''



Hello,

Welcome to the WGUPS application by Robert Morales.

In the Input below:
 * Press "s" to view the status of a package
 * Press "q" to quit the application

''')
actionEntered = input('Input: ')

if actionEntered == 's' or 'S':
    checkPackageStatus()



