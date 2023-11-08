name = input ("what's your name : ")
try:
    age = int(input("enter your age : "))
except ValueError:
    print("invalid_input")
    exit()
try:
    int(age)
except ValueError:
    print("invalid_input")
    print("try again")
    exit()
email = input("enter your email address : ")
phone = input("enter your phone number : ")
try:
    int(phone)
except ValueError:
    print("invalid input")
    print("try again")
    exit()
print("\n")
print("HELLO" + str(name) )
if age <= 50:
    print("YOU ARE TO YOUNG...")
    p = "Youth is a worthwhile phase of one's life. The age where the age group is no longer of a child but yet to turn out to be a grown-up is the youth age"
    print(p.title())
else:
    print("YOU ARE SUCH AN VALUABLE PERSON...")
    j = "Old age is when a person is near or beyond the usual life expectancy, usually from the age of 65 onwards"
    print(j.title())

u = "thanks for using me.......!"
print(u.upper())
