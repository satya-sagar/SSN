#WAP that asks your height in centimeters and returns in foot and inches, :)

a=int(input("Enter the height in centimeters ="))
b=a/2.54    #because 1 inch is 2.54 cms
c=round(b/12,2)
print("Your height is",c,"foot")