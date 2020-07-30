from tkinter import *
from random import choice

root = Tk()

root.title("SNAKE")

b = [[True for i in range(30)] for j in range(20)]

lst_col = [i for i in range(30)]
lst_lin = [i for i in range(20)]

bonus = {
    'x' : '',
    'y' : '0'
}

def generare():
    global bonus
    nr1 = choice(lst_lin)
    nr2 = choice(lst_col)
    while not b[nr1][nr2]:
        nr1 = choice(lst_lin)
        nr2 = choice(lst_col)
    a[nr1][nr2].config(bg = "red")
    bonus['y'] = nr1
    bonus['x'] = nr2

def createSnake():
    Score.config(text = str(score))
    if run:
        pass
    else:
        for i in snake:
            a[i[0]][i[1]].config(bg="white")
score = 1
run = True
last = "a"

def move():

    global snake, nr1, nr2, run,GameFrame,last,size,score
    if run:
        if last == "a":
            last  = "a"
            nr2 -= 1
            if nr2 < 0:
                nr2 = 29
        elif last == "d":
            size = 2
            last = 'd'
            nr2 += 1
            if nr2 == 30:
                nr2 = 0
        elif last == "w":
            size = 2
            last = 'w'
            nr1 -= 1
            if nr1 < 0:
                nr1 = 19
        elif last == "s":
            size =2
            last = 's'
            nr1 += 1
            if nr1 == 20:
                nr1 = 0

        if not b[nr1][nr2]:
            run = False

        b[nr1][nr2] = False
        a[nr1][nr2].config(bg = "black")
        if bonus['y'] != nr1 or bonus['x'] != nr2:
            a[snake[0][0]][snake[0][1]].config(bg = "white")
            b[snake[0][0]][snake[0][1]] = True
            snake.pop(0)
        else:
            score += 1
            generare()

        snake.append((nr1,nr2))
        createSnake()
        root.after(250, move)


def direction(e):
    global snake, nr1, nr2, run,GameFrame,last,size,score
    if run:
        key = e.char.lower()
        if key == "a":
            if last != 'd' or score == 1:
                last  = "a"
        elif key == "d":
            if last != 'a' or score == 1:
                last = 'd'
        elif key == "w":
            if last != 's'or score == 1:
                last = 'w'
        elif key == "s":
            if last != 'w' or score == 1:
                last = 's'

Score = Label(root, text = str(score), bg = "black", fg = "white", font = "50",width = 10)
Score.pack(pady = 15)
GameFrame = Frame(root, bd = 1, relief = "groove")
GameFrame.pack(pady = 15,padx = 10)

a = [[Label(GameFrame,width = 2,bg = "white") for i in range(50)] for j in range(20)]

for i in range(20):
    for j in range(30):
        a[i][j].grid(row = i, column = j)

root.after(250,move)

root.bind("<Key>", direction)

nr1 = choice(lst_lin)
nr2 = choice(lst_col)

snake = [(nr1,nr2)]
a[nr1][nr2].config(bg = "black")
b[nr1][nr2] = False
generare()

root.mainloop()