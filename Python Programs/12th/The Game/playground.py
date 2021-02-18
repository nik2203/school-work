'''
import pyxel
import math
#from funcs import App_Loading

class App():

    
    def __init__(self):
        pyxel.init(256,256, fps=60, scale=6)
        self.x=256//2
        self.y=256//2
        self.player_alive=False
        self.game_inst=False
        self.hit=False
        self.colour=9
        self.lives=5
        pyxel.load('the_game_res2.pyxres',image=True)
        pyxel.run(self.update_player,self.draw)
        

    def update_player(self):
        
        #Game Start
        if self.player_alive==False and pyxel.btnp(pyxel.KEY_S) and self.game_inst==False:
            pyxel.cls(0)
            self.player_alive=True
            self.game_inst=True
            self.x=256//2
            self.y=256//2

        else:

            #Player Movement
            if self.player_alive==True and self.game_inst==True:
                
                if pyxel.btn(pyxel.KEY_LEFT):
                    self.x = (self.x - 2)%256

                if pyxel.btn(pyxel.KEY_RIGHT):
                    self.x = (self.x + 2)%256

                if pyxel.btn(pyxel.KEY_UP):
                    self.y = (self.y - 2)%256

                if pyxel.btn(pyxel.KEY_DOWN):
                    self.y = (self.y + 2)%256

                if pyxel.btnp(pyxel.KEY_F):
                    self.hit=True


            if pyxel.btnp(pyxel.KEY_Q) and self.game_inst==True:
                pyxel.quit()

            if self.y>200 and self.game_inst==True and self.lives>0:
                self.lives-=1
                self.x=256//2
                self.y=256//2
                pass

            if self.player_alive==True and self.lives==0:
                self.player_alive=False

            if self.player_alive==False and self.game_inst==True and pyxel.btnp(pyxel.KEY_R):
                pyxel.cls(0)
                self.player_alive=True
                self.x=80
                self.y=100
                self.lives=5

        if pyxel.btnp(pyxel.KEY_R) and self.player_alive==False and self.lives==0:
             pyxel.cls(0)
             self.player_alive=True
             self.lives=5
             self.x=80
             self.y=100



    def draw(self):
        
        #Game Start
        if self.player_alive==False and self.game_inst==False:
            pyxel.cls(0)
            pyxel.text(100,256//2,'PRESS S TO START', pyxel.frame_count%16)
        
        #PlayerLoad
        if self.player_alive==True:
            pyxel.cls(0)
            pyxel.blt(self.x,self.y,0,0,13,15,25,0)
        
        #In-Game
        if self.player_alive==True and self.game_inst==True:
            ##pyxel.cls(0)
            pyxel.blt(self.x,self.y,0,0,13,15,25,0)
            pyxel.text(1,0,'x:'+str(self.x),4)
            pyxel.text(1,10,'y:'+str(self.y),4)
            pyxel.text(1,20,'Lives:'+str(self.lives),4)
            pyxel.text(200,0,'Frame Count:'+str(pyxel.frame_count),4)
        
        #Restart
        if self.player_alive==False and self.game_inst==True and self.lives==0:
            pyxel.cls(0)
            pyxel.text(110,(256//2)-10,'GAME OVER',pyxel.frame_count%16)
            pyxel.text(90,(256//2)+5,'PRESS R TO RESTART',pyxel.frame_count%16)

        #Hitting
        if self.player_alive==True and self.hit==True:
            self.hit=False

App()
'''
"""
Small snippet demonstrating diagonal pixel movement for Seubmarine on Discord.

Kris Pritchard / @krisrp
"""
import math
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.cls(0)

        self.x = 60
        self.y = 60
        # Give run the update/draw callbacks
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_S):
            self.y += 1
        if pyxel.btn(pyxel.KEY_A):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= 1
            self.y -= 1
        if pyxel.btn(pyxel.KEY_E):
            self.x += 1
            self.y -= 1
        if pyxel.btn(pyxel.KEY_Z):
            self.x -= 1
            self.y += 1
        if pyxel.btn(pyxel.KEY_C):
            self.x += 1
            self.y += 1

    def draw(self):
        # Don't forget to clear screen on every frame!
        pyxel.cls(0)

        # Draw the pyxel location:
        pyxel.text(5, 5, f'({self.x}, {self.y})', 7)

        # Draw the text at position: (text_x, text_y)
        pyxel.pset(self.x, self.y, 8)



if __name__ == "__main__":
    App()