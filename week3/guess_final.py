#!usr/bin/env python3

#Importing modules:
from ast import For
import random
import colorama 
from colorama import Fore

#Normalizing numbers:
menu = 0
select_level = 0
lvl1score = "Beat level 1 for score"
lvl2score = "Beat level 2 for score"
lvl3score = "Beat level 3 for score"

#Making Functions
def guess_function1():
    r_2 = int(input(Fore.WHITE + "Enter the highest desired range to guess from, from 1 to \n" + Fore.CYAN))
    tries = int(input(Fore.WHITE + "How many tries do you want?\n" + Fore.CYAN))
    n=0
    r_n = random.randint(1, r_2)
    while (tries > 0):
        tries = tries - 1
        if n != r_n:
            n= int(input(Fore.RED + "Whats your guess?\n" + Fore.CYAN))
            if n < r_n:
                print(Fore.RED + "The number is Higher" + Fore.CYAN)
            elif n > r_n:
                print(Fore.RED + "The number is Lower" + Fore.CYAN)
            elif n == r_n:
                print(Fore.GREEN + "Thats Correct! You had ", tries, " tries left.\n" + Fore.WHITE)
                global lvl4score
                lvl4score = tries

        else:
            pass
    if (n != r_n):
        print("The number was ", r_n, ", you failed.", sep="")
    pass
def guess_level_1():
    print(Fore.WHITE + "\nIn this level you will need to guess a number between 1 and 10 within 4 tries. \nIf you play this right you should be able to succeed 100% of the time.\n" + Fore.CYAN)
    r_2 = 10
    tries = 4
    n=0
    r_n = random.randint(1, r_2)
    while (tries > 0):
        tries = tries - 1
        if n != r_n:
            n= int(input(Fore.RED + "Whats your guess?\n" + Fore.CYAN))
            if n < r_n:
                print(Fore.RED + "The number is Higher" + Fore.CYAN)
            elif n > r_n:
                print(Fore.RED + "The number is Lower" + Fore.CYAN)
            elif n == r_n:
                print(Fore.GREEN + "Thats Correct! You had ", tries, " tries left.\n" + Fore.WHITE)
                global lvl1score
                lvl1score = tries

        else:
            pass
    if (n != r_n):
        print("The number was ", r_n, ", you failed.", sep="")
    pass
def guess_level_2():
    print(Fore.WHITE + "\nIn this level you will need to guess a number between 1 and 100 within 8 tries. \nIf you play this right you should be able to succeed 100% of the time.\n" + Fore.CYAN)
    r_2 = 100
    tries = 8
    n=0
    r_n = random.randint(1, r_2)
    while (tries > 0):
        tries = tries - 1
        if n != r_n:
            n= int(input(Fore.RED + "Whats your guess?\n" + Fore.CYAN))
            if n < r_n:
                print(Fore.RED + "The number is Higher" + Fore.CYAN)
            elif n > r_n:
                print(Fore.RED + "The number is Lower" + Fore.CYAN)
            elif n == r_n:
                print(Fore.GREEN + "Thats Correct! You had ", tries, " tries left.\n" + Fore.WHITE)
                global lvl2score
                lvl2score = tries

        else:
            pass
    if (n != r_n):
        print("The number was ", r_n, ", you failed.", sep="")
    pass
def guess_level_3():
    print(Fore.WHITE + "\nIn this level you will need to guess a number between 1 and 1000 within 18 tries. \nIf you play this right you should be able to succeed, but I didn't test it.\n" + Fore.CYAN)
    r_2 = 1000
    tries = 18
    n=0
    r_n = random.randint(1, r_2)
    while (tries > 0):
        tries = tries - 1
        if n != r_n:
            n= int(input(Fore.RED + "Whats your guess?\n" + Fore.CYAN))
            if n < r_n:
                print(Fore.RED + "The number is Higher" + Fore.CYAN)
            elif n > r_n:
                print(Fore.RED + "The number is Lower" + Fore.CYAN)
            elif n == r_n:
                print(Fore.GREEN + "Thats Correct! You had ", tries, " tries left.\n" + Fore.WHITE)
                global lvl3score
                lvl3score = tries

        else:
            pass
    if (n != r_n):
        print("The number was ", r_n, ", you failed.", sep="")
    pass
def scores():
    print ("Here you will be able to see your best scores")
    print(Fore.BLUE + "\n", lvl1score, sep="") 
    print(lvl2score)
    print(lvl3score)
    print("")
#Game menu:
print("\nWelcome\n")
while (menu !=4):
    menu = int(input(Fore.MAGENTA + "\nDo you wish to open the level menu (1) \nsee your results (2), play sandbox (3), or quit (4)\n" + Fore.CYAN))
    if menu == 3:
        guess_function1()
    elif menu == 1:
        select_level = int(input(Fore.MAGENTA + "Select a level 1-3, or press (4) to come back\n" + Fore.CYAN))
        if (select_level == 1):
            guess_level_1()
        elif (select_level ==2):
            guess_level_2()
        elif (select_level ==3):
            guess_level_3()
        else:
            pass
    elif menu == 2:
        scores()
    else:
        print(Fore.MAGENTA + "Goodbye" +Fore.WHITE)