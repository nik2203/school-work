import pyxel
from constants import *
from utilities import *
from tiles import *
from player import *
import time as t
from math import asin, acos, cos, sin, pi

# TO DO :



class Game:
    def __init__(self):
        pyxel.init(WINDOW_SIZE, WINDOW_SIZE, fps=30)
        pyxel.load("assets/game_data.pyxres")

        self.screen = "controls"
        self.count_down = 0
        self.score = 0
        self.retries = 0

        self.level_nb = 0

        self.all_coins = []
        self.max_coins = [1, 1, 2, 3, 2, 4, 3, 5]
        self.all_times = []
        self.all_retries = []
        for i in range(8):
            self.all_coins.append(0)
            self.all_times.append(0)
            self.all_retries.append(0)
        # Starting screen
        # Controls
        # Press enter to start level 1

        # Run game :
        pyxel.run(self.update, self.draw)


    def update(self):
        print(self.screen)
        if (self.screen=="finish_screen"):
            return None
        if pyxel.btnp(pyxel.KEY_P):
            self.level_nb += 1
            self.reload_level()
        if pyxel.btnp(pyxel.KEY_O):
            self.level_nb -= 1
            self.reload_level()
        if (self.screen=="game"):
            self.level.time -= 1/60
            if float_equal(self.level.time, 14.5):
                print(self.level.time)
                pyxel.sound(2).speed = 30
            elif float_equal(self.level.time, 6.5):
                print(self.level.time)
                pyxel.sound(2).speed = 20
            self.player.update(self.level, self)
            if (self.level.time <= 0):
                self.screen = "retry"
                self.all_retries[self.level_nb] +=1
                self.count_down = 60
                pyxel.stop(1)
                pyxel.play(1, 3)
            if (self.check_finish()):
                self.screen="to_next_level"
                self.all_coins[self.level_nb] += self.level.coins_collected
                self.all_times[self.level_nb] += 30 - self.level.time
                if (self.level_nb == 8):
                    self.screen = "finish_screen"
                    return None
                self.count_down = 60
                pyxel.stop(1)
            if (pyxel.btnp(pyxel.KEY_R)):
                self.screen = "retry"
                self.count_down = 60
                self.all_retries[self.level_nb] +=1
                pyxel.stop(1)
                pyxel.play(1, 3)
        elif (self.screen=="controls"):
            if pyxel.btnp(pyxel.KEY_ENTER):
                self.reload_level()
                self.screen = "game"
        if (self.screen==("to_next_level")):
            self.count_down -= 1
            if self.count_down==0:
                self.level_nb += 1
                self.score += self.level.coins_collected
                pyxel.sound(1).speed = max(pyxel.sound(1).speed - 1, 8)
                pyxel.sound(3).speed = max(pyxel.sound(1).speed - 1, 8)
                self.reload_level()
                if (self.level_nb == 8):
                    self.screen = "finish_screen"
                    return None
                else:
                    self.screen = "game"
        if (self.screen==("retry")):
            self.count_down -= 1
            if (self.count_down==0):
                self.reload_level()
                self.retries += 1
                self.screen = "game"

    def check_finish(self):
        for i in range(TN):
            for j in range(TN):
                tile = self.level.tiles[i][j]
                if tile.name=="finish":
                    if objects_overlapping(self.player, tile):
                        print("Level completed in", round(30 - self.level.time, 3), "seconds\n")
                        pyxel.stop(0)
                        pyxel.play(0, 1)
                        return True
        return False

    def reload_level(self):
        pyxel.sound(2).speed = 60
        pyxel.play(1, 2, loop=True)
        print(self.all_coins)
        print(self.all_retries)
        print(self.all_times)
        self.level = Level(self.level_nb)
        self.player = Player(*self.level.starting_coord)

    def draw(self):
        if self.screen=="game":
            self.draw_game()
        if self.screen=="finish_screen":
            pyxel.cls(0)
            pyxel.text(40, 40, "Congratulations, you have beaten the game !", 11)
            pyxel.text(50, 60, "Scores:", 10)
            pyxel.text(40, 80, "LEVEL    |    TIME    |    COINS    |    RETRIES", 10)
            for i in range(8):
                pyxel.text(40, 100 + 10*i, str(i+1) + "        |   " + str(round(self.all_times[i],3)) + "  |      " + str(self.all_coins[i]) + "/" + str(self.max_coins[i]) + "    |      " + str(self.all_retries[i]) , 8)
            score = 0
            for i in range(8):
                score += self.all_times[i] - 6 * self.all_coins[i] + 2 *self.all_retries[i]
            pyxel.text(40, 200, "Final score : " + str(round(score, 3)) + "   (lowest is best)", 11)

        if self.screen=="controls":
            pyxel.text(0, 0, "Clouds", 7)
            data = pyxel.image(4, system=True).data
            game_name = []
            for i in range(6):
                game_name.append([])
                for j in range(4*16):
                    game_name[i].append(data[i][j])
            pyxel.cls(0)
            pyxel.text(0, 0, "Controls:", 7)
            data = pyxel.image(4, system=True).data
            controls = []
            for i in range(6):
                controls.append([])
                for j in range(4*9):
                    controls[i].append(data[i][j])
            pyxel.cls(0)
            pyxel.text(0, 0, "Start with ENTER", 7)
            data = pyxel.image(4, system=True).data
            start = []
            for i in range(6):
                start.append([])
                for j in range(4*16):
                    start[i].append(data[i][j])
            pyxel.cls(0)
            pyxel.text(0, 0, "Move:", 7)
            data = pyxel.image(4, system=True).data
            move = []
            for i in range(6):
                move.append([])
                for j in range(4*5):
                    move[i].append(data[i][j])
            pyxel.cls(0)
            pyxel.blt(0, 0, 0, 120, 16, 75, 9, 0)
            data = pyxel.image(4, system=True).data
            jump = []
            for i in range(9):
                jump.append([])
                for j in range(85):
                    jump[i].append(data[i][j])
            pyxel.cls(0)
            pyxel.blt(0, 0, 0, 120, 32, 75, 9, 0)
            data = pyxel.image(4, system=True).data
            restart = []
            for i in range(9):
                restart.append([])
                for j in range(85):
                    restart[i].append(data[i][j])
            pyxel.cls(0)

            pyxel.cls(0)
            green = [24, 0]
            yellow = [40, 0]
            blue = [40, 16]
            pink = [32, 16]

            size = 4
            x = 10
            y = 15
            for i in range(0, 6):
                for j in range(0, 4*16):
                    if game_name[i][j]==7:
                        pyxel.blt(1 + x + j*size, 1 + y + i*size, 0, *yellow, size, size)
                        pyxel.blt(x + j*size, y + i*size, 0, *green, size, size)
            size = 3
            x = 20
            y = 70 -10
            for i in range(0, 6):
                for j in range(0, 4*9):
                    if controls[i][j]==7:
                        pyxel.blt(x + j*size, y + i*size, 0, *pink, size, size)
            size = 2
            x = 40
            y = 110 -10
            for i in range(0, 6):
                for j in range(0, 4*5):
                    if move[i][j]==7:
                        pyxel.blt(x + j*size, y + i*size, 0, *blue, size, size)
            pyxel.blt(x + 90, y - 3, 0, 56, 0, 20, 16, 0)
            pyxel.blt(x + 120, y - 3, 0, 56, 0, -20, 16, 0)
            size = 2
            x = 40
            y = 130 -10
            for i in range(0, 9):
                for j in range(0, 85):
                    if jump[i][j]==7:
                        pyxel.blt(x + j*size, y + i*size, 0, *blue, size, size)
            size = 2
            x = 40
            y = 155 -10
            for i in range(0, 9):
                for j in range(0, 85):
                    if restart[i][j]==7:
                        pyxel.blt(x + j*size, y + i*size, 0, *blue, size, size)
            pyxel.text(20, 190, "Scoring   :   1 coin <=> 3 restart <=> 6s on timer", 11)
            size = 2
            x = 60
            y = 218
            for i in range(0, 6):
                for j in range(0, 4*16):
                    if start[i][j]==7:
                        pyxel.blt(x + j*size, y + i*size, 0, *yellow, size, size)
            # pyxel.text(20, 20, "Press enter to start", 8)
        if self.screen=="to_next_level":
            self.draw_next()
        if self.screen=="retry":
            pyxel.cls(0)
            # pyxel.text(20, 20, "Time out", 8)
            pyxel.text(30, 40, "Try again", 8)
        # pyxel.text(30, 30, str(self.score), 8)

    def draw_game(self):
        pyxel.cls(0)
        self.draw_clock()

        for i in range(TN):
            for j in range(TN):
                self.level.tiles[i][j].draw()
        self.player.draw(self.level)

    def draw_next(self):
        full_color = 1
        border_color = 5

        str_to_print = str(round(30 - self.level.time, 3))
        to_print = []
        for i in range(len(str_to_print)):
            to_print.append(str_to_print[i])
        while to_print[2]!=".":
            to_print = ["0"] + to_print
        while len(to_print)<7:
            to_print.append("0")
        str_to_print = "".join(to_print)
        pyxel.text(0, 0, str_to_print, 7)
        data = pyxel.image(4, system=True).data
        score_text = []
        for i in range(6):
            score_text.append([])
            for j in range(24):
                score_text[i].append(data[i][j])


        pyxel.cls(0)
        theta_coord = [128 + 2**(0.5) * 128*sin(self.theta), 128 + 2**(0.5) * 128*cos(self.theta)]
        if self.theta > pi/2:
            # print(0)
            pyxel.tri(128, 128, 128, -1000, *theta_coord, full_color)
        elif self.theta > 0:
            # print(1)
            pyxel.rect(128, 0, 255, 128, full_color)
            pyxel.tri(128, 128, 1000, 128, *theta_coord, full_color)
        elif self.theta > -pi/2:
            # print(2)
            pyxel.rect(128, 0, 255, 255, full_color)
            pyxel.tri(128, 128, 128, 1000, *theta_coord, full_color)
        else:
            # print(6)
            pyxel.rect(128, 0, 255, 255, full_color)
            pyxel.rect(0, 128, 128, 255, full_color)
            pyxel.tri(128, 128, -1000, 128, *theta_coord, full_color)

        pyxel.line(128, 128, *theta_coord, border_color)
        pyxel.line(128, 0, 128, 128, border_color)

        for i in range(0, 6):
            # print(score_text[i])
            for j in range(0, 24):
                if score_text[i][j]==7:
                    pyxel.blt(10 + j*10, 100 + i*10, 0, 24, 0, 10, 10)
                    pyxel.blt(2 + 10 + j*10, 2 + 100 + i*10, 0, 32, 0, 10, 10)

    def draw_clock(self):
        self.theta = - pi + 2 * pi * self.level.time/30
        t, i = pi, 0
        while (t > self.theta ):
            pyxel.line(128, 128, 128 + 2**(0.5) * 128*sin(t), 128 + 2**(0.5) * 128*cos(t), 8 + (i)%8)
            t -= 2*pi / 120
            i += 1
        pyxel.rectb(0, 0, 255, 255, 0)
        pyxel.rectb(1, 1, 253, 253, 6)
        pyxel.rectb(7, 7, 255-13, 255-13, 6)


if (__name__ == '__main__'):
    Game()
