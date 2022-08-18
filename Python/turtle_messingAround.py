import turtle


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_ellipse(some_turtle):
    for i in range(1,100):
        some_turtle.forward(1)
        some_turtle.right(1)

def main():
    window = turtle.Screen()
    myTurtle = turtle.Turtle()
    # draw_square(turtle1)
    draw_ellipse(myTurtle)
    window.exitonclick()

if __name__ == '__main__':
    main()