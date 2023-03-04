# The Collatz Conjecture is one of the most famous unsolved problems in mathematics. It is named after
# Lothar Collatz who introduced the conjecture in 1937.
#  
# Collatz defined a function as follows: Given a positive integer, if the integer is even, divide it by 2;
# if the integer is odd, mutilpy it by 3 and add 1. Iterating this function results in a sequence of
# positive integers. For example, if n = 40, the sequence would be (40, 20, 10, 5, 16, 8, 4, 2, 1). 
# Collatz conjectured that the sequence would always end in 1.
#
# Below is a function that verfies the Collatz Conjecture for any integer n.
# I include a list of the integers the function outputs.

def collatz_checker(n):
    list_of_collatz_outputs = [n, ]
    while n >= 1:
        if n == 1:
            break
        elif n%2 == 0:
            n = n//2
            list_of_collatz_outputs.append(n)
        else:
            n = 3*n + 1
            list_of_collatz_outputs.append(n)
    if list_of_collatz_outputs[-1] == 1:
        print("It works!")
    print(list_of_collatz_outputs)

collatz_checker(100)
# This outputs
# It works!
# [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

