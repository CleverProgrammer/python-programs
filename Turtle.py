import turtle
def main():
    window = turtle.Screen()
    window.bgcolor("Black")

    #qazi_triangle()
  #  angie_circle()
    turtle_on_steroids()   
 
    window.exitonclick()

def turtle_on_steroids():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("Yellow")
    brad.speed(1000)
    for i in range (1,360):
        for i in range (1,5):
            brad.forward(180)
            brad.right(90)
        brad.right(11)

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
