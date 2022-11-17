# for addition
def add(x, y):
    print(x+y)
# for substraction
def substract(x, y):
    print(x-y)
# for multiplication
def multiply(x, y):
    print(x*y)
# for division
def divide(x, y):
    print(x/y)
# main body
a = float(input("enter 1st number="))
b = float(input("enter 2nd number="))
c = input("enter the work you want to do=")
#to decide the operation on it
if c == "addition":
    add(a,b)
elif c == "substraction":
    substract(a,b)
elif c == "multiplication":
    multiply(a,b)
else:
    divide(a,b)