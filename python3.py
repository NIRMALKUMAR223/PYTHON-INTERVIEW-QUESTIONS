def power(base,exp):
    if exp==1:
        return base
    if exp!=1:
        return base*power(base,exp-1)
base=int(input('Enter the value of base: '))
exp=int(input('Enter the value of exp: '))
print('power value',power(base,exp))
