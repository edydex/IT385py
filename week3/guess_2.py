#!usr/bin/env python3

import random

def guess_function():
    r_2 = int(input("Enter the highest desired range to guess from, from 1 to "))
    tries = int(input("How many tries do you want?\n"))
    r_n = random.randint(1, r_2)
    n=0
    while (tries > 0):
        while (n != r_n):
            tries = tries - 1
            n= int(input("Whats your guess?\n"))
            if n < r_n:
                print("Higher")
            elif n > r_n:
                print("Lower")
            elif n == r_n:
                print("Thats Correct! You had ", tries, " tries left.")

guess_function()
