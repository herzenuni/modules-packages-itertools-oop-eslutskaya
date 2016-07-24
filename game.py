

## game.py
## В этом файле будет располагаться класс, в котором
##  будет содержаться логика игры
from graphics import *
from tkinter import *
class Game:
        def __init__(self):
                self.new_game()
      
        def new_game(self):
                self.move = 1
                self.game = []
                self.winner = 0
                self.n = 3
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
game = Game()
root = Tk()
graphics = Graphics(root,game)
root.mainloop()                    
