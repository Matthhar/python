from graphics import *

data = [52, 47, 57, 49, 59, 62, 44, 76, 52, 52, 44, 59, 59, 79, 59, 42, 57, 48, 80, 43, 72, 74, 59, 44, 57, 55, 49, 54, 54]

window = GraphWin("Visualisation",400,400)

ball = Circle(Point(100,100),50)
ball.setFill(color_rgb(41,100,196))
ball.draw(window)

window.getMouse()

