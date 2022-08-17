import pyxel
from random import randint
from funcs import funcs



class Platform():
    def __init__(self,x,y,w,h,colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = colour

    def draw(self):
        # Draw our button
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)



class App():

    def __init__(self):
        pyxel.init(256, 256, fps=24, scale=6)
        self.x = 50
        self.y = funcs.FLOOR_LEVEL
        self.player_alive = False
        self.game_inst = False
        self.hit = False
        self.colour = 9
        self.vy = funcs.VY
        self.vx = funcs.VX
        self.speed=2
        self.grav = funcs.GRAVITY
        self.jump = True
        self.jump_pow = -10
        self.scroll=4
        self.floor = [Platform((randint(2,6)*30),randint(130,170),40,8,10) for i in range(3)]
        pyxel.image(0).load(0, 0, r"assets\TheUnderground.png")
        pyxel.run(self.update_player, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        for i, v in enumerate(self.floor):
            self.floor[i] = self.update_floor(*v)
            x,y=self.update_floor(*v)

        self.update_player()

        if self.y+8==y and self.jump==False:
                    self.jump=True
            

    def update_player(self):

        if self.player_alive == False and pyxel.btnp(pyxel.KEY_S) and self.game_inst == False:
            pyxel.cls(0)
            self.player_alive = True
            self.game_inst = True
            self.x = 50
            self.y = 192

        else:

            # Player Movement
            if self.player_alive == True and self.game_inst == True:

                if pyxel.btn(pyxel.KEY_LEFT):
                    self.x = self.x - self.speed

                if pyxel.btn(pyxel.KEY_RIGHT):
                    self.x = self.x + self.speed

                if pyxel.btnp(pyxel.KEY_UP) and self.jump:
                    self.vy = self.jump_pow
                    self.jump = False

                if not(self.jump):
                    self.vy += funcs.GRAVITY

                X=self.x
                Y=self.y
                for i in self.floor:
                    print(i.x,i.y,self.x,self.y)
                    if ((X+4>=i.x) and (X+4<=i.x+40)) and Y+8==i.y:
                        self.jump=True
                        self.vy=0

                self.x += self.vx
                self.y += self.vy

                if self.y > (funcs.FLOOR_LEVEL-8):
                    self.y = funcs.FLOOR_LEVEL-8
                    self.jump = True
                
                if self.x < 0:
                    self.x = 0
                
                if self.x>120:
                    self.x = 120
                    
            if pyxel.btnp(pyxel.KEY_Q) and self.game_inst == True:
                pyxel.quit()

            if self.player_alive == False and self.game_inst == True and pyxel.btnp(pyxel.KEY_R):
                pyxel.cls(0)
                self.player_alive = True
                self.x = 50
                self.y = 200

    def update_floor(self, x, y):
        return x, y

    def draw(self):

        # Game Start
        if self.player_alive == False and self.game_inst == False:
            pyxel.cls(0)
            pyxel.text(100, 256//2, 'PRESS S TO START', pyxel.frame_count % 16)

        # PlayerLoad
        #if self.player_alive == True:
         #   pyxel.cls(0)
          #  pyxel.blt(self.x, self.y, 0, 0, 0, 9, 8, 3)

        # In-Game
        if self.player_alive == True and self.game_inst == True:
            pyxel.blt(0, 0, 0, 0, 0, 1280, 704)
            
            #Scrolling
            offset = pyxel.frame_count % 256
            for i in range(2):
                pyxel.blt(i * 256 - offset, 0, 0, 0,0, 256, 256)

            # Drawing the rectangle
            pyxel.rect(self.x, self.y, 8, 8, self.colour)
            pyxel.text(1, 0, 'x:'+str(self.x), 4)
            pyxel.text(1, 10, 'y:'+str(self.y), 4)
            pyxel.text(200, 0, 'Frame Count:'+str(pyxel.frame_count), 4)


            #Drawing blocks
            for i in self.floor:
                i.draw()

        # Restart
        if self.player_alive == False and self.game_inst == True:
            pyxel.cls(0)
            pyxel.text(110, (256//2)-10, 'GAME OVER', pyxel.frame_count % 16)
            pyxel.text(90, (256//2)+5, 'PRESS R TO RESTART',
                       pyxel.frame_count % 16)

        # Hitting
        if self.player_alive == True and self.hit == True:
            self.hit = False


App()
