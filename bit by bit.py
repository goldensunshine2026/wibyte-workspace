import turtle
import time

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

ts = turtle.Screen()
ts.tracer(0)

pattern=0b01100110

style=0

for cnt in range(1000):
  if style == 0:
    pattern = pattern << 2
    if pattern > 0b11111111: 
      pattern = 0b00000011
  if style == 1:
    pattern = pattern >> 2
    if pattern == 0b00000000:
      pattern = 0b11000000
  if style == 2:
    pattern = pattern ^ 0b11111111
  if style == 3:
    if pattern == 0b11111111:
      pattern = 0b00000000
    pattern = pattern | (1 << cnt%8)
  if style == 5:
    pattern = 0b01111111
    


  ts.tracer(0)
  for kk in range(8):
    b = (pattern & (2**kk)) >> kk
    t.goto(100 - 40*kk, 40)
    t.write('b' + str(kk))
    if b == 1:
      draw_sq(100- 40*kk, 0, 'blue')
    else:
      draw_sq(100 - 40*kk, 0, 'red')
  ts.update()
  time.sleep(0.5)
turtle.mainloop()