import turtle
import random

# Game of Connect 4 

screen = turtle.Screen()
screen.setup(800,700)
screen.setworldcoordinates(-500,-500,500,500)
screen.title("Connect 4")
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0) # -- Immediate draw and update
t = turtle.Turtle()
t.up()
#score.hideturtle()

def draw_rectangle():
  t.goto(-350, -100)
  t.fillcolor('skyblue')
  t.pendown()
  t.begin_fill()
  t.goto(-350, 500)
  t.goto(350, 500)
  t.goto(350, -100)
  t.goto(-350, -100)
  t.end_fill()
  t.up()
# 6 rows and 7 columns

Nrows = 6
Ncols = 7

def draw_circle(x, y, r, fillcolor):
  # Draw a circle at (x, y), radius r and fill color 
  t.goto(x, y)
  t.setheading(-90)
  t.fillcolor(fillcolor)
  t.begin_fill()
  t.circle(r)
  t.end_fill()


board = []

nRows = 6
nCols = 7

board = [[0 for i in range(nCols)] for j in range(nRows)]

def draw_board():
  draw_rectangle()

  for kk in range(Nrows):
    for jj in range(Ncols):
      if board[kk][jj] == 0:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'white')
      if board[kk][jj] == 1:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'red')
      if board[kk][jj] == 2:
        draw_circle(-340 + jj*100, 450 - kk*100, 40, 'blue')

        def lowest_row(col):
  # Find the lowest available row in a given column
  r = -1
  for kk in range(Nrows-1, -1, -1):
    if board[kk][col] == 0:
      r = kk
      break
      
  return r



turtle.mainloop()