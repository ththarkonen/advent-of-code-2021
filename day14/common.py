
def parseData( lines ):

    template = ""
    insertions = {}

    counter = 0
    for line in lines:

        line = line.replace("\n", "")
        line = line.replace(" ", "")
        
        if counter == 0:

            template = line
            counter = 1
            continue

        elif not line: continue

        line = line.split("->")
        bond = line[0]
        insertion = line[1]

        insertions[ bond ] = insertion

    return ( template, insertions)

def computeBondCounts( template ):

    bonds = {}
    nAtoms = len( template )

    for ii in range( nAtoms - 1 ):

        bond_jj = template[ii:ii + 2]

        if bond_jj in bonds: bonds[ bond_jj ] += 1
        else: bonds[ bond_jj ] = 1

    return bonds

def updateBondCounts( bonds, insertions):

    updatedBonds = bonds.copy()

    for bond in bonds:

        if bond not in insertions: continue

        leftAtom = bond[0]
        rightAtom = bond[1]
        bondCount = bonds[bond]

        newAtom = insertions[ bond ]

        newLeftBond = leftAtom + newAtom
        newRightBond = newAtom + rightAtom

        if newLeftBond not in updatedBonds: updatedBonds[newLeftBond] = bondCount
        else: updatedBonds[newLeftBond] += bondCount

        if newRightBond not in updatedBonds: updatedBonds[newRightBond] = bondCount
        else: updatedBonds[newRightBond] += bondCount

        updatedBonds[bond] -= bondCount

    return updatedBonds

def countAtoms( bonds, firstLastAtoms):

    atomCounts = {}
    firstAtom = firstLastAtoms[0]
    lastAtom = firstLastAtoms[1]

    for bond in bonds:

        leftAtom = bond[0]
        rightAtom = bond[1]
        atomCount = bonds[bond]

        if leftAtom not in atomCounts: atomCounts[leftAtom] = atomCount
        else: atomCounts[leftAtom] += atomCount

        if rightAtom not in atomCounts: atomCounts[rightAtom] = atomCount
        else: atomCounts[rightAtom] += atomCount

    atomCounts[ firstAtom ] += 1
    atomCounts[ lastAtom ] += 1

    for bond in atomCounts:
        atomCounts[bond] = atomCounts[bond] / 2

    return atomCounts

