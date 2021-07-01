def oddNumbers(l, r):
    x = []
    for i in range(l, r + 1):
        if i % 2 == 1:
            x.append(i)
    return x

f=int(input("Enter the starting num:"))
t=int(input("Enter the ending num:"))
print(oddNumbers(f,t))