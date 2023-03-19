import math
def sum_two(arr):
    newarr=[]
    end=len(arr)
    if(end==2):
        return arr
    else:
        if (end%2)==0:
            
            r=int(end/2)
            
        else:
            r=int((end/2))+1
        for i in range(r):
            print(i)
            
            if(i==end-i-1):
                newarr.append(arr[i])
            else:
                newarr.append(arr[i]+arr[end-i-1])
        if(len(newarr)>2):
        
            return sum_two(newarr)
        else:
            return newarr
arr=[3,2]
print(sum_two(arr))