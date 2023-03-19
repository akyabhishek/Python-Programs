def reverseArray(arr):
    rev=[]
    n=len(arr)
    for i in range(0,n):
        rev.append(arr[n-i-1])
    return rev

print(reverseArray([2,1,5,8,4,7,9]))