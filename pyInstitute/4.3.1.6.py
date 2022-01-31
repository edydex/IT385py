def is_year_leap(year):
    if ((yr % 4) != 0):
        return False
    elif ((yr % 100) != 0):
        return True
    elif ((yr % 400) != 0):
        return False
    else:
        return True  

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")