import pyxel
import mysql.connector

class High():

    def __init__(self):
        pyxel.init(256,256, fps=24, scale=6)
        self.game_inst=False
        pyxel.image(0).load(0, 0, r"assets\TheUnderGround.png")
        pyxel.run(self.update_player,self.draw)
    
    def update_player(self):

            if pyxel.btnp(pyxel.KEY_Q) and self.game_inst==True:
                pyxel.quit()

    def draw(self):

        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 1280, 704)
        
High()