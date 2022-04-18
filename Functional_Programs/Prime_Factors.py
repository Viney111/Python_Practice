'''
@Author: Viney Khaneja
@Date: 2022-04-11 09:10AM
@Last Modified by: Viney Khaneja
@Last Modified time: None
@Title : Finding Prime Factors
'''

#Importing math library to calculate square root
import math

number = int(input("Enter the number, u want prime factors of: "))
def prime_factors(num):
    '''
    Description: Finding prime Factors of the number
    Parameter: Number for which prime factors to be find
    Return: A list of Prime Factors
    '''
    prime_Factors_List = []
    for i in range(2,num+1):
        if num % i == 0:
            flag = 0
            for j in range(2,int(math.sqrt(i))+1):
                if i % j == 0:
                    flag = 1
            if flag == 0 :
                prime_Factors_List.append(i)
    return prime_Factors_List

print(prime_factors(number))
print(prime_factors.__doc__)