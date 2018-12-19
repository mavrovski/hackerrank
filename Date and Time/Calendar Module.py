import calendar



month,day,year = map(int,input().split())
days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
day_of_week = days[calendar.weekday(year,month,day)]
print(day_of_week)

