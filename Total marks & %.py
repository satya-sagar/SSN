#Each subject is of 100 marks
a = int(input("Enter the number of subjects="))
L = []
sum = 0

for i in range(1, a+1):
    b = int(input("Enter the mark ="))
    L.append(b)
    sum+=b
print(L)
print("The total marks obtained is", sum)
print("The percentage is", (sum/(a*100)*100))