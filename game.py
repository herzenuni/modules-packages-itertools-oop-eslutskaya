## game.py
## В этом файле будет располагаться класс, в котором
##  будет содержаться логика игры
from config import config
from graphics import *

from stats import Stats


import player
class Game:

        def __init__(self, whos_turn, path_to_stat_file, field_size, stat = None):
                self.new_game(whos_turn, path_to_stat_file, field_size, stat)

      
        def new_game(self, whos_turn, path_to_stat_file, field_size, stat):
                self.move = whos_turn
                self.game = []
                self.winner = 0     #TODO Use None, young padavan
                self.n = field_size

                print (type (stat))
                for i in range(self.n):
                        b=[]
                        for j in range(self.n):
                            b.append(2+j+i*self.n)
                        self.game.append(b)
                print(self.game)
                        
        def test(self):
                for i in range(self.n): 
                        if self.game[i][0]==self.game[i][1] and self.game[i][0]==self.game[i][2] and self.game[i][1]==self.game[i][2]:
                            print("Winner: ", self.game[i][1])
                            self.winner = self.game[i][1]
                        if self.game[0][i]==self.game[1][i] and self.game[0][i]==self.game[2][i] and self.game[1][i]==self.game[2][i]:
                            print("Winner: ", self.game[0][i])
                            self.winner = self.game[0][i]
                if self.game[0][0]==self.game[1][1] and self.game[0][0]==self.game[2][2] and self.game[1][1]==self.game[2][2]:
                        print("Winner: ", self.game[0][0])
                        self.winner = self.game[0][0] 
                if self.game[0][2]==self.game[1][1] and self.game[0][2]==self.game[2][0] and self.game[1][1]==self.game[2][0]:
                        print("Winner: ", self.game[0][2])
                        self.winner = self.game[0][2]
        def press(self,i,j):
                if self.winner == 0 and (self.game[i][j] != 0 and self.game[i][j] != 1 ):
                        if self.move == 1:
                                self.game[i][j] = self.move
                                self.move = 0
                                self.test()
                                return 1
                        elif self.move == 0:
                                self.game[i][j] = self.move
                                self.move = 1
                                self.test()
                                return 0


stats = Stats(config["path_to_stat_file"])
game = Game(config["whos_turn"], config["path_to_stat_file"], config["field_size"], stats)

root = Tk()
graphics = Graphics(root, game, config["canvas_size"], config["field_size"])

root.mainloop()