from curses.panel import update_panels
import random
import string
print("Password Generator")

length= int(input("Enter Password Length: \n"))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper+num+symbols

randomize = random.sample(all,length)
password = "".join(randomize)

print(password)