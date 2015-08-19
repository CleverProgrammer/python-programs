from random import randint

human_shipRow = int(raw_input("Pick Ship 1 Row:"))
human_shipCol = int(raw_input("Pick Ship 1 Col:"))
    

for turn in range(4):
    board = []
    
    for x in range(5):
        board.append(["O"] * 5)
    
    def print_board(board):
        for row in board:
            print " ".join(row)
    
    print "Let's play Battleship!"
    print_board(board)
    
   # def random_row(board):
       # return randint(0, len(board) - 1)
    
    # def random_col(board):
       # return randint(0, len(board[0]) - 1)
    
    
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == human_shipRow and guess_col == human_shipCol:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        if turn >= 3:
            print "Game Over"
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print "Turn", turn + 1
        print_board(board)
