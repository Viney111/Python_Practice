'''
@Author: Viney Khaneja
@Date: 2022-04-11 09:10AM
@Last Modified by: Viney Khaneja
@Last Modified time: None
@Title : Printing power of 2
'''

#User Input
N = int(input("Enter a number to get power of 2: "))
#Number should be less than 31.
if(0<N<31):
    for i in range(1,N+1):
        print("2 ^",i,"=",2**i)
else:
    print("Enter number below 31")

