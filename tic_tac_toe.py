#from IPython.display import clear_output
def display_board(board):
    #clear_output()
    print('\n'*100)
    print(board[7] +' | '+ board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] +' | '+ board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] +' | '+ board[2] + ' | ' + board[3])

def player_input():
    
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 , do you want to be X or O: ').upper()
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    marker = (player1,player2)
    return marker

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else: return 'Player 2'

def space_check(board, position):
    
    return board[position] == " "

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):

    position = '0'
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input('Choose a position (1-9): ')
    if space_check(board,int(position)) :
            return  int(position)

def gameon_choice():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        choice = input('Would you like to keep playing ? Y or N ')
        
        if choice not in ["Y","N"]:
            print("Invalid input! Please choose Y or N")
    if choice == 'Y':
        return True
    else:
        return False
    

game_on_choice = True
while game_on_choice:
    # Play the game
    
    ##  SET EVERYTHING UP (BOARD, WHO'S FIRST, MARKERS X & O )
    the_board = [' ']*10
    display_board(the_board)
    print('Welcome to TIC TAC TOE\n')
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? Enter y or n?')
    
    if play_game == 'y':
        game_on =True
    else:
        game_on = False   
    
    ## GAME PLAY
    
    while game_on:
        
    
    ### PLAYER ONE TURN
        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player1_marker,position)
           
            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 HAS WON !')
                game_on = False
                
            # or check if there's a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME !')
                    break
             # no tie and no win? Then next player's turn       
                else:
                    turn = 'Player 2'
    
    ### PLAYER TWO TURN
        else:
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 HAS WON !')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME !')
                    break
                else:
                    turn = 'Player 1'
    
    # BREAK OUT OF THE WHILE LOOP ON replay()
    if not gameon_choice():
        break