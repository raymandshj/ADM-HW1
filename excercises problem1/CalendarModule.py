# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar as cal
month, day, year = map(int,input().split())
print(cal.day_name[cal.weekday(year,month,day)].upper())
