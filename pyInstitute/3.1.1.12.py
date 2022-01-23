year = int(input("Enter a year: "))

year_div4 = year % 4
year_div100 = year % 100
year_div400 = year % 400

if year < 1582:
    print("Not within Gregorian calendar period")
elif year_div4 != 0:
    print("Common Year")
elif year_div100 != 0:
    print("Leap Year")
elif year_div400 != 0:
    print("Common Year")
elif year >= 1582:
    print("Leap Year")