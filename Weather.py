
# Alaska temperature averages
temp_high = {"Jan": 36, "Feb": 39, "March": 52, "April": 64, "May": 73, "June": 82, "July": 84, "Aug": 84, "Sep": 77, "Oct": 64, "Nov": 54, "Dec": 39}
temp_low = {"Jan": 21, "Feb": 23, "March": 34, "April": 45, "May": 54, "June": 64, "July": 66, "Aug": 66, "Sep": 57, "Oct": 46, "Nov": 36, "Dec": 25}
average_temp = {"Jan": 28, "Feb": 30, "March": 43, "April": 55, "May": 64, "June": 73, "July": 75, "Aug": 75, "Sep": 68, "Oct": 55, "Nov": 45, "Dec": 32}
# global variables
yr_temp = sum(average_temp.values())/12
above_average = dict()


def average_Alaska(month):
    temperature = 0
    for temp in month:
        temperature += month[temp]
    ave = temperature / len(average_temp)
    print ("The average temperature in Alaska is " + str(ave) + " degrees.")


def higher_temp(monthly):
    global yr_temp
    for high in monthly:
        if monthly[high] > yr_temp:
            above_average[high] = (monthly[high])
    print ("The months with above average temperatures are: " + str(above_average))

average_Alaska(average_temp)
higher_temp(average_temp)
