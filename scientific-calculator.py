#Make a Scientific Calculator using Functions having min 6 operations
import  math
from fractions import Fraction

def sum(n):
    addition=0
    for i in range(n):
        num=float(input("Enter Number :"))
        addition=addition+num
    return addition

def multiplication(n):
    mul=1
    for i in range(n):
        num=float(input("Enter Number :"))
        mul=mul*num
    return mul

def pow(n,p):
    return (n**p)

def factorial(a):
    num = 1
    for i in range(a):
        num = (i + 1) * num
    return num

def permutation(n, r):
    return factorial(n) / factorial(n - r)


def combination(n, r):
    return factorial(n) / (factorial(n - r) * factorial(r))

def checkYN():
    if (ch == 'N' or ch == 'n'):
        return 0
    else:
        return 1

print("----Scientific Calculator---")
print("1\tAddition\n"
      "2\tSubtraction\n"
      "3\tMultiplication\n"
      "4\tDivision\n"
      "5\tSquare\n"
      "6\tCube\n"
      "7\tPower\n"
      "8\tFactorial\n"
      "9\tLogarithm\n"
      "10\tPermutation\n"
      "11\tCombination\n"
      )
i=1
while(i!=0):
    choice=int(input("Enter your Choice :"))
    if(choice==1):
        n=int(input("How many numbers you want to add:"))
        print("Addition : ",sum(n))
    elif(choice==2):
        a=float(input("Enter first Number:"))
        b=float(input("Enter first Number:"))
        print("Subtraction : ",a-b)
    elif(choice==3):
        n=int(input("How many numbers you want to multiply:"))
        print("Multiplication : ",multiplication(n))
    elif(choice==4):
        a = float(input("Enter first Number:"))
        b = float(input("Enter first Number:"))
        print("Division : ",a / b)
    elif(choice==5):
        a=int(input("Enter the number:"))
        print("Square of ",a,": ",pow(a,2))
    elif (choice == 6):
        a = int(input("Enter the number:"))
        print("Cube of ",a,": ", pow(a,3))
    elif(choice==7):
        a=int(input("Enter the number:"))
        p=int(input("Enter the power of number:"))
        print(a,"^",p," : ", pow(a, p))
    elif(choice==8):
        a=int(input("Enter the number to find Factorial:"))
        print("Factorial of ",a,":",factorial(a))
    elif(choice==9):
        a=int(input("Enter the number to find Logarithm :"))
        print("Logarithm of",a,":",math.log(a,10))
    elif (choice == 10 or choice == 11):
        n = int(input("Enter the value of n: "))
        r = int(input("Enter the value of r: "))
        if (n >= r):
            if (choice == 10):
                res = permutation(n, r)
            elif (choice == 11):
                res = combination(n, r)
            print(Fraction(res))
        else:
            print("Math Error")
    else:
        print("Invalid Choice")
    ch=input("Do you want to Continue (Y/N): ")
    i=checkYN()