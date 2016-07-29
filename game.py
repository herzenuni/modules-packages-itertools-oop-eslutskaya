## game.py
## В этом файле будет располагаться класс, в котором
##  будет содержаться логика игры
from config import config
from graphics import *

from stats import Stats


import player
class Game:

        def __init__(self, whos_turn, path_to_stat_file, field_size, stat = None):
                self.whos_turn = whos_turn
                self.path_to_stat_file = path_to_stat_file
                self.field_size = field_size
                self.stat = stat
      
        def new_game(self, whos_turn, path_to_stat_file, field_size, stat):
                self.move = whos_turn
                self.game = []
                self.winner = True
                self.n = field_size
                for i in range(self.n):
                        b=[]
                        for j in range(self.n):
                            b.append(2+j+i*self.n)
                        self.game.append(b)
                        
        def test(self):
                for i in range(self.n): 
                        if self.game[i][0]==self.game[i][1] and self.game[i][0]==self.game[i][2] and self.game[i][1]==self.game[i][2]:
                            return self.game[i][1]
                        if self.game[0][i]==self.game[1][i] and self.game[0][i]==self.game[2][i] and self.game[1][i]==self.game[2][i]:
                            return self.game[0][i]
                if self.game[0][0]==self.game[1][1] and self.game[0][0]==self.game[2][2] and self.game[1][1]==self.game[2][2]:
                        return self.game[0][0] 
                if self.game[0][2]==self.game[1][1] and self.game[0][2]==self.game[2][0] and self.game[1][1]==self.game[2][0]:
                        return self.game[0][2]
        def press(self,i,j):
                if not (self.winner or self.winner == 0) and (self.game[i][j] != 0 and self.game[i][j] != 1 ):
                        if self.move == 1:
                                self.game[i][j] = self.move
                                self.move = 0
                                self.winner = self.test()
                                if self.winner == 1 or self.winner == 0: print(self.winner)
                                return 1
                        elif self.move == 0:
                                self.game[i][j] = self.move
                                self.move = 1
                                self.winner = self.test()
                                if self.winner == 1 or self.winner == 0: print(self.winner)
                                return 0


stats = Stats(config["path_to_stat_file"])
game = Game(config["whos_turn"], config["path_to_stat_file"], config["field_size"], stats)

root = Tk()
graphics = Graphics(root, game, config["canvas_size"], config["field_size"])

root.mainloop()
