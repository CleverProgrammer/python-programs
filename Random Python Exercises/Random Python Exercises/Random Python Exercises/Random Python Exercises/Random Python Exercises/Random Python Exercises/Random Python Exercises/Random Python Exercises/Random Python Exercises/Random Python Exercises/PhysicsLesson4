#Physics Lesson 4 on Projectiles
from visual import *

scene.width = 800
scene.height = 600

scene.autoscale = 0
scene.range = (100,100,100)
scene.center = (50,40,0)

Radius = 2
initial_position = 2
ball = sphere(pos=(0,initial_position,0),radius=Radius, color = color.green)
ground = box(pos=(50,-1,0),size=(100,2,100))
#building = box(size=(5,100,5),pos=(0,50,0),color=color.blue)

gravity = 9.8  # m/s**2
velocity = 25   # m/s
angle = 45     # degrees
angle = angle * (pi/180) # converted to radians

# sin = opp / hyp
# cos = adj / hyp

# therefore

# opp = sin * hyp --> Y direction velocity 
# adj = cos * hyp --> X direction velocity

VelocityY = velocity * sin(angle)
VelocityX = velocity * cos(angle)

seconds = 0
dt = 0.01

finished = False

while not finished:
    rate(100) #100 times in a second, don't go to fast COMPUTER! haha
    seconds += dt

    # position equation: y(t) = y0 + v0*t + .5* a * t**2
    # direction with respect to time hence y(t)
    # initial position plus velocity in y direction times TIME +
    # 1/2 acceleration times TIME^2

    ballY = initial_position + VelocityY * seconds - .5 * gravity * seconds**2
    #y direction

    ballX = VelocityX * seconds
    #not accelerating in x direction 

    ball.pos = vector(ballX,ballY,0)

    if ballY - Radius <= 0:
        finished = True
        print "initial velocity: " + str(velocity)
        print "angle throw: " + str(angle)
        print "seconds in flight: " + str(seconds)
        print "Distance in the X direction: " + str(ballX)
        


    
