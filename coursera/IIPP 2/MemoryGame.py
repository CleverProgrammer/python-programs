# implementation of card game - Memory

import simplegui
import random
RECTANGLES_16 = 800 // 16
FRAME_WIDTH = 800
FRAME_HEIGHT = 100


# helper function to initialize globals
def new_game():
    global deckOfCards, checkedCard, exposed, turns, count_clicks
    deckOfCards = range(8) * 2 #Value of the card
    random.shuffle(deckOfCards)
    checkedCard = [] #Index of the card
    exposed = [False] * 16 #Current state of the card (Faceup/facedown?)
    turns = 0
    count_clicks = 0
    
    #Deck of 16 shuffled cards with two cards for each number
    #List of exposed cards. (Cards that are clicked on)
    #Cards that are face up should be True in exposed list, face down should be False
    #checkedCard list should check the value of exposed[i] list and then
    #compare THAT ith index with the deckOfCards[i] list.
    #checkedCard should APPEND that card from deckOfCards[i] only if exposed[i] is False
    
    #if the state of the card from exposed[i] is already True, then checkedCard
        #should ignore that case
    
    #If the both values in checkedCard are not the same, then 
        #Both values should be popped off from checkedCard
    
    #if both values in checkedCard are the same, then those two numbers
        #should remain in checkedCard so they could be repeteadly drawn on the canvas
        #and they should also remain True in exposed list. And
        #should remain visible permanently and should be unchangeable in checkedCard and exposed
    
    #count_clicks
    #turns

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global count_clicks, turns
    current_card = pos[0] // 50
    
    if count_clicks == 0:
        if exposed[current_card] == False:
            checkedCard.append(current_card)
            exposed[current_card] = True
            count_clicks += 1
            turns += 1
        print 'checkedCard', checkedCard
        print 'exposed', exposed
        
    elif count_clicks == 1:
        if current_card not in checkedCard:
            checkedCard.append(current_card)
            count_clicks += 1
            turns += 1
        exposed[current_card] = True
        
        print 'checkedCard', checkedCard
        print 'exposed', exposed
        
    else:
        if deckOfCards[checkedCard[-1]] != deckOfCards[checkedCard[-2]]:
            exposed[checkedCard[-1]] = False
            exposed[checkedCard[-2]] = False
            checkedCard.pop() #pops the last one
            checkedCard.pop() #pops the second last one
        else:
            exposed[checkedCard[-1]] = True
            exposed[checkedCard[-2]] = True
        
        if exposed[current_card] == False:
            checkedCard.append(current_card)
            exposed[current_card] = True
            count_clicks = 1
            turns += 1
   

# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = " +str(turns))
    green = 'green'
    red = 'red'
        
    for i, j in zip(range (0, FRAME_WIDTH, RECTANGLES_16), range(len(deckOfCards))):
        green, red = red, green
        canvas.draw_line([i-1, 0], [i-1, FRAME_HEIGHT], 2, green )
        if exposed[j]:
            canvas.draw_text(str(deckOfCards[j]), [i+11,63], 50, 'White')
        
        
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
