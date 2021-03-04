import constants as _c

matrix = _c.EMPTY_MATRIX

open_list = _c.LIST_EMPTY
closed_list = _c.LIST_EMPTY
tentative_routes_list = _c.LIST_EMPTY

print(matrix[0][0]['ID'])

open_list.append(matrix[0][0])
print(open_list)


done = False


def main():
    while(1):
        enter = input(_c.ENTER_MSG)

        if enter == '':
            print("ENTER...")

        elif enter == 'q':
            print(_c.EXIT_MSG)
            break


main()
