def maxArr(arr):
    maxNum=arr[0]
    minNum=arr[0]
    for i  in range(0,len(arr)):
        if arr[i]>maxNum:
            maxNum=arr[i]
        if arr[i]<minNum:
            minNum=arr[i]
    return [maxNum,minNum]
    
print(maxArr([2,1,5,8,4,7,9]))