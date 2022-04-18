"""
    @Author: Viney Khaneja
    @Date: 2022-04-12 12:10PM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : TicTacToe Game
"""
# Importing Random & Time
import random
import time
import os
# Mentioning Symbols for players
computer_symbol = "X"
manual_player_symbol = "O"


def clear(): return os.system('cls')


def tictactoe_game():
    """
            Description: Function to play tictactoe game & finding out if the game has any winner or is tied.
            Parameters: None
            Returns: Prints the winner if there is any result otherwise display a tie message
        """
    # Initializing a blank board with space
    board = [" " for x in range(0, 10)]
    board[0] = "A"
    # Variable to swap the turn between players
    player_turn = 0

    while True:
        # Getting Player Symbol & player input
        game_symbol, game_input = player_symbol(player_turn)
        if board[game_input] != computer_symbol and board[game_input] != manual_player_symbol:
            board[game_input] = game_symbol
            player_turn += 1
        else:
            print("Position is already occupied.")
            # For sleeping the screen.
            time.sleep(2.5)

        clear()
        print("Welcome to TicTacToe Game in Python\nComputer Symbol: \"X\"\nUser Symbol: \"O\" ")
        # Displaying the board
        display_board(board)
        # Checking the winning condition after every turn
        win_flag = winning_conditions(board)
        if win_flag != 1 and win_flag != -1:
            continue
        else:
            break
    # Printing the outcome of the game
    if win_flag == 1:
        if player_turn == 1:
            print("Bad Luck ! Computer wins")
        else:
            print("Congrats ! User Wins")
    else:
        print("Match tied")


def player_symbol(turn):
    """
                Description: Function to return Player Symbol & Player Input position
                Parameters: Turn Integer
                Returns: Returns Player symbol & Player Input Value
            """
    if turn % 2 == 0:
        computer_input = random.randint(1, 9)
        return computer_symbol, computer_input
    else:
        manual_input = int(input("Enter the position mannually: "))
        return manual_player_symbol, manual_input


def display_board(board):
    """
           Description: Function to display the board of game on console
           Parameters: None
           Returns: None, Prints the board of game on console
       """
    print("-------------")
    print("|", board[1],  "|", board[2], "|", board[3], "|")
    print("-------------")
    print("|", board[4],  "|", board[5], "|", board[6], "|")
    print("-------------")
    print("|", board[7],  "|", board[8], "|", board[9], "|")
    print("-------------")


def winning_conditions(board):
    """
            Description: Function to check if any of the player wins or not
            Parameters: Board List
            Returns: An integer (0,1,-1) i.e. 1 for winning, 0 for continue playing, -1 for tie
        """
    # For checking horizontal winning
    if board[1] == board[2] == board[3] != " ":
        return 1
    elif board[4] == board[5] == board[6] != " ":
        return 1
    elif board[7] == board[8] == board[9] != " ":
        return 1
    # For checking vertical winning
    elif board[1] == board[4] == board[7] != " ":
        return 1
    elif board[2] == board[5] == board[8] != " ":
        return 1
    elif board[3] == board[6] == board[9] != " ":
        return 1
    # For checking diagonal winning
    elif board[1] == board[5] == board[9] != " ":
        return 1
    elif board[3] == board[5] == board[7] != " ":
        return 1
    # For tie condition
    elif " " not in board:
        return -1
    # For not filling all the space available on board
    else:
        return 0


if __name__ == '__main__':
    tictactoe_game()
