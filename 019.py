#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

weekday=0
total=0
for year in range(1900, 2001):
    if (not year%4) and (year%100 or not year%400):
        month_length=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_length=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for idx, length in enumerate(month_length):
        for day in range(1,length+1):
            weekday=(weekday+1)%7
            if not weekday and day==1 and year>=1901:
                total+=1
print total
