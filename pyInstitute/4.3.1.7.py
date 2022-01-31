def is_year_leap(year):
    if ((yr % 4) != 0):
        return False
    elif ((yr % 100) != 0):
        return True
    elif ((yr % 400) != 0):
        return False
    else:
        return True        
def days_in_month(year, month):
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



test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
