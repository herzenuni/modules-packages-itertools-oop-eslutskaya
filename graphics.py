

## graphics.py
## В этом файле будет располагаться класс, в котором
##  будет описан графический интерфейс для работы игры

from tkinter import *

class Graphics:
    """
    Интерфейсссссссссс
    """
    
    def __init__(self, root, game, canvas_size, field_size):
        self.game = game  
        self.root = root
        self.canvas_size = canvas_size                     
        self.n = field_size                             # Количество клеток в одной строке/столбце
        self.rect_size = canvas_size / self.n           # Размер квадрата
        self.grid_width = 3                             # Толщина решетки

        self.made_menu()                                # Создаем меню
        self.made_input()                               # Ввод имен 

        self.frame_canvas = Frame(self.root)
        self.canvas = Canvas(self.frame_canvas, width = self.canvas_size, height = self.canvas_size, bg = "white")
        self.canvas.grid()
        self.frame_canvas.grid()
        self.new_game()
        
    def made_menu(self):
        m = Menu(self.root)                            
        self.root.config(menu = m)
        fm = Menu(m)
        m.add_cascade(label = "Game", menu = fm)
        fm.add_command(label = "New Game", command = self.new_game)
        fm.add_command(label = "Close game", command = self.close_game)

    def made_input(self):
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

    def new_game(self):
        self.game.new_game(self.game.whos_turn, self.game.path_to_stat_file, self.game.field_size, self.game.stat)
        self.frame_canvas.grid_forget()
        self.frame_player.grid()
        self.draw_rect()                                # Рисует квадрат
        self.draw_grid()                                # Рисует решетку
        self.canvas.tag_bind('rect', '<Button-1>',self.press)
        #Все виджеты с тегом "rect" при нажатии левой кнопки мыши, будут выполнять команду press


    def go(self):
            self.game.winner = None
            self.game.player_1 =self.player_inp_1.get()
            self.game.player_2 =self.player_inp_2.get()
            print(self.game.player_1,self.game.player_2)
            self.frame_player.grid_forget()
            self.frame_canvas.grid()

    def press(self,event):
        i = event.y // self.rect_size
        j = event.x // self.rect_size
        self.move = self.game.press(int(i),int(j))             # Узнаем свободна ли клетка и отсутствует ли победитель
        if self.move == 1:
                self.draw_tick(event.x,event.y,self.rect_size) # Передаем координаты курсора при нажатии на один из квадратов и размер клетки
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
     

