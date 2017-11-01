from __future__ import print_function
from colours import Colours


class Board:

    """ Class for Board Printing"""

    def display(self, disp):  # printing of the board
        """Board being printed for the first time"""
        for i in range(2):
            for j in range(90):
                print(Colours.BLUE + "X", end='')
            print('\n')

        i = 0
        j = 0
        while i <= 29:
            flag = 1
            j = 0
            while j <= 80:
                if i % 4 == 0 or i % 4 == 1:
                    if disp[i][j] != 'B':
                        disp[i][j] = ' '
                        disp[i][j + 1] = ' '
                        disp[i][j + 2] = ' '
                        disp[i][j + 3] = ' '
                    j = j + 4
                else:
                    if flag == 1:
                        if disp[i][j] != 'B':
                            disp[i][j] = ' '
                            disp[i][j + 1] = ' '
                            disp[i][j + 2] = ' '
                            disp[i][j + 3] = ' '
                        flag = -1
                        j = j + 4
                    elif flag == -1:
                        flag = 1
                        j = j + 4
            i = i + 1
        for i in range(30):  # main board being printed with different colours
            for j in range(90):
                if disp[i][j] == 'X':
                    print(Colours.BLUE + "X", end='')
                elif disp[i][j] == 'B':
                    print(Colours.GREEN + "B", end='')
                elif disp[i][j] == 'E':
                    print(Colours.MAGENTA + "E", end='')
                elif disp[i][j] == '%':
                    print(Colours.ENDC + "%", end='')
                elif disp[i][j] >= 0 and disp[i][j] <= 3:
                    print(Colours.HEADER + str(disp[i][j]), end='')

                else:
                    print(disp[i][j], end='')
            print('\n')

        for i in range(2):
            for j in range(90):
                print(Colours.BLUE + "X", end='')
            print('\n')

    def output(self, disp):
        """Board being printed for the rest of the time"""
        for i in range(2):
            for j in range(90):
                print(Colours.BLUE + "X", end='')
            print('\n')

        for i in range(30):
            for j in range(90):
                if disp[i][j] == 'X':
                    print(Colours.BLUE + "X", end='')
                elif disp[i][j] == 'B':
                    print(Colours.GREEN + "B", end='')
                elif disp[i][j] == 'E':
                    print(Colours.MAGENTA + "E", end='')
                elif disp[i][j] == '%':
                    print(Colours.ENDC + "%", end='')
                elif disp[i][j] >= 0 and disp[i][j] <= 3:
                    print(Colours.HEADER + str(disp[i][j]), end='')
                else:
                    print(disp[i][j], end='')
            print('\n')

        for i in range(2):
            for j in range(90):
                print(Colours.BLUE + "X", end='')
            print('\n')
