a=int(input("Enter the number ="))
su=0

temp=a
while temp>0:
    b=temp%10
    su+=b**3
    temp//=10

if su == a:
    print("Its a armstrong number")
else:
    print("Its not an Armstrong number")