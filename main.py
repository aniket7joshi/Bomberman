from __future__ import print_function
import signal
import time
import os
from bomberman import Bomberman
from board import Board
from alarmexception import AlarmException
from getchunix import GetchUnix
from enemy import Enemy
from bomb import Bomb
from bricks import Bricks

disp = [['X' for x in range(90)]
        for y in range(40)]  # The main board which is printed
getch = GetchUnix()


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):  # Input function
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        os.system('clear')
        b.output(disp)
        print("Your Score is %d" % score)
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


player = Bomberman()  # different objects being created
b = Board()
b.display(disp)
e = Enemy()
u = Bomb()
s = Bricks()
e.generate_enemies(disp, 10)  # enemies being generated
for i in range(10):  # if you want more enemies just change the number 10 in this and above line
    e.change(i, disp)
s.generate_bricks(disp)  # brikcs being generated
player.start(disp)
b.output(disp)
planted = 0  # different variables for various purposes
count = 0
flag = 0
die = 0
won = 1
score = 0
enemieskilled = 0
t = 1
done = [0 for i in range(100)]
                         # array for whether we have checked enemy number i
dons = [0 for i in range(100)]
                         # array for whether we have checked brick number i
while 1:  # the main loop begins
    length = e.enemies.__len__()
    lenbricks = s.all_bricks.__len__()
    if t == 1:
        now = time.time()
        t = 0
    if time.time() > now + 0.1:  # loop for movement of enemy
        i = 0
        while i < length / 2:
            e.move(i, disp, player)
            i = i + 1
        t = 1
    won = 1
    score = 0
    bricksdestroyed = 0
    for i in range(length):  # for calcuating scores
        if e.enemies[i] != -1:
            won = 0
        else:
            if done[i] == 0:
                enemieskilled = enemieskilled + 1
                done[i] = 1
        if i == length - 1:
            score = (enemieskilled / 2) * 100
    for i in range(lenbricks):
        if s.all_bricks[i] == -1:
            bricksdestroyed = bricksdestroyed + 1
    score = score + (bricksdestroyed / 2) * 20
    if won == 1:  # if all the enemies are killed then you won the game
        print("You Won")
        exit(0)
    c = input_to()  # input of the character
    if c == 's':  # down movement
        if player.left_x <= 28 and player.left_y <= 80:
            if planted == 0 or (flag == 0 and planted == 1):
                if disp[player.left_x + 2][player.left_y] != 'X':
                    if disp[player.left_x + 2][player.left_y] != '%':
                        disp[player.left_x + 2][player.left_y + 1] = 'B'
                        disp[player.left_x + 2][player.left_y + 2] = 'B'
                        disp[player.left_x + 2][player.left_y + 3] = 'B'
                        disp[player.left_x + 2][player.left_y] = 'B'
                        disp[player.left_x + 3][player.left_y] = 'B'
                        disp[player.left_x + 3][player.left_y + 1] = 'B'
                        disp[player.left_x + 3][player.left_y + 2] = 'B'
                        disp[player.left_x + 3][player.left_y + 3] = 'B'
                        disp[player.left_x][player.left_y] = ' '
                        disp[player.left_x][player.left_y + 1] = ' '
                        disp[player.left_x][player.left_y + 2] = ' '
                        disp[player.left_x][player.left_y + 3] = ' '
                        disp[player.left_x + 1][player.left_y] = ' '
                        disp[player.left_x + 1][player.left_y + 1] = ' '
                        disp[player.left_x + 1][player.left_y + 2] = ' '
                        disp[player.left_x + 1][player.left_y + 3] = ' '
                        player.left_x = player.left_x + 2
        os.system('clear')
        b.output(disp)
        print("Your Score is %d" % score)
        if player.left_x <= 28 and player.left_y <= 80 and planted == 1 and flag == 1:
            if disp[player.left_x + 2][player.left_y] != 'X':
                if disp[player.left_x + 2][player.left_y] != '%':
                    disp[player.left_x + 2][player.left_y + 1] = 'B'
                    disp[player.left_x + 2][player.left_y + 2] = 'B'
                    disp[player.left_x + 2][player.left_y + 3] = 'B'
                    disp[player.left_x + 2][player.left_y] = 'B'
                    disp[player.left_x + 3][player.left_y] = 'B'
                    disp[player.left_x + 3][player.left_y + 1] = 'B'
                    disp[player.left_x + 3][player.left_y + 2] = 'B'
                    disp[player.left_x + 3][player.left_y + 3] = 'B'
                    disp[player.left_x][player.left_y] = '3'
                    disp[player.left_x][player.left_y + 1] = '3'
                    disp[player.left_x][player.left_y + 2] = '3'
                    disp[player.left_x][player.left_y + 3] = '3'
                    disp[player.left_x + 1][player.left_y] = '3'
                    disp[player.left_x + 1][player.left_y + 1] = '3'
                    disp[player.left_x + 1][player.left_y + 2] = '3'
                    disp[player.left_x + 1][player.left_y + 3] = '3'
                    player.left_x = player.left_x + 2
                    die = 0
                    flag = 0
        os.system('clear')
        b.output(disp)
        print("Your Score is %d" % score)

    if c == 'w':  # up movement
        if player.left_x >= 2 and player.left_y <= 80:
            if planted == 0 or (flag == 0 and planted == 1):
                if disp[player.left_x - 2][player.left_y] != 'X':
                    if disp[player.left_x - 2][player.left_y] != '%':
                        disp[player.left_x - 2][player.left_y + 1] = 'B'
                        disp[player.left_x - 2][player.left_y + 2] = 'B'
                        disp[player.left_x - 2][player.left_y + 3] = 'B'
                        disp[player.left_x - 2][player.left_y] = 'B'
                        disp[player.left_x - 1][player.left_y] = 'B'
                        disp[player.left_x - 1][player.left_y + 1] = 'B'
                        disp[player.left_x - 1][player.left_y + 2] = 'B'
                        disp[player.left_x - 1][player.left_y + 3] = 'B'
                        disp[player.left_x][player.left_y] = ' '
                        disp[player.left_x][player.left_y + 1] = ' '
                        disp[player.left_x][player.left_y + 2] = ' '
                        disp[player.left_x][player.left_y + 3] = ' '
                        disp[player.left_x + 1][player.left_y] = ' '
                        disp[player.left_x + 1][player.left_y + 1] = ' '
                        disp[player.left_x + 1][player.left_y + 2] = ' '
                        disp[player.left_x + 1][player.left_y + 3] = ' '
                        player.left_x = player.left_x - 2
        os.system('clear')
        b.output(disp)
        print("Your Score is %d" % score)
        if player.left_x >= 2 and player.left_y <= 80 and planted == 1 and flag == 1:
            if disp[player.left_x - 2][player.left_y] != 'X':
                if disp[player.left_x - 2][player.left_y] != '%':
                    disp[player.left_x - 2][player.left_y + 1] = 'B'
                    disp[player.left_x - 2][player.left_y + 2] = 'B'
                    disp[player.left_x - 2][player.left_y + 3] = 'B'
                    disp[player.left_x - 2][player.left_y] = 'B'
                    disp[player.left_x - 1][player.left_y] = 'B'
                    disp[player.left_x - 1][player.left_y + 1] = 'B'
                    disp[player.left_x - 1][player.left_y + 2] = 'B'
                    disp[player.left_x - 1][player.left_y + 3] = 'B'
                    disp[player.left_x][player.left_y] = '3'
                    disp[player.left_x][player.left_y + 1] = '3'
                    disp[player.left_x][player.left_y + 2] = '3'
                    disp[player.left_x][player.left_y + 3] = '3'
                    disp[player.left_x + 1][player.left_y] = '3'
                    disp[player.left_x + 1][player.left_y + 1] = '3'
                    disp[player.left_x + 1][player.left_y + 2] = '3'
                    disp[player.left_x + 1][player.left_y + 3] = '3'
                    player.left_x = player.left_x - 2
                    flag = 0
                    die = 0
        os.system('clear')
        b.output(disp)
        print("Your Score is %d" % score)
    if c == 'd':  # right movement
        if player.left_x <= 28 and player.left_y <= 80:
            if planted == 0 or (flag == 0 and planted == 1):
                if disp[player.left_x][player.left_y + 4] != 'X':
                    if disp[player.left_x][player.left_y + 4] != '%':
                        disp[player.left_x][player.left_y + 7] = 'B'
                        disp[player.left_x][player.left_y + 6] = 'B'
                        disp[player.left_x][player.left_y + 5] = 'B'
                        disp[player.left_x][player.left_y + 4] = 'B'
                        disp[player.left_x + 1][player.left_y + 4] = 'B'
                        disp[player.left_x + 1][player.left_y + 5] = 'B'
                        disp[player.left_x + 1][player.left_y + 6] = 'B'
                        disp[player.left_x + 1][player.left_y + 7] = 'B'
                        disp[player.left_x][player.left_y] = ' '
                        disp[player.left_x][player.left_y + 1] = ' '
                        disp[player.left_x][player.left_y + 2] = ' '
                        disp[player.left_x][player.left_y + 3] = ' '
                        disp[player.left_x + 1][player.left_y] = ' '
                        disp[player.left_x + 1][player.left_y + 1] = ' '
                        disp[player.left_x + 1][player.left_y + 2] = ' '
                        disp[player.left_x + 1][player.left_y + 3] = ' '
                        player.left_y = player.left_y + 4
        os.system('clear')
        b.output(disp)
        print("Your Score is %d" % score)
        if player.left_x <= 28 and player.left_y <= 80 and planted == 1 and flag == 1:
            if disp[player.left_x][player.left_y + 4] != 'X':
                if disp[player.left_x][player.left_y + 4] != '%':
                    disp[player.left_x][player.left_y + 7] = 'B'
                    disp[player.left_x][player.left_y + 6] = 'B'
                    disp[player.left_x][player.left_y + 5] = 'B'
                    disp[player.left_x][player.left_y + 4] = 'B'
                    disp[player.left_x + 1][player.left_y + 4] = 'B'
                    disp[player.left_x + 1][player.left_y + 5] = 'B'
                    disp[player.left_x + 1][player.left_y + 6] = 'B'
                    disp[player.left_x + 1][player.left_y + 7] = 'B'
                    disp[player.left_x][player.left_y] = '3'
                    disp[player.left_x][player.left_y + 1] = '3'
                    disp[player.left_x][player.left_y + 2] = '3'
                    disp[player.left_x][player.left_y + 3] = '3'
                    disp[player.left_x + 1][player.left_y] = '3'
                    disp[player.left_x + 1][player.left_y + 1] = '3'
                    disp[player.left_x + 1][player.left_y + 2] = '3'
                    disp[player.left_x + 1][player.left_y + 3] = '3'
                    player.left_y = player.left_y + 4
                    flag = 0
                    die = 0
        os.system('clear')
        b.output(disp)
        print("Your Score is %d" % score)
    if c == 'a':  # left movement
        if player.left_x <= 28 and player.left_y >= 4:
            if planted == 0 or (flag == 0 and planted == 1):
                if disp[player.left_x][player.left_y - 1] != 'X':
                    if disp[player.left_x][player.left_y - 1] != '%':
                        disp[player.left_x][player.left_y - 2] = 'B'
                        disp[player.left_x][player.left_y - 3] = 'B'
                        disp[player.left_x][player.left_y - 4] = 'B'
                        disp[player.left_x][player.left_y - 1] = 'B'
                        disp[player.left_x + 1][player.left_y - 1] = 'B'
                        disp[player.left_x + 1][player.left_y - 2] = 'B'
                        disp[player.left_x + 1][player.left_y - 3] = 'B'
                        disp[player.left_x + 1][player.left_y - 4] = 'B'
                        disp[player.left_x][player.left_y] = ' '
                        disp[player.left_x][player.left_y + 1] = ' '
                        disp[player.left_x][player.left_y + 2] = ' '
                        disp[player.left_x][player.left_y + 3] = ' '
                        disp[player.left_x + 1][player.left_y] = ' '
                        disp[player.left_x + 1][player.left_y + 1] = ' '
                        disp[player.left_x + 1][player.left_y + 2] = ' '
                        disp[player.left_x + 1][player.left_y + 3] = ' '
                        player.left_y = player.left_y - 4
        os.system('clear')
        b.output(disp)
        print("Your Score is %d" % score)
        if player.left_x <= 28 and player.left_y >= 4 and planted == 1 and flag == 1:
            if disp[player.left_x][player.left_y - 1] != 'X':
                if disp[player.left_x][player.left_y - 1] != '%':
                    disp[player.left_x][player.left_y - 2] = 'B'
                    disp[player.left_x][player.left_y - 3] = 'B'
                    disp[player.left_x][player.left_y - 4] = 'B'
                    disp[player.left_x][player.left_y - 1] = 'B'
                    disp[player.left_x + 1][player.left_y - 1] = 'B'
                    disp[player.left_x + 1][player.left_y - 2] = 'B'
                    disp[player.left_x + 1][player.left_y - 3] = 'B'
                    disp[player.left_x + 1][player.left_y - 4] = 'B'
                    disp[player.left_x][player.left_y] = '3'
                    disp[player.left_x][player.left_y + 1] = '3'
                    disp[player.left_x][player.left_y + 2] = '3'
                    disp[player.left_x][player.left_y + 3] = '3'
                    disp[player.left_x + 1][player.left_y] = '3'
                    disp[player.left_x + 1][player.left_y + 1] = '3'
                    disp[player.left_x + 1][player.left_y + 2] = '3'
                    disp[player.left_x + 1][player.left_y + 3] = '3'
                    player.left_y = player.left_y - 4
                    flag = 0
                    die = 0
        os.system('clear')
        b.output(disp)
        print("Your Score is %d" % score)
    if c == 'b':  # for putting bomb
        u.plant(player, disp)
        planted = 1
        flag = 1
        die = 1
        x = player.left_x
        y = player.left_y
        cur = time.time()
        p = 2
    if planted == 1:  # for printing time left in bomb crack
        if time.time() > cur + 0.2:
            count = count + 1
            disp[x][y] = p
            disp[x][y + 1] = p
            disp[x][y + 2] = p
            disp[x][y + 3] = p
            disp[x + 1][y] = p
            disp[x + 1][y + 1] = p
            disp[x + 1][y + 2] = p
            disp[x + 1][y + 3] = p
            p = p - 1
            cur = time.time()
        if count == 3:
            u.explode(player, e, s, disp, die)
            u.clear(disp)
            planted = 0
            count = 0
    if c == 'q':  # to stop the game
        exit(1)
    time.sleep(0.3)

        # print("lauda")  # print("bahar")
