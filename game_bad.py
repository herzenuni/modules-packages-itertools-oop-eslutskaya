## game.py
## В этом файле будет располагаться класс, в котором
##  будет содержаться логика игры


#from stats import Stats
from config import config
#from graphics import *



#import player
class Game:
        player_1 = None
        player_2 = None
        def __init__(self, whos_turn, path_to_stat_file, field_size, stat = None):
                self.stat = stat
                Game.new_game(whos_turn, path_to_stat_file, field_size)

        @staticmethod
        def new_game( whos_turn, path_to_stat_file, field_size):
                Game.move = whos_turn
                Game.game = []
                Game.winner = True     
                Game.n = field_size
                for i in range(Game.n):
                        b=[]
                        for j in range(Game.n):
                            b.append(2+j+i*Game.n)
                        Game.game.append(b)
        @staticmethod               
        def test():
                for i in range(Game.n): 
                        if Game.game[i][0]==Game.game[i][1] and Game.game[i][0]==Game.game[i][2] and Game.game[i][1]==Game.game[i][2]:
                            print("Winner: ", Game.game[i][1])
                            Game.winner = Game.game[i][1]
                        if Game.game[0][i]==Game.game[1][i] and Game.game[0][i]==Game.game[2][i] and Game.game[1][i]==Game.game[2][i]:
                            print("Winner: ", Game.game[0][i])
                            Game.winner = Game.game[0][i]
                if Game.game[0][0]==Game.game[1][1] and Game.game[0][0]==Game.game[2][2] and Game.game[1][1]==Game.game[2][2]:
                        print("Winner: ", Game.game[0][0])
                        Game.winner = Game.game[0][0] 
                if Game.game[0][2]==Game.game[1][1] and Game.game[0][2]==Game.game[2][0] and Game.game[1][1]==Game.game[2][0]:
                        print("Winner: ", Game.game[0][2])
                        Game.winner = Game.game[0][2]
        @staticmethod  
        def press(i,j):
                if not Game.winner and (Game.game[i][j] != 0 and Game.game[i][j] != 1 ):
                        if Game.move == 1:
                                Game.game[i][j] = Game.move
                                Game.move = 0
                                Game.test()
                                return 1
                        elif Game.move == 0:
                                Game.game[i][j] = Game.move
                                Game.move = 1
                                Game.test()
                                return 0

from tkinter import *
class Graphics:
    """
    Интерфейсссссссссс
    """
    
    def __init__(self,  canvas_size, field_size):
        self.root = Tk()
        m = Menu(self.root)                             # Меню
        self.root.config(menu = m)
        fm = Menu(m)
        m.add_cascade(label = "Game", menu = fm)
        fm.add_command(label = "New Game", command = self.new_game)
        fm.add_command(label = "Close game", command = self.close_game)
        self.canvas_size = canvas_size                     
        self.n = field_size                             # Количество клеток в одной строке/столбце
        self.rect_size = canvas_size / self.n           # Размер квадрата
        self.grid_width = 3                             # Толщина решетки


        self.frame_player = Frame(self.root)
        self.player_1 = Label(self.frame_player, text = "Enter Player 1 Name")        
        self.player_inp_1 = Entry(self.frame_player, width = 20, bd = 3)
        self.player_2 = Label(self.frame_player, text = "Enter Player 2 Name")        
        self.player_inp_2 = Entry(self.frame_player, width = 20, bd = 3)
        self.go = Button(self.frame_player, text = "Go", command = self.go)

        self.player_1.grid()
        self.player_inp_1.grid()
        self.player_2.grid()
        self.player_inp_2.grid()
        self.go.grid()
        self.frame_player.grid()

        
        self.canvas = Canvas(self.root, width = self.canvas_size, height = self.canvas_size, bg = "white")
        self.canvas.grid()
        self.new_game()
        self.root.mainloop()
    def new_game(self):
        Game.new_game(config["whos_turn"], config["path_to_stat_file"], config["field_size"])
        self.draw_rect()                                # Рисует квадрат
        self.draw_grid()                                # Рисует решетку
        self.canvas.tag_bind('rect', '<Button-1>',self.press)
        #Все виджеты с тегом "rect" при нажатии левой кнопки мыши, будут выполнять команду press


    def go(self):
            Game.winner = None
            Game.player_1 =self.player_inp_1.get()
            Game.player_2 =self.player_inp_2.get()
            print(Game.player_1,Game.player_2)
            self.frame_player.grid_forget()

            
    def press(self,event):
        i = int(event.y // self.rect_size)
        j = int(event.x // self.rect_size)
        self.move = Game.press(i,j)            # Узнаем свободна ли клетка и отсутствует ли победитель
        if self.move == 1:
                self.draw_tick(event.x,event.y,self.rect_size) #Передаем координаты курсора при нажатии на один из квадратов и размер клетки
        elif self.move == 0:
                 self.draw_toe(event.x,event.y,self.rect_size) #Передаем координаты курсора при нажатии на один из квадратов и размер клетки
                
    def close_game(self):
            self.root.destroy()

    def draw_grid(self):
        for i in range(1,self.n):
            self.canvas.create_line([self.canvas_size/self.n*i,0], [self.canvas_size/self.n*i, self.canvas_size], width = self.grid_width, fill = "black", tag = "grid")
            self.canvas.create_line([0, self.canvas_size/self.n*i], [self.canvas_size, self.canvas_size/self.n*i], width = self.grid_width, fill = "black", tag = "grid")

    def draw_rect(self):
                self.a = self.canvas.create_rectangle([0, 0], [self.canvas_size,self.canvas_size],fill = "white", tag = "rect")

    def draw_toe(self,x, y, c):         # Рисует нолик
        k = c/7                         # Отступ от сетки
        self.canvas.create_oval([x//c*c+k, y//c*c+k],[x//c*c+c-k, y//c*c+c-k], width = 4)

    def draw_tick(self,x, y, c):        # Рисует крестик
        k = c/7                         # Отступ от сетки
        self.canvas.create_line([x//c*c+k, y//c*c+k], [x//c*c+c-k,y//c*c+c-k], width = 5)  
        self.canvas.create_line([x//c*c+k, y//c*c+c-k], [x//c*c+c-k, y//c*c+k], width = 5)



game = Game(config["whos_turn"], config["path_to_stat_file"], config["field_size"])

graphics = Graphics(config["canvas_size"], config["field_size"])


