import colors as _co

LIST_EMPTY = []

dp = {'G': 0, 'H': 0, 'F': 0, 'P': ''}

EXIT_MSG = _co.bcolors.OKBLUE + " Exiting program... " + _co.bcolors.ENDC
ENTER_MSG = "Press" + _co.bcolors.WARNING + " ENTER " + _co.bcolors.ENDC + "to continue "

EMPTY_MATRIX = [
    [{'ID': 1, **dp }, {'ID': 2, **dp }, {'ID': 3, **dp }, {'ID': 4, **dp }, {'ID': 5, **dp }, {'ID': 6, **dp }],
    [{'ID': 7, **dp }, {'ID': 8, **dp }, {'ID': 9, **dp }, {'ID': 10, **dp }, {'ID': 11, **dp }, {'ID': 12, **dp }],
    [{'ID': 13, **dp }, {'ID': 14, **dp }, {'ID': 15, **dp }, {'ID': 16, **dp }, {'ID': 17, **dp }, {'ID': 18, **dp }],
    [{'ID': 19, **dp }, {'ID': 20, **dp }, {'ID': 21, **dp }, {'ID': 22, **dp }, {'ID': 23, **dp }, {'ID': 24, **dp }],
    [{'ID': 25, **dp }, {'ID': 26, **dp }, {'ID': 27, **dp }, {'ID': 28, **dp }, {'ID': 29, **dp }, {'ID': 30, **dp }],
    [{'ID': 31, **dp }, {'ID': 32, **dp }, {'ID': 33, **dp }, {'ID': 34, **dp }, {'ID': 35, **dp }, {'ID': 36, **dp }]
]

