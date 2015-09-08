# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

paddle1_pos = [[0, 150],[0, 250]]
paddle1_vel = [0, 0]
paddle1_acc = -10

paddle2_pos = [[599, 150],[599, 250]]
paddle2_vel = [0, 0]
paddle2_acc = -10

score1 = 0
score2 = 0

sound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')
BASE_DIR = "http://commondatastorage.googleapis.com/codeskulptor-demos/pyman_assets/"
chompsound = simplegui.load_sound(BASE_DIR+"eatpellet.ogg")
chomp_volume = 0
chompsound.set_volume(chomp_volume)

ediblesound = simplegui.load_sound(BASE_DIR+"eatedible.ogg")


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #ball_vel = [4,4]
    if direction == LEFT:
        ball_vel = [random.randrange(4, 6), random.randrange(2, 4)]
        print 'LEFT', ball_vel
    elif direction == RIGHT:
        ball_vel = [-random.randrange(4, 6), -random.randrange(2, 4)]
        print 'RIGHT', ball_vel

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    if random.randrange(0,2) == 0:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)
    
    paddle1_pos = [[0, 150],[0, 250]]
    paddle1_vel = [0, 0]

    paddle2_pos = [[599, 150],[599, 250]]
    paddle2_vel = [0, 0]
    
    score1 = 0
    score2 = 0

    #spawn_ball()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, chompsound, chomp_volume
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    #canvas.draw_circle(center point, radius, line_width, line_color, color_fill)
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'red', 'white')
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos[0][1] + paddle1_vel[1] > -8) and (paddle1_pos[1][1] + paddle1_vel[1] < 408):
        paddle1_pos[0][1] += paddle1_vel[1]
        paddle1_pos[1][1] += paddle1_vel[1]
        
    if (paddle2_pos[0][1] + paddle2_vel[1] > -8) and (paddle2_pos[1][1] + paddle2_vel[1] < 408):
        paddle2_pos[0][1] += paddle2_vel[1]
        paddle2_pos[1][1] += paddle2_vel[1]
    
    # draw paddles
    canvas.draw_polyline(paddle1_pos, PAD_WIDTH, 'Red')
    canvas.draw_polyline(paddle2_pos, PAD_WIDTH, 'Red')
    
    # determine whether paddle and ball collide 
    # hit left paddle
    if (ball_pos[0] <= BALL_RADIUS + (HALF_PAD_WIDTH)) and ((ball_pos[1] < paddle1_pos[1][1]) and (ball_pos[1] > paddle1_pos[0][1])):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1 # 10% increase in speed after each hit
        ball_vel[1] *= 1.1
        if chomp_volume < 0.99:
            chomp_volume += 0.1
            chompsound.set_volume(chomp_volume)
        chompsound.play()
        
    # hit right paddle
    elif (ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - HALF_PAD_WIDTH) and ((ball_pos[1] < paddle2_pos[1][1]) and (ball_pos[1] > paddle2_pos[0][1])):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1 # 10% increase in speed after each hit
        ball_vel[1] *= 1.1
        if chomp_volume < 0.99:
            chomp_volume += 0.1
            chompsound.set_volume(chomp_volume)
        chompsound.play()
        
        
    # left gutter
    elif ball_pos[0] < BALL_RADIUS + (HALF_PAD_WIDTH) :
        score2 += 1
        chomp_volume = 0
        ediblesound.play()
        spawn_ball(LEFT)
        
    # right gutter 
    elif ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS:
        score1 += 1
        chomp_volume = 0
        ediblesound.play()
        spawn_ball(RIGHT)
    
    elif ball_pos[1] >= (HEIGHT - 1 ) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
         
    # draw scores
    
    canvas.draw_text(str(score1), [200, HEIGHT / 6], 60, 'white')
    canvas.draw_text(str(score2), [369, HEIGHT / 6], 60, 'white')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_acc, paddle2_acc
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] += paddle1_acc
    
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] -= paddle1_acc
        
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel[1] += paddle2_acc
        
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel[1] -= paddle2_acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_acc, paddle2_acc
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] -= paddle1_acc
        
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] += paddle1_acc
    
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel[1] -= paddle2_acc
        
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel[1] += paddle2_acc


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('New Game', new_game, 100)

# start frame
new_game()
frame.start()
