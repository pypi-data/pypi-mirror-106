import turtle

def screensize(a,b):
  turtle.screensize(a,b)

def startfill():
  turtle.begin_fill()

def endfill():
  turtle.end_fill()

def up(a):
  turtle.forward(a)

def down(a):
  turtle.left(180)
  turtle.forward(a)

def left(a):
  turtle.left(90)
  turtle.forward(a)

def right(a):
  turtle.right(90)
  turtle.forward(a)

def turn_left(a):
  turtle.left(a)

def turn_right(a):
  turtle.right(a)

def startdraw():
  turtle.screensize(500,500)
