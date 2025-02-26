""" x = 3
y = float(x)
print(x,y) """

""" values = [1,2,23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
print(values[0])
print(values[6]) """

""" "test"
["t","e","s","t"] """

""" x = "this is a thing"
y= x.split()
z = y[0]
print(y)
print(z) """

#Challenge

sentence = input("enter a sentence:")
words = sentence.split()
count = len(words)
print(count)

#Mad Libs Project

""" a = input("enter a celebrity:")
b = input("enter a verb1:")
c = input("enter a verb2:")
d = input("enter a noun:")
e = input("enter a number:")

Mad_lib = print(f"{a} went to {d} by {b} there, but {a} couldn't get {d} so they started {c}. It took them {e} minutes to get there...")
print(Mad_lib) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 70
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

#Challenge 2

""" import math
x = int(input("enter a number: "))
y = math.gcd(x,2)

if y ==2:
    print("even")
else:
    print("odd") """

#notes
""" def login(password):
    #if statement evaluates to true do next line
    if password == "secret":
        print("logged in")
    else:
        print("incorrect password")
login("secrets") """

""" def temp(x):
    if x >=80:
        print("too hot")
    elif 80> x >60:
        print("nice")
    else:
        print("Too Cold")
x = int(input("what da temp?"))
temp(x) """

#use modeulo to check remainder for 1 factor
#use a loop to check all potential factors range(2,15)
#conditional statement if factor append to list
#print the list

#Challenge 3 

"""
a = int(input("enter a bill: "))
b = input("Was the service: bad, okay, good, or great? ")

if b =="bad":
        print(a)
elif b =="okay":
        print(a*1.15)
elif b =="good":
        print(a*1.2)
elif b =="great":
        print(a*1.25)
else:
        print("Not an option") """

#Challenge 4

""" x = int(input("enter a number: "))

for factors in range(2,x+1):
    if x % factors ==0:
        print(factors) """

#Gambling code

""" isRich = True
is21 = True

def canGamble(isRich, is21):
    if isRich == True and is21 ==True:
        print("Let it ride!")
    elif isRich == False and is21 == True:
        print("You are too poor, get out")
    elif isRich == False or is21 == False:
        print("you cannot play") """

#Challenge 5

""" x = int(input("enter a number: "))
y = int(input("enter another number: "))
z = 1
for factors in range(1, min(x, y)+1):
    if x % factors ==0 and y % factors ==0:
        z = factors
print(z) """