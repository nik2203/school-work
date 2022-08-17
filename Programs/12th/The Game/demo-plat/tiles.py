import pyxel
from constants import *
from utilities import *
from random import randint

class Tile:
    def __init__(self, x, y, u, v, name):
        self.sprite_coord = [u, v, TL, TL]
        self.coord = [x, y]
        self.x, self.y = x, y
        self.w, self.h = TL, TL
        self.hitbox = [0, 0, self.w, self.h]
        self.name = name
        self.solid = 0 # By default tiles won't collide with the character
    def draw(self):
        pyxel.blt(*self.coord, 0, *self.sprite_coord, COL_KEY)


 ######  ########  ########  ######  ####    ###    ##
##    ## ##     ## ##       ##    ##  ##    ## ##   ##
##       ##     ## ##       ##        ##   ##   ##  ##
 ######  ########  ######   ##        ##  ##     ## ##
      ## ##        ##       ##        ##  ######### ##
##    ## ##        ##       ##    ##  ##  ##     ## ##
 ######  ##        ########  ######  #### ##     ## ########

class Start_tile(Tile):
     def __init__(self, x, y):
         super().__init__(x, y, 16, 0, "start")
         self.solid = 0 # Grass tile does collide with the character
         def draw(self):
             super().draw()

class Finish_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 8, 0, "finish")
        self.solid = 0 # Grass tile does collide with the character
    def draw(self):
        super().draw()

class Empty_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0, "empty")
    def draw(self):
        super().draw()

class Invisible_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, TL * min(3, randint(0, 64)), 56, "invisible")
        self.solid = 1
    def draw(self):
        super().draw()

class Clock_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0, "clock")
        self.solid = 1 # Grass tile does collide with the character
    def draw(self):
        super().draw()

class Coin_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0, "coin")
        self.solid = 0 # Coin tile does collide with the character
    def draw(self):
        pyxel.blt(*self.coord, 0, TL * ((pyxel.frame_count //10)%2), 72, TL, TL, COL_KEY)

class Lava_tile(Tile):
    def __init__(self, x, y):
        self.sprite_coord = [0, 80, TL, TL]
        self.coord = [x, y]
        self.x, self.y = x, y
        self.w, self.h = TL, 5
        self.hitbox = [0, 5, self.w, self.h]
        self.name = "lava"
        self.solid = 0 # By default tiles won't collide with the character
        self.previous_sprite = TL * randint(5,8)
    def draw(self):
        current_sprite = self.previous_sprite
        if (self.previous_sprite <= 3):
            if (randint(0, 5)==0):
                current_sprite = TL * min(randint(0,150), randint(5,8))
        else:
            if (randint(0, 40)==0):
                current_sprite = TL * min(randint(0,150), randint(5,8))
        pyxel.blt(*self.coord, 0, current_sprite, 80, TL, TL, 0)
        self.previous_sprite = current_sprite

######## ######## ########  ########     ###    #### ##    ##
   ##    ##       ##     ## ##     ##   ## ##    ##  ###   ##
   ##    ##       ##     ## ##     ##  ##   ##   ##  ####  ##
   ##    ######   ########  ########  ##     ##  ##  ## ## ##
   ##    ##       ##   ##   ##   ##   #########  ##  ##  ####
   ##    ##       ##    ##  ##    ##  ##     ##  ##  ##   ###
   ##    ######## ##     ## ##     ## ##     ## #### ##    ##


class Grass_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, TL * randint(0, 3), 24, "grass")
        self.solid = 1 # Grass tile does collide with the character
    def draw(self):
        super().draw()

class Brick_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, TL * randint(0, 3), 64, "brick")
        self.solid = 1 # Grass tile does collide with the character
    def draw(self):
        super().draw()

class Black_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 8, "black")
        self.solid = 1 # Grass tile does collide with the character
    def draw(self):
        super().draw()

class Dirt_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, TL * randint(0, 3), 32, "dirt")
        self.solid = 1 # Dirt tile does collide with the character
    def draw(self):
        super().draw()

class Dirt_rock_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, TL * randint(0, 3), 40, "dirt_rock")
        self.solid = 1 # Dirt tile does collide with the character
    def draw(self):
        super().draw()

class Rock_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, TL * randint(0, 3), 48, "rock")
        self.solid = 1 # Rock tile does collide with the character
    def draw(self):
        super().draw()

class Sky_tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, TL * min(3, randint(0, 64)), 56, "sky")
        self.solid = 0
    def draw(self):
        super().draw()


##       ######## ##     ## ######## ##
##       ##       ##     ## ##       ##
##       ##       ##     ## ##       ##
##       ######   ##     ## ######   ##
##       ##        ##   ##  ##       ##
##       ##         ## ##   ##       ##
######## ########    ###    ######## ########


class Level:
    def __init__(self, level_nb):
        self.tiles = make_object_array(32, 32)
        self.nb = level_nb
        tile_map = get_level_map(level_nb)
        self.time = 30
        self.coins_collected = 0

        for i in range(TN):
            for j in range(TN):
                x, y = i*TL, j*TL
                if (tile_map[i][j] == 0):
                    self.tiles[i][j] = Black_tile(x, y)
                elif (tile_map[i][j] == 1):
                    self.tiles[i][j] = Sky_tile(x, y)
                elif (tile_map[i][j] == 2):
                    self.tiles[i][j] = Clock_tile(x, y)
                elif (tile_map[i][j] == 3):
                    self.tiles[i][j] = Grass_tile(x, y)
                elif (tile_map[i][j] == 4):
                    self.tiles[i][j] = Dirt_tile(x, y)
                elif (tile_map[i][j] == 5):
                    self.tiles[i][j] = Empty_tile(x, y)
                elif (tile_map[i][j] == 6):
                    self.tiles[i][j] = Empty_tile(x, y)
                elif (tile_map[i][j] == 7):
                    self.tiles[i][j] = Invisible_tile(x, y)
                elif (tile_map[i][j] == 8):
                    self.tiles[i][j] = Brick_tile(x, y)
                elif (tile_map[i][j] == 9):
                    self.tiles[i][j] = Coin_tile(x, y)
                elif (tile_map[i][j] == 10):
                    self.tiles[i][j] = Start_tile(x, y)
                elif (tile_map[i][j] == 11):
                    self.tiles[i][j] = Finish_tile(x, y)
                elif (tile_map[i][j] == 12):
                    self.tiles[i][j] = Empty_tile(x, y)
                elif (tile_map[i][j] == 13):
                    self.tiles[i][j] = Rock_tile(x, y)
                elif (tile_map[i][j] == 14):
                    self.tiles[i][j] = Lava_tile(x, y)
                elif (tile_map[i][j] == 15):
                    self.tiles[i][j] = Dirt_rock_tile(x, y)
                else:
                    self.tiles[i][j] = Empty_tile(x, y)

                if level_nb==8:
                    sx, sy = 0, 0


                if (tile_map[i][j] == 10):
                    #Starting coordinates
                    sx, sy = x, y
                    # print("start at", x, y)

        self.starting_coord = [sx, sy]
