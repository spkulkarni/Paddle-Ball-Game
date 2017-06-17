import tkinter
from tkinter import *
import random
from tkinter import messagebox
import time
tk = Tk()


tk.title("Paddleball Game")
tk.resizable(0,0) # tk window cannot be resized in x or y
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=600, height=600, bd=0,bg='black', highlightthickness=0) #no borders around the canvas
canvas.pack()
tk.update()
t=0

sec=0




class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 200, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:

                return True
        return False

    def draw(self):
        if self.hit_bottom == False:

            self.canvas.move(self.id, self.x, self.y)

            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 3
            if pos[3] >= self.canvas_height:
                self.y = -3

            if pos[3] >= self.canvas_height:
                self.hit_bottom = True

            if self.hit_paddle(pos) == True:
                self.y = -3
                global t
                t=t+1

            if pos[0] <= 0:
                self.x = 3
            if pos[2] >= self.canvas_width:
                self.x = -3

            if ball.hit_bottom == False:
                self.canvas.after(10, self.draw) # miliseconds, function



class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)



    def draw(self):
        if ball.hit_bottom == False:

            self.canvas.move(self.id, self.x, 0)

            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0
            if pos[2] >= self.canvas_width:
                self.x = 0

            self.canvas.after(10, self.draw)
        else:
            global t
            messagebox.showinfo(" ","Game Over!!!!your score is  " + str(t))


    def turn_left(self, event):
        self.pos = self.canvas.coords(self.id)

        if self.pos[0] >= 1:
            self.x = -3

    def turn_right(self, event):
        self.pos = self.canvas.coords(self.id)

        if self.pos[2] <= self.canvas_width-1:
            self.x = 3

paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

#time=0
def start_game(event):
    ball.draw()
    #global start
    #start=time.clock()
    #app=App()
    #t=time+1

global start,stop

start=time.clock()

canvas.bind_all("<Button-1>", start_game)

paddle.draw()

tk.mainloop()

