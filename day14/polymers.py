
import common

file = open("./day14/data.txt")
lines = file.readlines()

( template, insertions) = common.parseData( lines )
bonds = common.computeBondCounts( template )

firstLastAtoms = ( template[0], template[-1])

#steps = 10
steps = 40

for ii in range( steps ):
    bonds = common.updateBondCounts( bonds, insertions)

atomCounts = common.countAtoms( bonds, firstLastAtoms)
atomCounts = sorted( atomCounts.items(), key = lambda x:x[1] )

leastCommon = int( atomCounts[0][1] )
mostCommon = int( atomCounts[-1][1] )

print( mostCommon - leastCommon )