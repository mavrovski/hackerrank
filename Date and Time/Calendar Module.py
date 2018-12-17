import calendar


# print(calendar.TextCalendar(firstweekday=6).formatyear(2018))
#
month,day,year = map(int,input().split())
days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
day_of_week = days[calendar.weekday(year,month,day)]
print(day_of_week)

