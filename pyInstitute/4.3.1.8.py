def mo2(yr):
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
modays = [31,mo2(yr),31, 30,31,30, 31,30,31, 30,31,30]
def day_of_the_year(yr, mo, da):
    return (da +mo2(yr))
    #mocount = 0
    #modays = [31, mo2, 31]
    #print([1], [2], [3])
    #while mo > mocount
    


b = mo2(1900)
c = day_of_the_year(2000, 3, 15)
d = modays
print(b)
print(c)