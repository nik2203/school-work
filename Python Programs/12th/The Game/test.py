import pyxel

GRAVITY_CONSTANT = 1
WINDOW_SIZE = 200
FLOOR_LEVEL = 150


class App():
    def __init__(self):
        pyxel.init(WINDOW_SIZE, WINDOW_SIZE, fps=30)
        self.x = 50
        self.y = FLOOR_LEVEL
        self.vx = 0
        self.vy = 0
        self.speed = 2
        self.on_floor = True
        self.jump_power = -10
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = (self.x - self.speed) % WINDOW_SIZE

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = (self.x + self.speed) % WINDOW_SIZE

        if pyxel.btnp(pyxel.KEY_UP) and self.on_floor:
            self.vy = self.jump_power
            self.on_floor = False
        if not(self.on_floor):
            self.vy += GRAVITY_CONSTANT

        self.x += self.vx
        self.y += self.vy

        if self.y > (FLOOR_LEVEL - 8):
            self.y = FLOOR_LEVEL - 8
            self.on_floor = True

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 8, 8, 8)
        pyxel.rect(0, FLOOR_LEVEL, WINDOW_SIZE, WINDOW_SIZE, 3)
        pyxel.text(0, 0, str((self.x, self.y)), 8)


App()
