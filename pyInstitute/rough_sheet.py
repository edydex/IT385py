def is_year_leap(yr):
    if ((yr % 4) != 0):
        return False
    elif ((yr % 100) != 0):
        return True
    elif ((yr % 400) != 0):
        return False
    else:
        return True        
def days_in_month(yr, mo):
    if (mo == 2):
        if ((yr % 4) != 0):
            xtra=0
        elif ((yr % 100) != 0):
            xtra=1
        elif ((yr % 400) != 0):
            xtra=0
        else:
            xtra=1
        if (xtra ==1):
            return 29
        else:
            return 28
    elif (mo == (1 or 3 or 5 or 7 or 9 or 11)):
        return 31
    else:
        return 30
def day_of_the_year(yr, mo, da):
    while mo > 
    return(mo+30)



a = is_year_leap(2000)
b = days_in_month(2000, 2)
c = day_of_the_year(2000, 3, 15)
print(a)
print(b)
print(c)