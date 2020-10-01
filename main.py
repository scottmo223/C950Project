# Robert S Morales 000954923

import hashTable
import tools

packageFile = 'WGUPS Package File.csv'
distanceTable = 'WGUPS Distance Table.csv'

dataObject = tools.readCSVFile(packageFile) # This loads the data csv file into a hash object
distanceObject = tools.readCSVFile(distanceTable, True) # This loads the distance csv file into a hash object
truck1 = []
#truck1.append()

# for i in distanceObject:
#     print(i)

#print(distanceObject[4][1])
#print(tools.findShortestDistance(distanceObject[1][1],distanceObject[4]))

print(tools.loadTruck1FirstPackage(distanceObject))
