tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            longestWordLength = 0
            if longestWordLength < len(table[i][j]):
                longestWordLength = len(table[i][j])
        colWidths[i] = longestWordLength

    for rowNum in range(len(table[0])):
        columnNum = 0
        while columnNum < len(table):
            print(table[columnNum][rowNum].rjust(colWidths[columnNum]), end=' ')
            columnNum += 1
        print('')

printTable(tableData)
