'''
        @Author: Viney Khaneja
        @Date: 2022-04-11 08:54AM
        @Last Modified by: Viney Khaneja
        @Last Modified time: None
        @Title : Random Numbers needed to match distict Coupon Numbers
    '''

import random

def randon_number_generator(range):
    '''
        Description: Create a random number within the range.
        Parameter: Range to get random number in that range only
        Return: random_num i.e. a 2 digit random number
    '''
    random_num = random.randint(0,range)
    return random_num

def calculating_random_counts():
    '''
        Description: Taking Inputs from user for distinct coupons and
                    Counting random counts to match distinct coupon numbers
        Parameter: none
        Return: None, Prints the random counts
    '''
    # Initializing empty list
    distict_coupon_numbers_list = []

    # User Inputs
    coupons_count = int(input("Enter the count of distinct coupon numbers u want to add: "))
    coupon_number_digits_range = int(input("Enter the max range of the the digits coupon numbers: "))

    for i in range(0,coupons_count):
        distict_coupon_number = int(input("Enter the distinct coupon number: "))
        if distict_coupon_number not in distict_coupon_numbers_list and distict_coupon_number <= coupon_number_digits_range:
            distict_coupon_numbers_list.append(distict_coupon_number)
        else:
            print(
                "Enter distinct number as it is already present OR you have entered number that is out of range of coupon")
    #Variables
    random_count = j = 0
    while j < len(distict_coupon_numbers_list):
        if distict_coupon_numbers_list[j] == randon_number_generator(coupon_number_digits_range):
            j += 1
        else:
            random_count += 1
    print(f"Total random numbers needed to match distinct coupons: {random_count}.")

if __name__ == "__main__":
    calculating_random_counts()