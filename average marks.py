sum=0
for i in range(5):
    a=int(input("Enter the marks of the subject ="))
    sum+=a
avg=sum/5
print("The average mark is",avg)
if avg>60:
    print("You got a first class")