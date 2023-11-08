s=input().split()
l=[]
u=''
for i in s:
    r=""
    for j in i:
        r=j+r
    l.append(r)
for p in l:
    u=u+p
    u=u+' '

print(u)
