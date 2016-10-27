import turtle

def goCorner(turtle,lengthUnit,ifRight,ifBack):
    if ifRight:
        angle = 60
    else:
        angle = 120

    turtle.rt(angle)
    
    if ifBack:
        turtle.bk(lengthUnit)
    else:
        turtle.fd(lengthUnit)
    
    turtle.lt(angle)

def drawTriangleLevel(turtle,lengthUnit,level):
    
    if level == 0:
        turtle.begin_fill()
        for i in range(3):
            turtle.rt(60)
            turtle.fd(lengthUnit)
            turtle.rt(60)
        turtle.end_fill()
        
    else:
        runningDistance = lengthUnit*2**(level-1)
        
        # draw the upper triangle
        drawTriangleLevel(turtle,lengthUnit,level-1)

        # draw right triangle
        goCorner(turtle, runningDistance,True,False)
        drawTriangleLevel(turtle,lengthUnit,level-1)
        goCorner(turtle, runningDistance,True,True)

        # draw left triangle
        goCorner(turtle, runningDistance,False,False)
        drawTriangleLevel(turtle,lengthUnit,level-1)
        goCorner(turtle, runningDistance,False,True)


def draw(lengthUnit, level):
    window = turtle.Screen()
    window.bgcolor('green')

    brad = turtle.Turtle()
    brad.color('yellow')
    brad.shape('turtle')
    brad.speed('fastest')

    # draw the upper triangle
    drawTriangleLevel(brad,lengthUnit,level)

    window.exitonclick()

draw(10,5)
