from curses.panel import update_panels
import random
import string
print("Password Generator")
#Normalizing values
length = 0
qlower = 0
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#function
while (length <4) or (length > 300):
    length= int(input("Enter Password Length (4-300): \n"))
print("Now Choose the complexity of your password: \n")
while (qlower != "y") or (qlower != "n"):
    qlower = input("Do you want to use lower case letters? (y/n)\n")
    if (qlower == "y"):
        all = all + lower
        print("Lowercase letters will be included")
    elif (qlower =="n"):
        print("Lowercase will be omitted")
    else:
        print('Choose either "y" or "n"')
all = lower + upper+num+symbols

randomize = random.sample(all,length)
password = "".join(randomize)

print(password)








#Base of the code taken from https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9 