#!usr/bin/env python3

import random

def guess_function():
    r_2 = int(input("Enter the highest desired range to guess from, from 1 to "))
    tries = int(input("How many tries do you want?\n"))
    n=0
    r_n = random.randint(1, r_2)
    while (tries > 0):
        tries = tries - 1
        if n != r_n:
            n= int(input("Whats your guess?\n"))
            if n < r_n:
                print("Higher")
            elif n > r_n:
                print("Lower")
            elif n == r_n:
                print("Thats Correct! You had ", tries, " tries left.")
        else:
            pass
    if (n != r_n):
        print("The number was ", r_n, ", you failed.", sep="")
    pass


guess_function()
print("end")
replay_q = int(input("Do you wish to play again (1), move to the next level (2), \n see leaderboard (3), or quit (4)\n"))
if replay_q == 1:
    guess_function()
else:
    print("Goodbye")