from graphics import *
from time import *

data = [52, 47, 57, 49, 59, 62, 44, 76, 52, 52, 44, 59, 59, 79, 59, 42, 57, 48, 80, 43, 72, 74, 59, 44, 57, 55, 49, 54, 54]

window = GraphWin("Visualisation",500,500)

y = 100
x = 200
yspeed = 25
xspeed = 25
r = 45
g = 250
b = 165
colourchange = 1

while True:
    ball = Circle(Point(y,x),50)
    ball.setFill(color_rgb(r,g,b))
    y = y + yspeed
    x = x + xspeed
    ball.draw(window)
    sleep(0.1)
    ball.undraw()
    if y == 450:
        yspeed = -25
    if y == 50:
        yspeed = 25
    if x == 450:
        xspeed = -25
    if x == 50:
        xspeed = 25
    for change in data: 
        if colourchange == 1:
            r = r + change
            colourchange = colourchange + 1
        if colourchange == 2:
            g = g + change
            colourchange = colourchange + 1
        if colourchange == 3:
            b = b + change
            colourchange = 1
 
    
window.getMouse()

