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
def day_of_the_year(yr, mo, da):
    global doty
    doty = sum(modays[0:(mo-1)],da)
    return doty

test_years = [1900, 2000, 2016, 1987, 2021]
test_months = [2, 2, 1, 11, 12]
test_days = [28, 29, 31, 30, 31]
for i in range(len(test_years)):
    yr = test_years[i]
    mo2(yr)
    mo = test_months[i]
    modays = [31,mo2(yr),31, 30,31,30, 31,31,30, 31,30,31]
    da = test_days[i]
    if (modays[mo-1] >= da):
        result = day_of_the_year(yr, mo, da)
        print("The date ",da,"/",mo,"/",yr, " will be ", result, " days from since the year started.", sep="")
    else:
        print("Date does't exist")
