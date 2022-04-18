'''
        @Author: Viney Khaneja
        @Date: 2022-04-11 03:54PM
        @Last Modified by: Viney Khaneja
        @Last Modified time: None
        @Title : Calculating Distance between the mentioned point to origin
    '''

import math
#Taking Inputs from User for X and Y co-ordinates
x1 = int(input("Enter the first X Co-ordinate: "))
y1 = int(input("Enter the first Y Co-ordinate: "))
x2 = int(input("Enter the second X Co-ordinate: "))
y2 = int(input("Enter the second Y Co-ordinate: "))

#Calculating Distance between two mentioned points
distance = math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
print(f"Distance between two points is: {distance}")