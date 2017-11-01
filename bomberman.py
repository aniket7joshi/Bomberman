from board import Board


class Bomberman(Board):

    """Bomberman coordinates"""

    def __init__(self):
        """Bomberman at the start coordinates"""
        self.left_x = 0
        self.left_y = 0

    def start(self, disp):  # bomberma position at the start
        """Printing Bomberman at start"""
        disp[0][0] = 'B'
        disp[0][1] = 'B'
        disp[1][1] = 'B'
        disp[1][0] = 'B'
        disp[0][2] = 'B'
        disp[0][3] = 'B'
        disp[1][2] = 'B'
        disp[1][3] = 'B'

    def posl(self):  # posl returns the row in which the topleft B of bomberman is present
        """Bomberman top left x coordinate"""
        return self.left_x

    def posr(self):  # posr sreturns the column in which the topleft B of bomberman is present
        """Bomberman top left y coordinate"""
        return self.left_y
