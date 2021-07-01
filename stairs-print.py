def staircase(n):
    for i in range(n):
        for k in range(n - i-1):
            print(" ", end="")
        for j in range(i+1):
            print('#',end="")
        print("")

i=int(input("Enter the no. of lines of stairs your want to print:"))
staircase(i)