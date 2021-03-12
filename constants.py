import colors as _co

N = 6

EMPTY_LIST = []

dp = {'F': 0, 'Q': 0, 'R': 0}
EMPTY_CELL = {'ID': 0, 'POS': (0, 0), **dp}

EXIT_MSG = _co.bcolors.OKBLUE + " Exiting program... " + _co.bcolors.ENDC
ENTER_MSG = "Press" + _co.bcolors.WARNING + " number " + _co.bcolors.ENDC + "to continue "

EMPTY_MATRIX = [
    [{'ID': 1, 'POS': (0, 0), **dp }, {'ID': 2, 'POS': (0, 1), **dp }, {'ID': 3, 'POS': (0, 2), **dp }, {'ID': 4, 'POS': (0, 3), **dp }, {'ID': 5, 'POS': (0, 4), **dp }, {'ID': 6, 'POS': (0, 5), **dp }],
    [{'ID': 7, 'POS': (1, 0), **dp }, {'ID': 8, 'POS': (1, 1), **dp }, {'ID': 9, 'POS': (1, 2), **dp }, {'ID': 10, 'POS': (1, 3), **dp }, {'ID': 11, 'POS': (1, 4), **dp }, {'ID': 12, 'POS': (1, 5), **dp }],
    [{'ID': 13, 'POS': (2, 0), **dp }, {'ID': 14, 'POS': (2, 1), **dp }, {'ID': 15, 'POS': (2, 2), **dp }, {'ID': 16, 'POS': (2, 3), **dp }, {'ID': 17, 'POS': (2, 4), **dp }, {'ID': 18, 'POS': (2, 5), **dp }],
    [{'ID': 19, 'POS': (3, 0), **dp }, {'ID': 20, 'POS': (3, 1), **dp }, {'ID': 21, 'POS': (3, 2), **dp }, {'ID': 22, 'POS': (3, 3), **dp }, {'ID': 23, 'POS': (3, 4), **dp }, {'ID': 24, 'POS': (3, 5), **dp }],
    [{'ID': 25, 'POS': (4, 0), **dp }, {'ID': 26, 'POS': (4, 1), **dp }, {'ID': 27, 'POS': (4, 2), **dp }, {'ID': 28, 'POS': (4, 3), **dp }, {'ID': 29, 'POS': (4, 4), **dp }, {'ID': 30, 'POS': (4, 5), **dp }],
    [{'ID': 31, 'POS': (5, 0), **dp }, {'ID': 32, 'POS': (5, 1), **dp }, {'ID': 33, 'POS': (5, 2), **dp }, {'ID': 34, 'POS': (5, 3), **dp }, {'ID': 35, 'POS': (5, 4), **dp }, {'ID': 36, 'POS': (5, 5), **dp }]
]
