

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

        self.canvas = Canvas(self.root, width = self.canvas_size, height = self.canvas_size, bg = "white")
        self.canvas.pack()
        self.draw_rect()                                # Рисует квадрат
        self.draw_grid()                                # Рисует решетку
        
        self.canvas.tag_bind('rect', '<Button-1>',self.press)
        #Все виджеты с тегом "rect" при нажатии левой кнопки мыши, будут выполнять команду press

    def press(self,event):
        i = event.y // self.rect_size
        j = event.x // self.rect_size
        self.move = self.game.press(int(i),int(j))            # Узнаем свободна ли клетка и отсутствует ли победитель
        if self.move == 1:
                self.draw_tick(event.x,event.y,self.rect_size) #Передаем координаты курсора при нажатии на один из квадратов и размер клетки
        elif self.move == 0:
                 self.draw_toe(event.x,event.y,self.rect_size) #Передаем координаты курсора при нажатии на один из квадратов и размер клетки
                


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
     

