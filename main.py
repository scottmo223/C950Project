# Robert S Morales 000954923

import hashTable
import tools
import Truck

packageFile = 'WGUPS Package File.csv'
distanceTable = 'WGUPS Distance Table.csv'

packageHashTable = tools.readCSVFile(packageFile) # This loads the data csv file into a hash object

#tools.checkPackageStatus(packageHashTable, '4')

distanceObject = tools.readCSVFile(distanceTable, True) # This loads the distance csv file into a hash object
# truck1 = Truck.Truck(1)
# truck1.loadPackage('4')
# truck1.loadPackage('2')
# truck1.loadPackage('1')
# print(truck1.packages)
# print(truck1.deliverPackage())
# print(truck1.deliverPackage())

print(tools.initialPackage(distanceObject))
print(tools.initialPackage(distanceObject,False))

# for i in distanceObject:
#     print(i)

#print(distanceObject) #2 dim array - array[searches down][searches across]
#print(distanceObject[4][0]) #This gives the ADDRESS of the 4th row

#print(tools.findShortestDistance(distanceObject[1][1],distanceObject[4]))

#print(tools.initialPackage(distanceObject))
