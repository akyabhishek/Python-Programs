def movie(awards,k):
    newl=[]
    for j in range(0,len(awards)):
        x=awards[j]
        temp=[]
        temp.append(x)
        for i in range(1,len(awards)):
            d=diff(x,awards[i])
            if(d <=4):
                temp.append(awards[i])
                
        newl.append(temp)
    return newl

def diff(x,y):
    if x>y:
        return int(x-y)
    else:
        return int(y-x)
        


print(movie([1,13,6,8,9,3,5],4))