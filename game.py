

## game.py
## В этом файле будет располагаться класс, в котором
##  будет содержаться логика игры

class Game:
        move = 1
        game = []
        winner = 0

        def __init__(self):
                pass
        def new_game(self):
                for i in range(3):
                        b=[]
                        for j in range(3):
                            b.append(3*i+j)
                        self.game.append(b)
        def test(self):
                for i in range(3):
                        
                        if self.game[i][0]==self.game[i][1] and self.game[i][0]==self.game[i][2] and self.game[i][1]==self.game[i][2]:
                            print("Winner: ", self.game[i][1])
                            self.winner = self.game[i][1]
                            label["text"] = "Winner: " + self.winner
                        if self.game[0][i]==self.game[1][i] and self.game[0][i]==self.game[2][i] and self.game[1][i]==self.game[2][i]:
                            print("Winner: ", self.game[0][i])
                            self.winner = self.game[0][i]
                            label["text"] = "Winner: " + self.winner
                if self.game[0][0]==self.game[1][1] and self.game[0][0]==self.game[2][2] and self.game[1][1]==self.game[2][2]:
                        print("Winner: ", self.game[0][0])
                        self.winner = self.game[0][0] 
                        label["text"] = "Winner: " + self.winner
                if self.game[0][2]==self.game[1][1] and self.game[0][2]==self.game[2][0] and self.game[1][1]==self.game[2][0]:
                        print("Winner: ", self.game[0][2])
                        self.winner = self.game[0][2]
                        label["text"] = "Winner: " + self.winner

        def press(self,e):
                if self.winner==0:
                        if  not ((e.widget["text"]=="X")or(e.widget["text"]=="O")):
                            if self.move==1:
                                a = int(e.widget["text"])-1
                                self.game[a//3][a%3]="X"  
                                e.widget["text"] = "X"
                                self.move = 0
                            else:
                                a = int(e.widget["text"])-1
                                self.game[a//3][a%3]="O"
                                e.widget["text"] = "O"
                                self.move = 1
                            self.test()
                     