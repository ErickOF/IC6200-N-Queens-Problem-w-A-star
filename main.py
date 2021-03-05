import numpy as np

import colors as _co
import constants as _c

# GLOBAL VARIABLES - remember to use -global-
matrix = np.array(_c.EMPTY_MATRIX.copy())

open_list = _c.EMPTY_LIST.copy()  # .copy() Prevents mutation
closed_list = _c.EMPTY_LIST.copy()
tentative_routes_list = _c.EMPTY_LIST.copy()

row = -1
col = -1

def addItemOpenList():
    for i in range(_c.N):
        for j in range(_c.N):
            cell = matrix[i][j]
            if(cell['F'] == 0):
                open_list.append(cell)
        print('\n')


def getFirstItemOpenList():
    if(open_list == _c.EMPTY_LIST):
        return _c.EMPTY_CELL
    else:
        return open_list[0]


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


def getRestrictions():
    print('Row [', row, '] Column [', col, ']')

    print('ID\t\t '+ _co.bcolors.OKGREEN + str(matrix[row][col]['ID']) + _co.bcolors.ENDC)

    print('Column\t\t', getIDs(matrix[:, col]))
    print('Row\t\t', getIDs(matrix[row, :]))

    diagonals = getDiagonals(np.flipud(matrix), (row, col))
    print('Diagonal 1\t', getIDs(diagonals[0]))

    print('Diagonal 2\t', getIDs(diagonals[1]))


def main():
    while(1):
        enter = input(_c.ENTER_MSG)

        if enter == '':
            print("ENTER...")
            # TODO: remove it
            addItemOpenList()  # F == 0
            print(open_list)

        elif enter == 'q':
            print(_c.EXIT_MSG)
            currentCell = getFirstItemOpenList()
            currentPos = currentCell['POS']
            print('currentPos :', currentPos)

            global row, col
            row = currentPos[0]
            col = currentPos[1]
            getRestrictions()
            break


main()
