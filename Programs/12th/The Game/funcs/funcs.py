import pyxel

GRAVITY = 1
FLOOR_LEVEL = 200
VY = 0
VX = 0


#Loading Screen
class App_Loading:

    def __init__(self):
        pyxel.init(256, 256,scale=5)
        pyxel.image(0).load(0, 0, "bg.png")
        self.select = False
        pyxel.run(self.update, self.draw)

#Declaring region where  option is highlighted
    def update(self):
        pyxel.mouse(True)       
        if (pyxel.mouse_x>95 and pyxel.mouse_x<165) and ((pyxel.mouse_y<145 and pyxel.mouse_y>132) or (pyxel.mouse_y>148 and pyxel.mouse_y<165)):
            self.select = True
        else:
            self.select = False            
        if pyxel.btn(pyxel.KEY_S):
            global game
            game=True

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
        pyxel.text(115,135,'START (S)',0)
        pyxel.text(103,155,'HIGHSCORES (H)',0)  #file does not exist rn
        pyxel.text(1,0,'x:'+str(pyxel.mouse_x),4)
        pyxel.text(1,10,'y:'+str(pyxel.mouse_y),4)

        if self.select and (pyxel.mouse_y<145 and pyxel.mouse_y>132):
            pyxel.rectb(95,132,70,12,0)
        if self.select and (pyxel.mouse_y>148 and pyxel.mouse_y<165):
            pyxel.rectb(95,152,70,12,0,)

