import turtle

def draw_square(turtle):
    #brad = turtle.Turtle()
    turtle.color('yellow')
    turtle.shape('turtle')
    turtle.speed('fast')

    #draw square pieces
    for i in range(2):
        turtle.fd(100)
        turtle.rt(45)
        turtle.fd(100)
        turtle.rt(135)


def draw_flower(flowernumber):
    window = turtle.Screen()
    window.bgcolor('green')

    brad = turtle.Turtle()
    brad.speed(0)

    for i in range(flowernumber):
        draw_square(brad)
        brad.rt(360/flowernumber)

    window.exitonclick()

    
draw_flower(36)
