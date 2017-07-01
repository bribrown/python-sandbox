# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with
# each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:
#
#
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
# Your printTable() function would print the following:
#
#
#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose

def reworkTable(originalTable):
    y = 0
    nestedTable = []
    newTable = []

    while y < 4:
        for i in range(len(originalTable)):
            nv = originalTable[i][y]
            nestedTable.append(nv)
            i += 1
        newTable.append(nestedTable)
        nestedTable = []
        y += 1

    return (newTable)

def printTable(userLists):
    y = 0

    while y < 3:
        for i in range(len(userLists)):
            x = userLists[i][y]
            x = x.rjust(15,' ')
            userLists[i][y] = x
            i += 1
        y += 1

    for i in range(len(userLists)):
        x = userLists[i]
        z = ''.join(x)
        print(z)
        i += 1

def main():

    tableData = [['Flyers', 'Penguins', 'Capitals', 'Rangers'],
                 ['Maple Leafs', 'Sabres', 'Bruins', 'Canadiens'],
                 ['Red Wings', 'Blackhawks', 'Predators', 'Blues']]


    printTable(reworkTable(tableData))


if __name__ == "__main__": main()