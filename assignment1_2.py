import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')

t.speed(0)
n = 36
h = 0

for i in range(200):
  c = colorsys.hsv_to_rgb(h, 1, 0.9)
  h += 1 / n
  t.color(c)
  t.left(170)
  for j in range(6):
    t.forward(210)
    t.left(200)
