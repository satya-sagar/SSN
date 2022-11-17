# 1 dollar = 74.49 INR
def conversion(x):
    return(x*74.49)

print("convert dollar to Indian Rupees")
a=float(input("Enter currency in Dollars="))
b=conversion(a)
print(b)
