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
#Function
while (length <4) or (length > 300):
    length= int(input("Enter Password Length (4-300): \n"))
print("Now Choose the complexity of your password: \n")

def write_file():
    pass_name = input("Write a name for your password: \n")
    f= open("passwordlist.txt","a") 
    f.write("\n\n")
    f.write(pass_name)
    f.write("\n")
    f.write(password)
    f.close()
def include_upper():
    qupper = input("Do you want to use upper case letters? (y/n)\n")
    global all
    if (qupper == "y"):
        all = lower+ upper
        print("Upper case letters will be included")
    elif (qupper =="n"):
        print("Upper case letters will be omitted")
        all = lower
    else:
        print('Choose either "y" or "n"')
        include_upper()
def include_num():
    qnum = input("Do you want to use numbers? (y/n)\n")
    global all
    if (qnum == "y"):
        all += num
        print("Numbers will be included")
    elif (qnum =="n"):
        print("Numbers will be omitted")
    else:
        print('Choose either "y" or "n"')
        include_num()
def include_symbols():
    qsymbols = input("Do you want to use symbols? (y/n)\n")
    global all
    if (qsymbols == "y"):
        all += symbols
        print("Symbols will be included")
    elif (qsymbols =="n"):
        print("Symbols will be omitted")
    else:
        print('Choose either "y" or "n"')
        include_symbols()
include_upper()
include_num()
include_symbols()

randomize = random.sample(all,length)
password = "".join(randomize)

print("Here is your generated password: ",password)

write_file()

