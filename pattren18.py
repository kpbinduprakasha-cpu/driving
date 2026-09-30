a=int(input())
b=int(input())
result=""
for i in range(a,b+1):
    is_odd=(i%2==1)
    
    if is_odd:
        result=result+str(i)+" "
print(result)
