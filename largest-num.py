#Find the Biggest of 4 numbers


a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter fourth number: "))
if(a>b and a>c and a>d):
    print(a,"is the biggest number")
elif(b>a and b>c and b>d):
    print( b, "is the biggest number")
elif(c>a and c>b and c>d):
    print( c, "is the biggest number")
elif (d > a and d > b and d > c):
    print(d, "is the biggest number")
else:
    print("Invalid Choices of numbers")

#using list
l1=[]
n=int(input("Enter the how many numbers you want to compare:"))
for i in range(n):
    element=int(input("Enter the number : "))
    l1.append(element)
print(max(l1)," is the biggest number")