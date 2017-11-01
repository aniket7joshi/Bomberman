"""Enemy defined"""
import random
from board import Board


class Enemy(Board):
    """Enemy class begins"""

    def __init__(self):  # initialisation
        self.enemies = []
        self.left_x = 0
        self.left_y = 0

    def generate_enemies(self, disp, i):
        """enemies being generated randomly"""
        pointer = 0
        while pointer < i:
            flag = -1
            while flag != 1:
                xcor = random.randint(2, 14)
                xcor = xcor * 2
                ycor = random.randint(2, 20)
                ycor = ycor * 4
                if disp[xcor][ycor] == ' ':
                    disp[xcor][ycor] = 'E'
                    disp[xcor][ycor + 1] = 'E'
                    disp[xcor][ycor + 2] = 'E'
                    disp[xcor][ycor + 3] = 'E'
                    disp[xcor + 1][ycor] = 'E'
                    disp[xcor + 1][ycor + 1] = 'E'
                    disp[xcor + 1][ycor + 2] = 'E'
                    disp[xcor + 1][ycor + 3] = 'E'
                    flag = 1
                    self.enemies.append(xcor)
                    self.enemies.append(ycor)
            pointer = pointer + 1
    def change(self, i, disp):
        """change of disp array after enemy movement"""
        disp[self.enemies[2 * i]][self.enemies[2 * i + 1]] = 'E'
        disp[self.enemies[2 * i]][self.enemies[2 * i + 1] + 1] = 'E'
        disp[self.enemies[2 * i]][self.enemies[2 * i + 1] + 2] = 'E'
        disp[self.enemies[2 * i]][self.enemies[2 * i + 1] + 3] = 'E'
        disp[self.enemies[2 * i] + 1][self.enemies[2 * i + 1]] = 'E'
        disp[self.enemies[2 * i] + 1][self.enemies[2 * i + 1] + 1] = 'E'
        disp[self.enemies[2 * i] + 1][self.enemies[2 * i + 1] + 2] = 'E'
        disp[self.enemies[2 * i] + 1][self.enemies[2 * i + 1] + 3] = 'E'

    def move(self, i, disp, bman):
        """random movement of enemy"""
        xvar = random.randint(1, 4)
        flag = 0
        while flag != 1:
            if self.enemies[2 * i] != -1 and self.enemies[2 * i + 1] != -1:
                if self.enemies[2 * i] == bman.posl() and self.enemies[2 * i + 1] == bman.posr():
                    print "You are dead"
                    exit(0)
                if xvar == 1:  # downwards movement
                    if self.enemies[2 * i] + 3 <= 29 and (disp[self.enemies[2 * i] + 2][self.enemies[2 * i + 1]] == ' ' or disp[self.enemies[2 * i] + 2][self.enemies[2 * i + 1]] == 'E' or disp[self.enemies[2 * i] + 2][self.enemies[2 * i + 1]] == 'B'):
                        if disp[self.enemies[2 * i] + 2][self.enemies[2 * i + 1]] == 'B':
                            print "You are dead"
                            exit(0)
                        else:
                            disp[self.enemies[2 * i] + 2][
                                self.enemies[2 * i + 1]] = 'E'
                            disp[self.enemies[2 * i] + 2][
                                self.enemies[2 * i + 1] + 1] = 'E'
                            disp[self.enemies[2 * i] + 2][
                                self.enemies[2 * i + 1] + 2] = 'E'
                            disp[self.enemies[2 * i] + 2][
                                self.enemies[2 * i + 1] + 3] = 'E'
                            disp[self.enemies[2 * i] + 3][
                                self.enemies[2 * i + 1]] = 'E'
                            disp[self.enemies[2 * i] + 3][
                                self.enemies[2 * i + 1] + 1] = 'E'
                            disp[self.enemies[2 * i] + 3][
                                self.enemies[2 * i + 1] + 2] = 'E'
                            disp[self.enemies[2 * i] + 3][
                                self.enemies[2 * i + 1] + 3] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1]] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 1] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 2] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 3] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1]] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 1] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 2] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 3] = ' '
                            self.enemies[2 * i] = self.enemies[2 * i] + 2
                            flag = 1
                            break
                    else:
                        xvar = 2
                if xvar == 2:  # upwards movement
                    if self.enemies[2 * i] - 1 >= 1 and (disp[self.enemies[2 * i] - 1][self.enemies[2 * i + 1]] == ' ' or disp[self.enemies[2 * i] - 1][self.enemies[2 * i + 1]] == 'E' or disp[self.enemies[2 * i] - 1][self.enemies[2 * i + 1]] == 'B'):
                        if disp[self.enemies[2 * i] - 1][self.enemies[2 * i + 1]] == 'B':
                            print "You are Dead"
                            exit(0)
                        else:
                            disp[self.enemies[2 * i] - 1][
                                self.enemies[2 * i + 1]] = 'E'
                            disp[self.enemies[2 * i] - 1][
                                self.enemies[2 * i + 1] + 1] = 'E'
                            disp[self.enemies[2 * i] - 1][
                                self.enemies[2 * i + 1] + 2] = 'E'
                            disp[self.enemies[2 * i] - 1][
                                self.enemies[2 * i + 1] + 3] = 'E'
                            disp[self.enemies[2 * i] - 2][
                                self.enemies[2 * i + 1]] = 'E'
                            disp[self.enemies[2 * i] - 2][
                                self.enemies[2 * i + 1] + 1] = 'E'
                            disp[self.enemies[2 * i] - 2][
                                self.enemies[2 * i + 1] + 2] = 'E'
                            disp[self.enemies[2 * i] - 2][
                                self.enemies[2 * i + 1] + 3] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1]] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 1] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 2] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 3] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1]] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 1] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 2] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 3] = ' '
                            self.enemies[2 * i] = self.enemies[2 * i] - 2
                            flag = 1
                            break
                    else:
                        xvar = 3
                if xvar == 3:  # right side movement of enemy
                    if self.enemies[2 * i + 1] <= 80 and (disp[self.enemies[2 * i]][self.enemies[2 * i + 1] + 4] == ' ' or disp[self.enemies[2 * i]][self.enemies[2 * i + 1] + 4] == 'E' or disp[self.enemies[2 * i]][self.enemies[2 * i + 1] + 4] == 'B'):
                        if disp[self.enemies[2 * i]][self.enemies[2 * i + 1] + 4] == 'B':
                            print "You are dead"
                            exit(0)
                        else:
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 4] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 5] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 6] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 7] = 'E'
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 4] = 'E'
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 5] = 'E'
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 6] = 'E'
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 7] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1]] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 1] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 2] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 3] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1]] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 1] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 2] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 3] = ' '
                            self.enemies[2 * i + 1] = self.enemies[
                                2 * i + 1] + 4
                            flag = 1
                            break
                    else:
                        xvar = 4
                if xvar == 4:  # left movement of enemy
                    if self.enemies[2 * i + 1] >= 4 and (disp[self.enemies[2 * i]][self.enemies[2 * i + 1] - 1] == ' ' or disp[self.enemies[2 * i]][self.enemies[2 * i + 1] - 1] == 'E' or disp[self.enemies[2 * i]][self.enemies[2 * i + 1] - 1] == 'B'):
                        if disp[self.enemies[2 * i]][self.enemies[2 * i + 1] - 1] == 'B':
                            print "You are dead"
                            exit(0)
                        else:
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] - 1] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] - 2] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] - 3] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] - 4] = 'E'
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] - 1] = 'E'
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] - 2] = 'E'
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] - 3] = 'E'
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] - 4] = 'E'
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1]] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 1] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 2] = ' '
                            disp[self.enemies[2 * i]][
                                self.enemies[2 * i + 1] + 3] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1]] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 1] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 2] = ' '
                            disp[self.enemies[2 * i] + 1][
                                self.enemies[2 * i + 1] + 3] = ' '
                            self.enemies[2 * i + 1] = self.enemies[
                                2 * i + 1] - 4
                            flag = 1
                            break
                    else:
                        xvar = 1
            else:
                flag = 1
