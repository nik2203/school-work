#Function to define bullet
class Bullet:
    def __init__(self):
        self.x = -10
        self.y = 0
        self.vx = 0
        self.vy = 0
        
    def fire(self, x, y):
        self.x = x
        self.y = y
        self.vx = B_SPD_X
        self.vy = -B_SPD_Y
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY

