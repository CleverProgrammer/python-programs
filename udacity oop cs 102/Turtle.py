import turtle
def main():
    window = turtle.Screen()
    window.bgcolor("red")

    #qazi_triangle()
    #angie_circle()
    brad_square()   

    window.exitonclick()

def brad_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("Yellow")
    brad.speed(5)
    for i in range (1,37):
        for i in range (1,5):
            brad.forward(150)
            brad.right(90)
        brad.right(10)

def angie_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("pink")
    angie.circle(50)

def qazi_triangle():
    qazi = turtle.Turtle()
    qazi.shape("arrow")
    qazi.color("green")
    qazi.right(45)
    qazi.forward(70)
    qazi.right(135)
    qazi.forward(100)
    qazi.right(135)
    qazi.forward(70)
    qazi.right(135)
    
main()
