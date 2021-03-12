import time
import numpy as np
import constants as _c

from colors import bcolors as bc

# GLOBAL VARIABLES - remember to use -global-
matrix = np.array(_c.EMPTY_MATRIX.copy())

open_list = _c.EMPTY_LIST.copy()  # .copy() Prevents mutation
closed_list = _c.EMPTY_LIST.copy()  # List of Lists
tentative_routes_list = _c.EMPTY_LIST.copy()

row = -1
col = -1

under_green = bc.UNDERLINE + bc.OKGREEN

# ____ PRINTS ____


def printMatrixQueens(showRestrictions=False):
    for i in range(_c.N):
        print('| ', end='')
        for j_ in range(_c.N):
            cell = matrix[i][j_]
            if(showRestrictions and cell['R'] > 0):
                print(bc.WARNING + '~ ' + bc.ENDC, end='| ')
            elif(cell['Q'] == 1):
                print(bc.OKGREEN + 'Q ' + bc.ENDC, end='| ')
            else:
                print('  ', end='| ')
        print('\n')


def printMatrixFeed():
    print('\n')
    for i_ in range(_c.N):
        print('| ', end='')
        for j in range(_c.N):
            cell = matrix[i_][j]
            print(bc.WARNING +
                  str(cell['F']) + ' ' + bc.ENDC, end='| ')
        print('\n')


def printMatrixExtraInfo():
    for i in range(_c.N):
        print('| ', end='')
        for j in range(_c.N):
            cell = matrix[i][j]
            print(bc.BOLD + str(cell['ID']) + '-' + str(cell['Q']) + '-' +
                  str(cell['R']) + '-' + str(cell['F']) + '-' + bc.ENDC, end='| ')
        print('\n')


def printList(listToPrint):
    print(bc.HEADER + '[' + bc.ENDC, end='')

    lenList = len(listToPrint)
    counter_ = 0
    for item in listToPrint:
        counter_ += 1
        print(bc.HEADER + '[' + bc.ENDC, end='')
        lenItem = len(item)
        count_list = 0
        for i_ in item:
            print(str(i_['ID']), end='')
            count_list += 1

            if(lenItem != count_list):
                print(', ', end='')

        if(lenList != counter_):
            print(bc.HEADER + ']' + bc.ENDC+', ', end='')

        else:
            print(bc.HEADER + ']' + bc.ENDC, end='')

    print(bc.HEADER + ']' + bc.ENDC, end='\n\n')

# ____ RE-SETS ____


def resetMatrix(followCell):
    for i in range(_c.N):
        for a in range(_c.N):
            matrix[i][a] = {'ID': matrix[i][a]['ID'],
                            'POS': matrix[i][a]['POS'],
                            'F': 0,
                            'Q': 0,
                            'R': 0}
    # TODO: set news Queens and set Restrictions
    # print('//////////////////////////////////////////')
    # printMatrixExtraInfo()
    # print(getIDs_V2(followCell))
    # print('//////////////////////////////////////////')

    for queen in followCell:
        global row, col
        row = queen['POS'][0]
        col = queen['POS'][1]

        # print('>> ', queen['ID'], ' (', queen['POS']
        #       [0], ', ', queen['POS'][1], ')')
        setQueen(row, col)

        # printMatrixQueens(True)
        # print('\n')

        # print('//////////////////////////////////////////')

        restrictions = getRestrictions()
        # print('<><><><><><><><><> >> restrictions : \n', restrictions)
        setRestriction(restrictions)

        # printMatrixQueens(True)


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

    num = matrix[i][j]['ID']

    if num in diag_1:
        diag_1.remove(num)
    if num in diag_2:
        diag_2.remove(num)

    list_restrictions = diag_1 + diag_2
    return len(list_restrictions)

def removeDuplicates(array):
  return list(dict.fromkeys(array))

def getALLRestrictions():
    list_restrictions = []
    for i_cell in range(_c.N):
        for j_cell in range(_c.N):
            if(matrix[i_cell][j_cell]['Q'] == 1):
                print('ID <', matrix[i_cell][j_cell]['ID'], '>')
                cols = getIDs(matrix[:, col])
                # print('cols > ', cols)
                rows = getIDs(matrix[row, :])
                # print('rows > ', rows)

                diagonals = getDiagonals(np.flipud(matrix), (row, col))
                diag_1 = getIDs(diagonals[0])
                # print('diag_1 > ', diag_1)
                diag_2 = getIDs(diagonals[1])
                # print('diag_2 > ', diag_2)

                list_restrictions = cols + rows + diag_1 + diag_2  # ANALIZAR SUMAS DE ARRAYS
                # print("🚀🚀🚀🚀" + str(matrix[row][col]['ID']),
                #       "🚀 list_restrictions", list_restrictions)

                list_restrictions.sort()
                # print("🚀🚀🚀🚀" + str(matrix[row][col]['ID']), "🚀 list_restrictions.sort()", list_restrictions)
    #remove repetidos
    # print('list_restrictions: ', list_restrictions, end='')
    listWithOutDuplicates = removeDuplicates(list_restrictions)
    # print('listWithOutDuplicates: ', listWithOutDuplicates, end='')

    return listWithOutDuplicates

def getRestrictions():
    cols = getIDs(matrix[:, col])
    # print('cols > ', cols)
    rows = getIDs(matrix[row, :])
    # print('rows > ', rows)

    diagonals = getDiagonals(np.flipud(matrix), (row, col))
    diag_1 = getIDs(diagonals[0])
    # print('diag_1 > ', diag_1)
    diag_2 = getIDs(diagonals[1])
    # print('diag_2 > ', diag_2)

    list_restrictions = cols + rows + diag_1 + diag_2  # ANALIZAR SUMAS DE ARRAYS
    # print("🚀🚀🚀🚀" + str(matrix[row][col]['ID']),
    #       "🚀 list_restrictions", list_restrictions)

    list_restrictions.sort()
    # print("🚀🚀🚀🚀" + str(matrix[row][col]['ID']),
    #       "🚀 list_restrictions.sort()", list_restrictions)
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
    sortDecendents = [0]
    followCell = {}
    done = False

    while(done == False):
        print(bc.OKCYAN + "\nIteration : " + str(iterations) + '\n' + bc.ENDC)

        printMatrixQueens(showRestrictions)


        try:
            enter = int(input(_c.ENTER_MSG))

            if(type(enter) == int):

                iterations_loop = enter - 1
                while(iterations_loop>=0 and done == False):
                    iterations_loop -= 1
                    # if(sortDecendents == []):
                    #     print(bc.OKGREEN + "RESET\n" + bc.ENDC)
                    #     # resetMatrix(closed_list[-2])
                    #     resetMatrix(followCell)

                    #     # printMatrixExtraInfo()

                    iterations += 1
                    list_without_RQ = getCellsWithOutRestritionOrQueen()  # Step 1

                    list_Ids = getIDs_V2(list_without_RQ)
                    setFeed(list_Ids)  # Step 2

                    s = sortListByFeed(list_without_RQ)

                    if(len(open_list) == 0):
                        for a in s:
                            open_list.insert(len(open_list), [a])

                    myCell = open_list[0][-1]
                    # print('Current Cell', myCell)

                    queens = len(open_list[0])

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

                    print(under_green + "\nCurrent Trajectory :" + bc.ENDC + " ", end='')
                    print(getIDs_V2(open_list[0]), '\n')

                    followCell = closed_list[-1]  # Array

                    if(sortDecendents == []):
                        print(bc.OKGREEN + "RESET\n" + bc.ENDC)
                        # resetMatrix(closed_list[-2])
                        resetMatrix(followCell)

                        # printMatrixExtraInfo()

                    if(len(open_list) > 0):
                        del open_list[0]
                    else:
                        print('Open List Empty..... Final')
                        break

                    # print(under_green + "Current Cell :" + bc.ENDC + ' ' +
                    #       str(myCell['ID']) + '\n')

                    # print(bc.HEADER + 'Open List ' + bc.ENDC, end=': ')
                    # printList(open_list)

                    # print(bc.HEADER + 'Closed List ' + bc.ENDC, end=': ')
                    # printList(closed_list)

                    newDecendents = getCellsWithOutRestritionOrQueen()
                    # print('New Decendents', getIDs_V2(newDecendents))

                    sortDecendents = sortListByFeed(newDecendents)
                    # print('Sort New Decendents', getIDs_V2(sortDecendents))

                    # TODO Generate new path and add to current Node, to start.
                    # TODO Validate new path on Closed List
                    # TODO Check if with Have 6 Queens, by length of last item on Closes List
                    # TODO Get ramdon cell with less feed

                    listNewsNodes = []

                    for decendet in sortDecendents:
                        b = followCell.copy()
                        b.append(decendet)
                        listNewsNodes.append(b)

                    candidates = listNewsNodes.copy()[::-1]

                    # print(bc.HEADER + 'Candites ' + bc.ENDC, end=': ')
                    # printList(candidates[::-1])

                    for cand in candidates:
                        result = all(elem in cand for elem in open_list)
                        if (result == False):
                            open_list.insert(0, cand)
                        else:
                            print(
                                'Canditado en lista de abierto, no se tomara en cuanta.......')

                    print(bc.OKGREEN + 'Queens : ' + bc.ENDC, str(queens))

                    if(queens == 6):
                        print(bc.FAIL + "\nCurrent Trajectory :" + bc.ENDC + " ", end='')
                        print(getIDs_V2(followCell), '\n')
                        done = True

            # elif enter == 'q':
            #     print(_c.EXIT_MSG)
            #     break
        except:
            print(_c.EXIT_MSG)
            break

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
