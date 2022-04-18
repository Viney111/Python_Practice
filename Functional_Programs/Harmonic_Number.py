'''
@Author: Viney Khaneja
@Date: 2022-04-11 11:10AM
@Last Modified by: Viney Khaneja
@Last Modified time: None
@Title : Printing Nth Harmonic Number
'''
# User Input
N = int(input("Enter a number for printing harmonic'th value: "))
harmonic_Result = 0
if(N>0):
    for i in range (1,N+1):
        harmonic_Result += 1/i
    print(f"Harmonic value is {harmonic_Result} ")
else:
    print("Number value should not equal to zero")

import random
# num = int(input("Enter the no of rows u want: "))
# num_for_bool
# for i in range(1,num+1):
#     print("*"* i)