from tkinter import *
import random
import time

move = 1
game = []
winner = 0


for i in range(3):
        b=[]
        for j in range(3):
            b.append(3*i+j)
        game.append(b)
def test(game):
    global winner 
    for i in range(3):
        if game[i][0]==game[i][1] and game[i][0]==game[i][2] and game[i][1]==game[i][2]:
            print("Winner: ", game[i][1])
            winner = game[i][1]
            label["text"] = "Winner: " + winner
        if game[0][i]==game[1][i] and game[0][i]==game[2][i] and game[1][i]==game[2][i]:
            print("Winner: ", game[0][i])
            winner = game[0][i]
            label["text"] = "Winner: " + winner
    if game[0][0]==game[1][1] and game[0][0]==game[2][2] and game[1][1]==game[2][2]:
        print("Winner: ", game[0][0])
        winner = game[0][0] 
        label["text"] = "Winner: " + winner
    if game[0][2]==game[1][1] and game[0][2]==game[2][0] and game[1][1]==game[2][0]:
        print("Winner: ", game[0][2])
        winner = game[0][2]
        label["text"] = "Winner: " + winner
    
            
def press(e):
    global move
    if winner==0:
        if  not ((e.widget["text"]=="X")or(e.widget["text"]=="O")):
            if move==1:
                a = int(e.widget["text"])-1
                game[a//3][a%3]="X"  
                e.widget["text"] = "X"
                move = 0
            else:
                a = int(e.widget["text"])-1
                game[a//3][a%3]="O"
                e.widget["text"] = "O"
                move = 1
            print(game)
            test(game)
    
root = Tk()
root.title("Крестики-нолики")
button = []
button_1 = Button(root)
button_1.configure(text = "1",width=4,height= 2 )
button_1.grid(row=0,column=0)

button_2 = Button(root)
button_2.configure(text = "2",width=4,height= 2 )
button_2.grid(row=0,column=1)

button_3 = Button(root)
button_3.configure(text = "3",width=4,height= 2 )
button_3.grid(row=0,column=2)

button_4 = Button(root)
button_4.configure(text = "4",width=4,height=2 )
button_4.grid(row=1,column=0)

button_5 = Button(root)
button_5.configure(text = "5",width=4,height= 2 )
button_5.grid(row=1,column=1)

button_6 = Button(root)
button_6.configure(text = "6",width=4,height= 2 )
button_6.grid(row=1,column=2)

button_7 = Button(root)
button_7.configure(text = "7",width=4,height= 2 )
button_7.grid(row=2,column=0)

button_8 = Button(root)
button_8.configure(text = "8",width=4,height= 2 )
button_8.grid(row=2,column=1)

button_9 = Button(root)
button_9.configure(text = "9",width=4,height= 2 )
button_9.grid(row=2,column=2)

label = Label(text="")
label.grid(row=3,column=1)
root.bind_class('Button', '<1>', press)


root.mainloop()

