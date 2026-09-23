a=int(input())

year=a//365
week=a-(365*year)
week_7=(week//7)
day=week-(7*week_7)
day_1=(day//1)
print(str(year)+" years "+str(week_7)+" weeks "+str(day)+" days")