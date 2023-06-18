#. Write a program to check whether a number input by the user is a palindrome or not in python

def palindrome(n):
    rev=0
    temp=n
    while (n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    print(rev)
    if rev==temp:
        return "palindrome"
    else:
        return "not Palindrome"
a=int(input("Enter a number to check Palindome or not:"))
print(a," is ",palindrome(a))