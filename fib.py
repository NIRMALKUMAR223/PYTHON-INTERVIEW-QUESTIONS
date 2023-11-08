n=5
a=0
b=1
fib=[]
fact=[]
for i in range(1,int(n)+1):
    c=a+b
    a=b
    b=c
    fib.append(c)
for i in fib:
    count=1
    for j in range(1,i+1):
        count=count*i
    fact.append(count)
print(fact)
