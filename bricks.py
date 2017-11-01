from __future__ import print_function
import random


class Bricks():

    """initalisation"""

    def __init__(self):
        """all_bricks contain the 2 pointer for every brick generated"""
        self.all_bricks = []

    def generate_bricks(self, disp):
        """generation of random bricks"""
        i = 0
        while i < 30:
            """to change the number of bricks just change the number inside the loop"""
            flag = -1
            while flag != 1:
                xcor = random.randint(0, 14)
                xcor = xcor * 2
                ycor = random.randint(2, 18)
                ycor = ycor * 4
                if disp[xcor][ycor] == ' ':
                    disp[xcor][ycor] = '%'
                    disp[xcor][ycor + 1] = '%'
                    disp[xcor][ycor + 2] = '%'
                    disp[xcor][ycor + 3] = '%'
                    disp[xcor + 1][ycor] = '%'
                    disp[xcor + 1][ycor + 1] = '%'
                    disp[xcor + 1][ycor + 2] = '%'
                    disp[xcor + 1][ycor + 3] = '%'
                    flag = 1
            i = i + 1
            self.all_bricks.append(xcor)
            self.all_bricks.append(ycor)
