import numpy as np

import colors as _co
import constants as _c

# GLOBAL VARIABLES - remember to use -global-
matrix = np.array(_c.EMPTY_MATRIX.copy())

open_list = _c.EMPTY_LIST.copy()  # .copy() Prevents mutation
closed_list = _c.EMPTY_LIST.copy()  # List of Lists
tentative_routes_list = _c.EMPTY_LIST.copy()

row = -1
col = -1

# ____ PRINTS ____


def printMatrixQueens(showRestrictions=False):
    for i in range(_c.N):
        print('| ', end='')
        for j in range(_c.N):
            cell = matrix[i][j]
            if(showRestrictions and cell['R'] > 0):
                print(_co.bcolors.WARNING + '~ ' + _co.bcolors.ENDC, end='| ')
            elif(cell['Q'] == 1):
                print(_co.bcolors.OKGREEN + 'Q ' + _co.bcolors.ENDC, end='| ')
            else:
                print('  ', end='| ')
        print('\n')


def printMatrixFeed():
    print('\n')
    for i in range(_c.N):
        print('| ', end='')
        for j in range(_c.N):
            cell = matrix[i][j]
            print(_co.bcolors.WARNING +
                  str(cell['F']) + ' ' + _co.bcolors.ENDC, end='| ')
        print('\n')


def printMatrixExtraInfo():
    for i in range(_c.N):
        print('| ', end='')
        for j in range(_c.N):
            cell = matrix[i][j]
            print(_co.bcolors.BOLD + str(cell['ID']) + '-' + str(cell['Q']) + '-' +
                  str(cell['R']) + '-' + str(cell['F']) + '-' + _co.bcolors.ENDC, end='| ')
        print('\n')


def printClosedList():
    print('Closed List : [', end='')

    for item in closed_list:
        if(type(item) is list):
            for i_ in item:
                print(str(i_['ID']) + ',', end='')
        else:
            print(str(item['ID']) + ',', end='')
    print(']')


def printOpenList():
    print('Open List : [', end='')

    for item in open_list:
        if(type(item) is list):
            print('[', end='')
            for i_ in item:
                print(str(i_['ID']) + ',', end='')
            print(']', end=',')
        else:
            print(str(item['ID']) + ',', end='')
    print(']')

# ____ SETS ____


def setQueen(x, y):
    # print('setQueen', end=' ')
    matrix[x][y]['Q'] = 1


def setRestriction(restrictions_list=[]):
    # print('setRestriction', end=' ')
    for i in range(_c.N):
        for j in range(_c.N):
            if(matrix[i][j]['ID'] in restrictions_list):
                matrix[i][j]['R'] = 1


def setFeed(restrictions_list=[]):
    # print('setFeed', end=' ')
    for i in range(_c.N):
        for j in range(_c.N):
            if(matrix[i][j]['ID'] in restrictions_list):
                pos = matrix[i][j]['POS']
                length = getEndangeredCells(pos[0], pos[1])
                # print('ID> ', matrix[i][j]['ID'], ' [', length, ']')
                matrix[i][j]['F'] = length

# ____ GETS ____


def getCellsWithOutRestritionOrQueen():
    listWithOutRestrictionOrQueen = []
    for i in range(_c.N):
        for j in range(_c.N):
            cell = matrix[i][j]
            if(cell['R'] == 0 and cell['Q'] == 0):
                listWithOutRestrictionOrQueen.append(cell)
    return listWithOutRestrictionOrQueen


def getDiagonals(matrix, pos):
    row_d, col_d = pos
    nrows = len(matrix)
    ncols = len(matrix[0]) if nrows > 0 else 0
    # First diagonal
    d1_i, d1_j = nrows - 1 - max(row_d - col_d, 0), max(col_d - row_d, 0)
    d1_len = min(d1_i + 1, ncols - d1_j)
    diag1 = [matrix[d1_i - k][d1_j + k] for k in range(d1_len)]
    # Second diagonal
    t = min(row_d, ncols - col_d - 1)
    d2_i, d2_j = nrows - 1 - row_d + t, col_d + t
    d2_len = min(d2_i, d2_j) + 1
    diag2 = [matrix[d2_i - k][d2_j - k] for k in range(d2_len)]
    return (diag1, diag2)


def getIDs(array):
    ids_list = _c.EMPTY_LIST.copy()

    for item in array:
        if(item['ID'] != matrix[row][col]['ID']):
            ids_list.append(item['ID'])

    return ids_list


def getIDs_V2(array):
    ids_list = _c.EMPTY_LIST.copy()

    for item in array:
        ids_list.append(item['ID'])

    return ids_list


def getEndangeredCells(i, j):
    diagonals = getDiagonals(np.flipud(matrix), (i, j))
    diag_1 = getIDs_V2(diagonals[0])
    diag_2 = getIDs_V2(diagonals[1])

    # print('diag_1 ', diag_1, ' -- diag_2 ', diag_2, '')

    num = matrix[i][j]['ID']

    if num in diag_1:
        diag_1.remove(num)
    if num in diag_2:
        diag_2.remove(num)

    # print('diag_1 ', diag_1, ' -- diag_2 ', diag_2, '')

    list_restrictions = diag_1 + diag_2

    # print('list_restrictions ', list_restrictions)

    return len(list_restrictions)


def getRestrictions():
    # print('Row [', row, '] Column [', col, ']')

    # print('ID\t\t ' + _co.bcolors.OKGREEN +
    #       str(matrix[row][col]['ID']) + _co.bcolors.ENDC)

    cols = getIDs(matrix[:, col])
    rows = getIDs(matrix[row, :])

    # print('cols\t\t ', _co.bcolors.OKGREEN, matrix[:, col], _co.bcolors.ENDC)

    diagonals = getDiagonals(np.flipud(matrix), (row, col))
    diag_1 = getIDs(diagonals[0])
    diag_2 = getIDs(diagonals[1])

    list_restrictions = cols + rows + diag_1 + diag_2
    list_restrictions.sort()
    # print("🚀🚀🚀🚀" + str(matrix[row][col]['ID']), "🚀 list_restrictions", list_restrictions)
    return list_restrictions


# ____ SORT ____
def sortListByFeed(feedList):
    # print('sortListByFeed', end=' ')
    feedList.sort(key=lambda x: x['F'])
    return feedList

# ____ ADDS ____


def addItemClosesList(closedNode):
    print('closedNode ', closedNode, end='')
    closed_list.append(closedNode)


def addItemOpenList(newNode):
    print('newNode ', newNode, end='')
    open_list.insert(0, newNode)

# ____ VALIDATIONS ____


def checkIfExistsOnClosedList():
    result = all(elem in [8, 9, 4, 6, 5, 1] for elem in [1, 5, 4, 6, 8, 9])
    if result:
        print('Yes, list1 contains all elements in list2', end='')
        return True
    else:
        print('No, list1 does not contains all elements in list2', end='')
        return False

# ____ MAIN ____


def main():
    iterations = 0
    queens = 0
    showRestrictions = True

    while(1):
        print(_co.bcolors.OKCYAN + "\nIteration : " +
              str(iterations) + '\n' + _co.bcolors.ENDC)

        printMatrixQueens(showRestrictions)

        enter = input(_c.ENTER_MSG)

        if enter == '':
            iterations += 1
            list_without_RQ = getCellsWithOutRestritionOrQueen()  # Step 1

            list_Ids = getIDs_V2(list_without_RQ)
            setFeed(list_Ids)  # Step 2

            s = sortListByFeed(list_without_RQ)

            if(len(open_list) == 0):
                for a in s:
                    open_list.insert(len(open_list), [a])

            myCell = open_list[0][-1]
            print('Current Cell', myCell)

            closed_list.insert(len(closed_list), open_list[0])

            currentPos = myCell['POS']

            global row, col
            row = currentPos[0]
            col = currentPos[1]

            setQueen(row, col)

            restrictions = getRestrictions()
            setRestriction(restrictions)

            # printMatrixExtraInfo()
            # printMatrixFeed()

            if(len(open_list) > 0):
                del open_list[0]
            else:
                print('Open List Empty..... Final')
                break

            printOpenList()
            printClosedList()

            newDecendents = getCellsWithOutRestritionOrQueen()
            print('New Decendents', getIDs_V2(newDecendents))

            sortDecendents = sortListByFeed(newDecendents)
            print('Sort New Decendents', getIDs_V2(sortDecendents))

            # TODO Generate new path and add to current Node, to start.
            # TODO Validate new path on Closed List
            # TODO Check if with Have 6 Queens, by length of last item on Closes List

            listNewsNodes = []

            a = closed_list[-1]  # Array
            for decendet in sortDecendents:
                b = a.copy()
                b.append(decendet)
                listNewsNodes.append(b)

            bb = listNewsNodes.copy()[::-1]

            for b in bb:
                open_list.insert(0, b)

            printOpenList()
        elif enter == 'q':
            print(_c.EXIT_MSG)
            break


main()
