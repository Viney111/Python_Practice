"""
    @Author: Viney Khaneja
    @Date: 2022-04-11 08:54AM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Getting Head Tail Percentage
"""

yearToBeChecked = int(input("Enter the year, you want to check: "))
def check_Leap_Year(year):
    '''
    Description: Function to check for leap year
    Parameter: Year to  be checked for leap year
    Return: Nothing
    '''
    if (year % 4==0) and (year % 100!=0):
        print(f"{year} is a leap year")
    elif (year % 400 ==0) and (year % 100 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

if (1000<= yearToBeChecked <= 9999):
    check_Leap_Year(yearToBeChecked)
else:
    print("Enter 4 digit Year")