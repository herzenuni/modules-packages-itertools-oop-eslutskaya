

## graphics.py
## В этом файле будет располагаться класс, в котором
##  будет описан графический интерфейс для работы игры

from tkinter import *
class Graphics:
    """
    Интерфейсссссссссс
    """
    canvas_size = 360
    n = 3  #Количество клеток в одной строке/столбце
    grid_width = 3  #Толщина решетки
    rect = []     #Двумерный массив с квадратами, которые входят в canvas
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root, width = self.canvas_size , height = self.canvas_size, bg = "white")
        self.canvas.pack()
        self.draw_grid() #Рисует решетку
        self.draw_rect() #Рисует квадраты
        self.canvas.tag_bind('rect', '<Button-1>',self.press)
        #Все виджеты с тегом "rect" при нажатии левой кнопки мыши, будут выполнять команду press

    def press(self,event):
        c = self.canvas_size / self.n  #Размер клетки
        #global move
        #if move == 0:
            #move = 1
            #Узнаем свободна ли клетка и отсутствует ли победитель
        self.draw_toe(event.x,event.y,c) #Передаем координаты курсора при нажатии на один из квадратов и размер клетки
        #else:
            #move = 0
            #Узнаем свободна ли клетка и отсутствует ли победитель 
        self.draw_tick(event.x,event.y,c) #Передаем координаты курсора при нажатии на один из квадратов и размер клетки


    def draw_grid(self):
        for i in range(1,self.n):
            self.canvas.create_line([self.canvas_size/self.n*i,0], [self.canvas_size/self.n*i, self.canvas_size], width = self.grid_width, fill = "black", tag = "grid")
            self.canvas.create_line([0, self.canvas_size/self.n*i], [self.canvas_size, self.canvas_size/self.n*i], width = self.grid_width, fill = "black", tag = "grid")

    def draw_rect(self):
        s = 0
        for i in range(0,self.n):
            b = []
            for j in range(0,self.n):
                c = self.canvas.create_rectangle([i*self.canvas_size/self.n, j*self.canvas_size/self.n], [i*self.canvas_size/self.n+self.canvas_size/self.n,j*self.canvas_size/self.n+self.canvas_size/self.n],fill = "white")
                self.canvas.itemconfig(c,tags = (s,"rect"))
                b.append(c)
                s+=1
            self.rect.append(b)

    def draw_toe(self,x, y, c):
        k = c/7              #Отступ от сетки
        self.canvas.create_oval([x//c*c+k, y//c*c+k],[x//c*c+c-k, y//c*c+c-k], width = 4) #Рисует нолик

    def draw_tick(self,x, y, c):
        k = c/7              #Отступ от сетки
        self.canvas.create_line([x//c*c+k, y//c*c+k], [x//c*c+c-k,y//c*c+c-k], width = 5)  #Рисует крестик
        self.canvas.create_line([x//c*c+k, y//c*c+c-k], [x//c*c+c-k, y//c*c+k], width = 5)
     


root = Tk()
g=Graphics(root)
root.mainloop()
