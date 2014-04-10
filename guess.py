
# template for "Guess the number" mini-project

import simplegui
import random

global rand
global count
count=7

# helper function to start and restart the game
def new_game():
    global rand
    global count
    count=7
    print "New game.Range is from 0 to 100"
    print "Number of remaining guesses is",count
    print 
    rand=random.randrange(0,100)
    
 #buttons and textfield
def range100():
    global count
    count=7
    new_game()
   
def range1000():
    global rand
    global count
    rand=random.randrange(0, 1000)
    count=7
    print "New game.Range is from 0 to 1000"
    print "Number of remaining guesses is",count
    print 
   
def input_guess(guess):
    
    global rand
    global count 
    count-=1
    print "Guess was ",guess
    print "Number of remaining guesses is",count
    
    if rand==int(guess):
        print "Correct"
    elif rand<int(guess):
        print "Lower!"
    elif rand>int(guess):
        print "Higher!"
    if count==0:
        print "Number of guesses finished"
        print 
        new_game()
    print 
    
#create frame
f=simplegui.create_frame("Guess Game",200,200)


# register event handlers for control elements
f.add_button("Range is[0,100)",range100,200)
f.add_button("Range is[0,1000)",range1000,200)
f.add_input("Enter a guess",input_guess,200)

# call new_game and start frame

f.start()
new_game()

