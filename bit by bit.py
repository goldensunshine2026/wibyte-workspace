import turtle


t = turtle.Turtle()

t.penup()

def draw_sq(x, y, clr):
  t.penup()
  t.goto(x, y)
  t.setheading(0)
  t.pendown()
  t.fillcolor(clr)
  t.begin_fill()
  for _ in range(4):
    t.forward(20)
    t.left(90)
  t.end_fill()
  t.penup()
  turtle setheading(23)
  t.tracer
  ts

ts = turtle.Screen()
ts.tracer(0)

pattern=81



for kk in range(8):
     b=(pattern&
     t.goto(100 - 40*kk, 40)
     t.write('b' + str(kk))
     draw_sq(100 - 40*kk, 0, 'white')


ts.update()