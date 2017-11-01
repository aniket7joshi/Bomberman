from bomberman import Bomberman
from enemy import Enemy
from bricks import Bricks


class Bomb():

    def __init__(self):
        self.left_x = ' '
        self.left_y = ' '

    def plant(self, B, disp):
        """# bomb being planted and the array now prints 3,2,1 while the bomb explodes"""
        self.left_x = B.posl()
        self.left_y = B.posr()
        disp[self.left_x][self.left_y] = '3'
        disp[self.left_x][self.left_y + 1] = '3'
        disp[self.left_x][self.left_y + 2] = '3'
        disp[self.left_x][self.left_y + 3] = '3'
        disp[self.left_x + 1][self.left_y] = '3'
        disp[self.left_x + 1][self.left_y + 1] = '3'
        disp[self.left_x + 1][self.left_y + 2] = '3'
        disp[self.left_x + 1][self.left_y + 3] = '3'

    def explode(self, b, e, s, disp, die):
        """explosion of the bomb"""
        flag = 0
        flag1 = 0
        len = e.enemies.__len__()
        lenbricks = s.all_bricks.__len__()
        """if bomberman dont move from bomb position #what will happen to men if bomb explode"""
        if die == 1:
            flag = 1
        if self.left_y >= 3:
            if disp[self.left_x][self.left_y - 2] == 'B' or disp[self.left_x][self.left_y] == 'B':
                flag = 1
        if self.left_x >= 2:
            if disp[self.left_x - 1][self.left_y] == 'B' or disp[self.left_x][self.left_y] == 'B':
                flag = 1
        if self.left_x <= 26:
            if disp[self.left_x + 2][self.left_y] == 'B' or disp[self.left_x][self.left_y] == 'B':
                flag = 1
        if self.left_y <= 76:
            if disp[self.left_x][self.left_y + 5] == 'B' or disp[self.left_x][self.left_y] == 'B':
                flag = 1
        if self.left_y >= 3:
            if disp[self.left_x][self.left_y - 2] == 'E' or disp[self.left_x][self.left_y] == 'E':
                """# if flag happens to be 1 then the bomberman is dead"""
                i = 0
                while i < len / 2:  # now the killing of enemies if it comes in the area of bomb
                    if e.enemies[2 * i] == self.left_x and e.enemies[2 * i + 1] == self.left_y - 4:
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1]] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 1] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 2] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 3] = ' '
                        disp[e.enemies[2 * i] + 1][e.enemies[2 * i + 1]] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 1] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 2] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 3] = ' '
                        e.enemies[2 * i] = -1
                        e.enemies[2 * i + 1] = -1
                        break
                    i = i + 1
                flag1 = 1
        if self.left_y >= 3 and (disp[self.left_x][self.left_y - 2] == '%'):  # removal of brick
            i = 0
            while i < lenbricks / 2:
                if s.all_bricks[2 * i] == self.left_x:
                    if s.all_bricks[2 * i + 1] == self.left_y - 4:
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1]] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 1] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 2] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 3] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1]] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 1] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 2] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 3] = ' '
                        s.all_bricks[2 * i] = -1
                        s.all_bricks[2 * i + 1] = -1
                        break
                i = i + 1
            flag1 = 1
        if self.left_x >= 2:
            if disp[self.left_x - 1][self.left_y] == 'E' or disp[self.left_x][self.left_y] == 'E':
                i = 0
                while i < len / 2:
                    if e.enemies[2 * i] == self.left_x - 2 and e.enemies[2 * i + 1] == self.left_y:
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1]] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 1] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 2] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 3] = ' '
                        disp[e.enemies[2 * i] + 1][e.enemies[2 * i + 1]] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 1] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 2] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 3] = ' '
                        e.enemies[2 * i] = -1
                        e.enemies[2 * i + 1] = -1
                        break
                    i = i + 1
                flag1 = 1
        if self.left_x >= 2 and (disp[self.left_x - 1][self.left_y] == '%'):  # removal of bricks
            i = 0
            while i < lenbricks / 2:
                if s.all_bricks[2 * i] == self.left_x - 2:
                    if s.all_bricks[2 * i + 1] == self.left_y:
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1]] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 1] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 2] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 3] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1]] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 1] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 2] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 3] = ' '
                        s.all_bricks[2 * i] = -1
                        s.all_bricks[2 * i + 1] = -1
                        break
                i = i + 1
            flag1 = 1
        if self.left_x <= 26:
            if disp[self.left_x + 2][self.left_y] == 'E' or disp[self.left_x][self.left_y] == 'E':
                i = 0
                while i < len / 2:
                    if e.enemies[2 * i] == self.left_x + 2 and e.enemies[2 * i + 1] == self.left_y:
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1]] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 1] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 2] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 3] = ' '
                        disp[e.enemies[2 * i] + 1][e.enemies[2 * i + 1]] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 1] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 2] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 3] = ' '
                        e.enemies[2 * i] = -1
                        e.enemies[2 * i + 1] = -1
                        break
                    i = i + 1
                flag1 = 1
        if self.left_x <= 26 and (disp[self.left_x + 2][self.left_y] == '%'):  # removal of bricks
            i = 0
            while i < lenbricks / 2:
                if s.all_bricks[2 * i] == self.left_x + 2:
                    if s.all_bricks[2 * i + 1] == self.left_y:
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1]] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 1] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 2] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 3] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1]] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 1] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 2] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 3] = ' '
                        s.all_bricks[2 * i] = -1
                        s.all_bricks[2 * i + 1] = -1
                        break
                i = i + 1
            flag1 = 1
        if self.left_y <= 76:
            if disp[self.left_x][self.left_y + 5] == 'E' or disp[self.left_x][self.left_y] == 'E':
                i = 0
                while i < len / 2:
                    if e.enemies[2 * i] == self.left_x and e.enemies[2 * i + 1] == self.left_y + 4:
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1]] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 1] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 2] = ' '
                        disp[e.enemies[2 * i]][e.enemies[2 * i + 1] + 3] = ' '
                        disp[e.enemies[2 * i] + 1][e.enemies[2 * i + 1]] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 1] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 2] = ' '
                        disp[e.enemies[2 * i] + 1][
                            e.enemies[2 * i + 1] + 3] = ' '
                        e.enemies[2 * i] = -1
                        e.enemies[2 * i + 1] = -1
                        break
                    i = i + 1
                flag1 = 1
        if self.left_y <= 76 and (disp[self.left_x][self.left_y + 5] == '%'):  # removal of bricks
            i = 0
            while i < lenbricks / 2:
                if s.all_bricks[2 * i] == self.left_x:
                    if s.all_bricks[2 * i + 1] == self.left_y + 4:
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1]] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 1] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 2] = ' '
                        disp[s.all_bricks[2 * i]][
                            s.all_bricks[2 * i + 1] + 3] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1]] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 1] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 2] = ' '
                        disp[s.all_bricks[2 * i] + 1][
                            s.all_bricks[2 * i + 1] + 3] = ' '
                        s.all_bricks[2 * i] = -1
                        s.all_bricks[2 * i + 1] = -1
                        break
                i = i + 1
            flag1 = 1
        if flag == 1:
            print "YOU ARE DEAD"
            exit(1)

    def clear(self, disp):  # clearance after the bomb explodes
        disp[self.left_x][self.left_y] = ' '
        disp[self.left_x][self.left_y + 1] = ' '
        disp[self.left_x][self.left_y + 2] = ' '
        disp[self.left_x][self.left_y + 3] = ' '
        disp[self.left_x + 1][self.left_y] = ' '
        disp[self.left_x + 1][self.left_y + 1] = ' '
        disp[self.left_x + 1][self.left_y + 2] = ' '
        disp[self.left_x + 1][self.left_y + 3] = ' '
