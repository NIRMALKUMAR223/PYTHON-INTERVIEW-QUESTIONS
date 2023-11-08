import random as r

def target(n,target):
    while True:
        a=r.choice(n)
        b=r.choice(n)
        if a+b == target:
            print(f"The value is {a} + {b} =",target)
            break

lis=list(map(int,input(">>").split()))
t=int(input(">>"))
target(lis,t)
