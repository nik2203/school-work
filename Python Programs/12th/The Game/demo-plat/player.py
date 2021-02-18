import pyxel
from constants import *
from utilities import *
from tiles import *


class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.w, self.h = 6, 8
        self.vx, self.vy = 0, 0
        self.offset_x, self.offset_y = 2, 2
        self.hitbox = [0, 0, self.w, self.h]

        self.status = "idle"
        self.on_ground = False
        self.facing = 1
        self.coyote_time = 0
        self.previous_coyote_time = 0

        make_sensors(self, self.offset_x, self.offset_y)
        # sensors[4] = checks underneath for collision, sensors[5] = checks underneath and on the sides for coyote time
        self.sensors += [Sensor(self.x + 2, self.y + self.h/2 - 1, self.w -2, self.h/2 + 1), Sensor(self.x - 1, self.y + self.h/2 - 1, self.w + 2, self.h/2 + 1)]
        # sensors[6:7] check for side tiles for grabs [left, right]
        self.sensors += [Sensor(self.x - 1, self.y + self.h/2 - 1, self.w/2 + 1, 2), Sensor(self.x + self.w/2, self.y + self.h/2 - 1, self.w/2, 2)]

    def update(self, level, game):
        slide = False
        self.move(level, game)
        for i in range(TN):
            for j in range(TN):
                tile = level.tiles[i][j]
                if (self.on_ground==False and objects_overlapping(self.sensors[6], tile) and tile.solid):
                    self.status = "left_slide"
                    # print("left_slide")
                    slide = True
                if (self.on_ground==False and objects_overlapping(self.sensors[7], tile) and tile.solid):
                    self.status = "right_slide"
                    # print("right_slide")
                    slide = True
        if slide:
            pass
        elif (self.on_ground == False):
            self.status = "jumping"
        elif (abs(self.vx) + abs(self.vy) > 0.2):
            self.status = "running"
        else:
            self.status = "idle"

    def move(self, level, game):
        if (pyxel.btn(pyxel.KEY_LEFT)):
            if (self.on_ground or self.vy < 0.1):
                self.vx = max(self.vx - 0.4, -1)
            elif (self.status in ["left_slide", "right_slide"]):
                self.vx = max(self.vx - 0.07, -1)
            else:
                self.vx = max(self.vx - 0.4, -0.8/abs(self.vy))
            self.facing = -1
        if (pyxel.btn(pyxel.KEY_RIGHT)):
            if (self.on_ground or self.vy < 0.01):
                self.vx = min(self.vx + 0.4, 1)
            elif (self.status in ["left_slide", "right_slide"]):
                self.vx = max(self.vx + 0.07, 1)
            else:
                self.vx = min(self.vx + 0.4, 1.2/abs(self.vy))
            self.facing = 1
        if (pyxel.btnp(pyxel.KEY_SPACE) and self.on_ground):
            pyxel.play(3, 6)
            self.vy -= 4
            self.on_ground = False
        if (pyxel.btnp(pyxel.KEY_SPACE) and self.status in ["left_slide", "right_slide"]):
            pyxel.play(3, 6)
            self.vy -= 5
            if self.status=="right_slide":
                self.vx -= 5
            if self.status=="left_slide":
                self.vx += 5
            self.on_ground = False

        self.coyote_time = max(0, self.coyote_time - 1)
        if (self.previous_coyote_time == 0 and self.coyote_time == 0):
            self.on_ground = False

        fraction = 7
        for i in range(fraction):
            self.x += self.vx/fraction
            self.y += self.vy/fraction
            self.collide(level, game)
            if self.coyote_time <= 0:
                self.on_ground = False
            if (self.on_ground == False):
                if (self.status in ["left_slide", "right_slide"]):
                    self.vy = min(self.vy + 0.1/fraction, 0.5)
                    self.vy = max(self.vy, -2)
                else:
                    self.vy = min(self.vy + 0.2/fraction, 4.5)

        self.vx *= 0.7

        self.vy *= 0.9

        self.previous_coyote_time = self.coyote_time




    def collide(self, level, game):
        for i in range(TN):
            for j in range(TN):
                tile = level.tiles[i][j]
                if tile.solid and square_distance(self, tile)< 16**2:
                    # Standard collision
                    tile_collision(self, tile)
                    # Checking for coyote time
                    if objects_overlapping(self.sensors[4], tile):
                        self.on_ground = True
                        self.coyote_time = 5
                    elif (objects_overlapping(self.sensors[5], tile) and self.coyote_time==5):
                        self.coyote_time = 5
                    if (self.on_ground==False and objects_overlapping(self.sensors[6], tile)):
                        self.status = "left_slide"
                        # print("left_slide")
                    if (self.on_ground==False and objects_overlapping(self.sensors[7], tile)):
                        self.status = "right_slide"
                        # print("right_slide")
                # Coin collection
                if tile.name=="coin" and objects_overlapping(self, tile):
                    level.coins_collected += 1
                    level.tiles[i][j] = Sky_tile(tile.x, tile.y)
                    pyxel.play(0, 0)
                if tile.name=="lava" and objects_overlapping(self, tile):
                    level.time = 0

    def draw(self, level):
        if (self.status=="idle"):
            pyxel.blt(self.x, self.y, 2, 1+ TL * ((pyxel.frame_count //15)%4), 0, self.facing * self.w, self.h, 0)
        if (self.status=="running"):
            pyxel.blt(self.x, self.y, 2, 1 + TL * ((pyxel.frame_count //5)%8), 8, self.facing * self.w, self.h, 0)
        if (self.status=="jumping"):
            pyxel.blt(self.x, self.y, 2, 1 + TL * ((pyxel.frame_count //8)%4), 16, self.facing * self.w, self.h, 0)
        if (self.status=="left_slide"):
            pyxel.blt(round(self.x), self.y, 2, TL * ((pyxel.frame_count //8)%4), 24, -1 * self.w, self.h, 0)
        if (self.status=="right_slide"):
            pyxel.blt(self.x, self.y, 2, TL * ((pyxel.frame_count //8)%4), 24, self.w, self.h, 0)

        if DEBUGGING:
            for i in [6, 7]:
                self.sensors[i].draw()
            pyxel.text(self.x + 10, self.y - 5, self.status, 8)
            pyxel.text(self.x + 10, self.y +3, str(self.on_ground), 8)
