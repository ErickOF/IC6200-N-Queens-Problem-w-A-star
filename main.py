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


def getCellsWithOutRestritionOrQueen():
    listWithOutRestrictionOrQueen = []
    for i in range(_c.N):
        for j in range(_c.N):
            cell = matrix[i][j]
            if(cell['R'] == 0 and cell['Q'] == 0):
                listWithOutRestrictionOrQueen.append(cell)
    return listWithOutRestrictionOrQueen


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


def setQueen(x, y):
    print('setQueen', end=' ')
    matrix[x][y]['Q'] = 1


def setRestriction(restrictions_list=[]):
    print('setRestriction', end=' ')
    for i in range(_c.N):
        for j in range(_c.N):
            if(matrix[i][j]['ID'] in restrictions_list):
                matrix[i][j]['R'] = 1


# def updateFeed(restrictions_list=[]):
#     print('updateFeed')
#     for i in range(_c.N):
#         for j in range(_c.N):
#             if(matrix[i][j]['ID'] in restrictions_list):
#                 matrix[i][j]['F'] += 1

def setFeed(restrictions_list=[]):
    print('setFeed', end=' ')
    for i in range(_c.N):
        for j in range(_c.N):
            if(matrix[i][j]['ID'] in restrictions_list):
                pos = matrix[i][j]['POS']
                length = getEndangeredCells(pos[0], pos[1])
                # print('ID> ', matrix[i][j]['ID'], ' [', length, ']')
                matrix[i][j]['F'] = length


def sorfListByFeed(feedList):
    print('sorfListByFeed', end=' ')
    feedList.sort(key=lambda x: x['F'])
    return feedList


def addItemClosesList(closedNode):
    print('closedNode ', closedNode, end='')
    closed_list.append(closedNode)


def addItemOpenList(newNode):
    print('newNode ', newNode, end='')
    open_list.insert(0, newNode)


def getFirstItemOpenList():
    if(open_list == _c.EMPTY_LIST):
        return _c.EMPTY_CELL
    else:
        return open_list[0]


def checkIfExistsOnClosedList():
    result = all(elem in [8, 9, 4, 6, 5, 1] for elem in [1, 5, 4, 6, 8, 9])
    if result:
        print('Yes, list1 contains all elements in list2', end='')
        return True
    else:
        print('No, list1 does not contains all elements in list2', end='')
        return False


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
    print('Row [', row, '] Column [', col, ']')

    print('ID\t\t ' + _co.bcolors.OKGREEN +
          str(matrix[row][col]['ID']) + _co.bcolors.ENDC)

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


def getRestrictions_TEST():
    for i in range(_c.N):
        for j in range(_c.N):
            # print('ID\t\t ' + _co.bcolors.OKGREEN + str(matrix[i][j]['ID']) + _co.bcolors.ENDC)

            cols = getIDs(matrix[:, j])
            rows = getIDs(matrix[i, :])

            # print('cols\t\t ', _co.bcolors.FAIL, matrix[:, j], _co.bcolors.ENDC)

            diagonals = getDiagonals(np.flipud(matrix), (i, j))
            diag_1 = getIDs(diagonals[0])
            diag_2 = getIDs(diagonals[1])

            list_restrictions = cols + rows + diag_1 + diag_2
            list_restrictions.sort()
            # print("🚀", str(matrix[i][j]['ID']), "🚀 list_restrictions", list_restrictions, '\n')


def main():
    iterations = 0
    queens = 0
    showRestrictions = True

    print(_co.bcolors.BOLD + 'ID' + '-' + 'Q' + '-' + 'R' +
          '-' + 'F' + '-' + _co.bcolors.ENDC, end='| ')

    # getRestrictions_TEST()

    while(1):

        print(_co.bcolors.OKCYAN + "\nIteration : " +
              str(iterations) + '\n' + _co.bcolors.ENDC)

        printMatrixQueens(showRestrictions)

        enter = input(_c.ENTER_MSG)

        if enter == '':
            iterations += 1
            list_without_RQ = getCellsWithOutRestritionOrQueen()
            list_Ids = getIDs_V2(list_without_RQ)
            setFeed(list_Ids)

            sortListByFeed = sorfListByFeed(list_without_RQ)

            if(len(open_list) == 0):
                for a in sortListByFeed:
                    open_list.insert(len(open_list), [a])

            myCell = open_list[0][-1]
            print('\myCell', myCell)

            closed_list.insert(len(closed_list), open_list[0])
            print('\closed_list', closed_list)

            currentPos = myCell['POS']

            global row, col
            row = currentPos[0]
            col = currentPos[1]

            setQueen(row, col)

            restrictions = getRestrictions()
            setRestriction(restrictions)

            printMatrixExtraInfo()
            # printMatrixFeed()

            if(len(open_list) > 0):
                del open_list[0]
            else:
                print('Open List Empty..... Final')
                break

            print('\open_list', open_list)

            # TODO Generate new path and add to current Node, to end.
            # TODO Validate new path on Closed List
            # TODO Check if with Have 6 Queens, by length of last item on Closes List

        elif enter == 'q':
            print(_c.EXIT_MSG)
            currentCell = getFirstItemOpenList()
            break


main()
