def rev(s):
    str=''
    for i in s:
        str=i+str
    return str va

s="geeksforgeeks"
print("The original string is :",end='')
print(s)
print("The reversed string (using loop) is : ",end='')
print(rev(s))
