a=int(input())
b=int(input())
total=1
for i in range(a,b+1):
    if (i%2)!=0:
        total=total*i
print(total)
