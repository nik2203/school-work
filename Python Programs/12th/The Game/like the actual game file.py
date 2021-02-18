import pyxel

GRAVITY = 0.075
DY = 3
DX = 2

class Button:
    """Create a button on the screen."""
    def __init__(self, x, y, w, h, label, color):
        # Create the splat at position (x, y)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.label = label
        self.color = color

    def draw(self):
        # Draw our button
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)
        pyxel.text(self.x+10, self.y+4, self.label, (self.color+2)%15)

    def check_clicked(self, mouse_x, mouse_y):
        if self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h:
            print('clicked!')
            return True
        else:
            print('not clicked!')
            return False



#Loading Screen
class App_Loading:

    def __init__(self):
        pyxel.init(256, 256,scale=5)
        pyxel.image(0).load(0, 0, "assets\\bg.png")
        pyxel.mouse(True)
        self.buttonA = Button(95,132,70,12, 'Start (S)', 2)
        self.buttonB = Button(95,152,70,12, 'Highscores (H)', 8)
        
        pyxel.run(self.update, self.draw)

#Declaring region where  option is highlighted
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if self.buttonA.check_clicked(pyxel.mouse_x, pyxel.mouse_y):
                self.buttonA.color = (self.buttonA.color + 1) % 15
                print('Do the thing for button A')
            if self.buttonB.check_clicked(pyxel.mouse_x, pyxel.mouse_y):
                self.buttonB.color = (self.buttonB.color + 1) % 15
                print('Do the thing for button B')

#Drawing options and highlighting them
    def draw(self):
        pyxel.cls(0)
        # blt arguments:
        # x position = 0
        # y position = 0
        # img bank (0-2) = 0 
        # u img/texture coordinate = 0
        # v img/texture coordinate = 0
        # w img/texture width = 100
        # v img/texture/height = 100
        pyxel.rect(120,135,30,10,9)
        pyxel.blt(0, 0, 0, 0, 0, 1280, 704)
        pyxel.text(1,0,'x:'+str(pyxel.mouse_x),4)
        pyxel.text(1,10,'y:'+str(pyxel.mouse_y),4)
        
        self.buttonA.draw()
        self.buttonB.draw()

App_Loading()