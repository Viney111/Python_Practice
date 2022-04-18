'''
@Author: Viney Khaneja
@Date: 2022-04-11 08:54AM
@Last Modified by: Viney Khaneja
@Last Modified time: None
@Title : Getting Head Tail Percentage
'''

#Importing Random Function
import random
#User Input
maxCountFlipCoins = int(input("Enter the number, you want to flip coin: "))
#Variables
countFlippCoins = countHeads = countTails = 0
if (0<maxCountFlipCoins):
    while(maxCountFlipCoins>countFlippCoins):
        flipResult = random.random()
        if flipResult<0.5:
            countTails += 1
        else:
            countHeads += 1
        countFlippCoins += 1
    print(
        f"Percentage of Heads is {(countHeads / maxCountFlipCoins) * 100} and Tails is {(countTails / maxCountFlipCoins) * 100}")
else:
    print("Flip Counts should be positive")
