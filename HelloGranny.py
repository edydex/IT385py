#!usr/bin/env python3
#Hello *user_name* script

#Ask for name:
user_name = input("Greetings Sir, by what name should I be addressing You?\nMy name is ")
#Ask for year:
current_year = int( input("Oh, " + user_name +" thats a nice name. Now you see, I came here from a far away land and lost the track of time, would you mind telling me the year we're in?\nSure, the year is "))
#Respond to input, ask for their birth year
user_birthyear = int(input("That means that im already 69 years old, you seem pretty young though, which year were you born in?\nI was born in "))
#Math Section of script
user_age = current_year - user_birthyear
#Final Response 
print(f"Wow, {user_name}, you look pretty good for a {user_age} year old.")
#The next script works but it gives an error after it runs, even though it gives the desired results
#   print(f"Wow, {user_name}, you look pretty good for a {user_age} year old.").format(user_name, user_age)
#The script under doesn't work, I assume it has something to do with adding "user_name", which is a string, to "user_age", which is an intager.
#   print("Wow, " + user_name + ", you look pretty good for a " + user_age + "year old.")