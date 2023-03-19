def getEnc(numbers):
    n=len(numbers)
    c=n-2
    while(n!=c):
        i=0
        j=1
        while(j<n):
            sum=numbers[i]+numbers[j]
            sum=int(sum%10)
            numbers[i]=sum
            i=i+1
            j=j+1
        n=n-1
    return str(numbers[0])+str(numbers[1])



print(getEnc([4,5,6,7]))