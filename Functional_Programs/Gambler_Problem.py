"""
        @Author: Viney Khaneja
        @Date: 2022-04-10 11:40AM
        @Last Modified by: Viney Khaneja
        @Last Modified time: None
        @Title : Printing Nth Harmonic Number
        """

import random
# CONSTANTS
WIN_NUMBER = 1
BET_MONEY = 1

# User Inputs
starting_stake = int(input("Enter the starting stake of Gambler: "))
goal_money = int(input("Enter the goal money of Gambler: "))
games_played = int(input("Enter the number of times, Gambler wants to play: "))


def gambling():
    """
    Description: Checks if the gambler loses or wins
    Parameter:None
    Return:win_flag: If Gambler wins, it returns win_flag = 1 & if loses, it returns win_flag = 0
    """
    initial_stake = starting_stake
    win_flag = 0
    while (initial_stake > 0) and (initial_stake <= goal_money):
        bet = random.randint(0,1)
        if bet == WIN_NUMBER:
            initial_stake += BET_MONEY
        else:
            initial_stake -= BET_MONEY
    if initial_stake >= goal_money:
        win_flag = 1
    else:
        win_flag = 0
    return win_flag

# Initializing variables for counting win & losses with zero
win_count = lose_count = 0
for i in range(1, games_played+1):
    result = gambling()
    if result == 1:
        win_count += 1
    else:
        lose_count += 1

print(f"Gambler wins {win_count} times & percentage of win & loss are {(win_count/games_played)*100} and {(lose_count/games_played)*100} respectively.")