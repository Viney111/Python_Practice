'''
        @Author: Viney Khaneja
        @Date: 2022-04-11 05:10PM
        @Last Modified by: Viney Khaneja
        @Last Modified time: None
        @Title : Permutation of Strings using Iterative & recursive method
    '''
import math
input_word = input("Enter the word, for which permutated strings to be calculated: ")

def permutation_recursive(word,l,r):

    permutated_words_list_recursive = []
    if l == r:
        permutated_words_list_recursive.append(word)
    else:
        i = l
        while i <= r:
            word = list(word)
            word[i],word[l] = word[l],word[i]
            word = "".join(word)
            permutation_recursive(str(word),l+1,r)
            word = list(word)
            word[i], word[l] = word[l], word[i]
            word = "".join(word)
    return permutated_words_list_recursive

def swapping(word,a,b):
    '''
                Description: Swapping the word with indexes passed as arguments
                Parameter: Takes the string and two integers for swapping
                Return: Return swapped word
            '''
    temp = word[a]
    word[a] = word[b]
    word[b] = temp
    return word

def calculate_factorial(word):
    '''
            Description: Calculating the factorial of the passed number
            Parameter: Takes a number as argument of which factorial we have to calculate
            Return: Factorial of number
        '''
    #Initializing fact variable by value 1
    fact = 1
    for i in range (1,len(word)+1):
        fact = fact * i
    return fact

def permutation_iterative(word):
    '''
            Description: Finding Permutation of the words passed as argument & storing in list
            Parameter: The word of which permutated string to be made
            Return: A list of Permutation of word
        '''
    permutated_words_list_iterative = []
    length_of_word = len(word)
    factorial_of_word = calculate_factorial(word)
    for i in range (0,factorial_of_word):
        tempered_word = word
        temp = i
        j = length_of_word
        permutated_word = ""
        for j in range(length_of_word,0,-1):
            quotient = int(temp / j)
            remainder = int(temp % j)
            permutated_word += tempered_word[remainder]
            tempered_word = tempered_word.replace(tempered_word[remainder],"",1)
            temp = quotient
        permutated_words_list_iterative.append(permutated_word)
    return permutated_words_list_iterative

print(permutation_iterative(input_word))
print(permutation_recursive(input_word,0,len(input_word)-1))