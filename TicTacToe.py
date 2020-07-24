
import random
from IPython.display import clear_output
print("Welcome to Tic - Tac - Toe by Shashwat Vatsa")
def display_board(board):
    clear_output()
    print('', board[7], '|', board[8], '|', board[9])
    print('---|---|---')
    print('', board[4], '|', board[5], '|', board[6])
    print('---|---|---')
    print('', board[1], '|', board[2], '|', board[3])
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
        if not (marker == 'X' or marker == 'O'):
            print("Sorry, invalid input. Please try again.")
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
def place_marker(board, marker, position):
    board[position] = marker
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board [9] == mark) 
    or (board[4] == mark and board[5] == mark and board[6] == mark)
    or (board[1] == mark and board[2] == mark and board[3] == mark)
    or (board[1] == mark and board[3] == mark and board[7] == mark)
    or (board[2] == mark and board[5] == mark and board[8] == mark)
    or (board[3] == mark and board[6] == mark and board[9] == mark)
    or (board[3] == mark and board[5] == mark and board[7] == mark)    
    or (board[1] == mark and board[5] == mark and board[9] == mark))
def choose_first(a, b):
    return random.choice([a, b])
def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, pos):
        pos = int(input("Enter the next position (1 to 9) : "))
        if pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Sorry, invalid position. Please enter a number between 1 to 9.")
        if not space_check(board, pos):
            print("Sorry, you entered a non-empty position. Please enter any other position.")
    return pos
def replay():
    return input("Enter 'Yes' if you want to play again.").lower() == 'Yes'

while True:
        clear_output()
        
        Board = [' '] * 10
        player1 = str(input("Enter name of Player 1 : "))
        player2 = str(input("Enter name of Player 2 : "))
        player_one_marker, player_two_marker = player_input()
        turn = choose_first(player1, player2)
        print(turn, "will play first.")
        x = input("Press any button on the keyboard to continue.")
        
        while True:
            if turn == player1:
                display_board(Board)
                print(player1, ", it's time to play!")
                index = player_choice(Board)
                place_marker(Board, player_one_marker, index)
            
                if win_check(Board, player_one_marker):
                    display_board(Board)
                    print("Congratulations!", player1, "has won the game.")
                    break
                elif full_board_check(Board):
                    display_board(Board)
                    print("Game ended as a tie.")
                    break
                else:
                    turn = player2
                    
            else:
                display_board(Board)
                print(player2, ", it's time to play!")
                index = player_choice(Board)
                place_marker(Board, player_two_marker, index)
            
                if win_check(Board, player_two_marker):
                    display_board(Board)
                    print("Congratulations!", player2, "has won the game.")
                    break
                elif full_board_check(Board):
                    display_board(Board)
                    print("Game Tied.")
                    break
                else:
                    turn = player1
                    
        if not replay():
            break
