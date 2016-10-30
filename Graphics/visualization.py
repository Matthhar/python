from graphics import *
from time import *
from random import randint

data = [52, 47, 57, 49, 59, 62, 44, 76, 52, 52, 44, 59, 59, 79, 59, 42, 57, 48, 80, 43, 72, 74, 59, 44, 57, 55, 49, 54, 54]
#list of data values to be used


window = GraphWin("Visualisation",500,500)

y = 100
x = 200
yspeed = 10
xspeed = 10
r = 40
g = 200
b = 120
colourchange = 1
ball = Circle(Point(y,x),50)
ball.setFill(color_rgb(r,g,b))
ball.setOutline(color_rgb(r,g,b))
ball.draw(window)

# This code sets the initial values for variables and creates the ball and window to be drawn


while True:
    
       
    ball.move(yspeed,xspeed)
    ball.setFill(color_rgb(r,g,b))
    ball.setOutline(color_rgb(r,g,b))
    sleep(0.2)
    y = y + yspeed
    x = x + xspeed
    
    #Code above moves the ball and updates its colour values
    
    
    if y == 450:
        yspeed = -10
    if y == 50:
        yspeed = 10
    if x == 450:
        xspeed = -10
    if x == 50:
        xspeed = 10
        
    #A series of if statements is used to get the ball to bounce off the edge of the window
    
    
    for change in data: 
        if colourchange == 1:
            r = r + (change*randint(0,1))
            if r > 255: 
                r = 1
            colourchange = colourchange + 1
        if colourchange == 2:
            g = g + (change*randint(0,1))
            if g > 255: 
                g = 1
            colourchange = colourchange + 1
        if colourchange == 3:
            b = b + (change*randint(0,1))
            if b > 255: 
                b = 1
            colourchange = 1
 
    # A for loop and some more if statements are used to randomise the RGB values of the ball using the data values
    
    
    
window.getMouse()

