board = ["-", "-", "-",
         "-", "-", "-",         #the default board
         "-", "-", "-",]

#initializing variables for winner, whether to continue game and the current player
winner = None               #winner set to no one
game_still_going = True     #continue playing
current_player = "X"        #first player starts off with X

def display_board():        #function to display the created default board, each - separated by a |
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn(player):        #function for the main game part, which'll take a parameter to hold the current player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: \n")      #only positions 1-9 are legal
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:    #loops continuosly until a value which is legal, in the list is entered
            position = input("Choose a position from 1-9: \n")
        position = int(position)-1          #entered position is subtracted as indexing is from 0-8
        if board[position] == "-":
            valid = True                    #this continuous loop is broken is all the conditions are satisfied
        else:                               #prevents entering into an already used up space
            print("YOU CANNOT DO THAT -_-")
    board[position] = player                #updates the board by overwritting the - with either an X or O
    display_board()


def check_rows():                           #this function is used to check whether there are rows with 3X's or O's in a row
    global game_still_going                 #in order to change a global variable access must be granted
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"                 #if the values of each space in a row is equal the game is stopped, (but it should not be equal to the - as thats the default board)
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False            #the above values are truthy, and if satisfied game is stopped
    if row_1:
        return board[0]                     #this statement is basically to return the X/O
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():                        #same procedure done for columns and diagonals
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return


def check_for_winner():
    global winner
    row_winner = check_rows()           #setting variables to hold the values of the above defined functions
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner             #updating the global winner variable
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_if_tie():
    global game_still_going           #if all spaces are taken up the game is stopped as a tie
    if "-" not in board:
        game_still_going = False
    return


def check_if_game_over():
    check_for_winner()               #game is over once a person wins or a tie
    check_if_tie()


def flip_player():
    global current_player           #function to switch the players after each turn by accessing the current_player global variable and changing it to O or X
    if current_player=="X":
        current_player = "O"
    elif current_player =="O":
        current_player = "X"
    return


def play_game():        #main function
    display_board()                 #display the board
    while game_still_going:         #truthy value either T/F
        handle_turn(current_player) #handle_turn function is called each time with the current_player global variable as an argument
        check_if_game_over()        #checks after each turn whether the game is over
        flip_player()               #if game isn't over the next player is given a chance

    if winner=="X" or winner=="O":
        print(winner + " won.")    #checking the value of the global winner variable for it's value and displaying the winner
    elif winner==None:
        print("Tie.")


play_game()